#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os.path
import math
from collections import Counter,OrderedDict

from util import *
from xmlio import xml_iter
from config import *
from plot import *


def main(dataset, resize_width, resize_height, strip_size, 
         have_half, is_cover, result_dir):
    hist_map = "{}/{}_{}_{}_{}.png".format(result_dir,"hist_map",resize_width, resize_height, strip_size)
    heat_map = "{}/{}_{}_{}_{}.png".format(result_dir,"heat_map", resize_width, resize_height, strip_size)
    blubble_map = "{}/{}_{}_{}.png".format(result_dir,"blubble_map", resize_width, resize_height, strip_size)
    bar_png = "{}/{}_{}_{}_{}.png".format(result_dir,"bar",resize_width, resize_height, strip_size)
    # objections Counter
    obj_table = Counter()
    count_file = "{}/count_{}_{}_{}.txt".format(result_dir, resize_width, resize_height, strip_size)
    # GroundTruth box aspect radio
    wh_aspect_radio = Counter()
    wh_aspect_radio_file = "{}/wh_aspect_radio_{}_{}_{}.txt".format(result_dir,resize_width, resize_height, strip_size)
    hw_aspect_radio = Counter()
    hw_aspect_radio_file = "{}/hw_aspect_radio_{}_{}_{}.txt".format(result_dir,resize_width, resize_height, strip_size)
     
    count_map = [[0 for _ in xrange(resize_width/strip_size)] for _ in xrange(resize_height/strip_size)]

    filecount = 0
    for picname, size, objs in xml_iter(dataset):
        filecount += 1
        if filecount % 100 == 0:
            print "have process %d xml files" %(filecount)
        width = size["width"]
        height = size["height"]
        for obj in objs:
            obj_table[obj["classname"]] += 1
            objw, objh = get_width_height(xmin=obj["xmin"], ymin=obj["ymin"], xmax=obj["xmax"], ymax=obj["ymax"])
            
            if not have_half:
                wh_aspect_radio[round(float(objw)/objh)] += 1
                hw_aspect_radio[round(float(objh)/objw)] += 1
            else: # get include .5 aspect radio result
                wh_aspect_radio[float(round(float(objw*2)/objh))/2] += 1
                hw_aspect_radio[float(round(float(objh*2)/objw))/2] += 1

            # classname we not use it, but have the information
            if not is_cover:
                wx, hy = get_center_point(width=width, height=height, 
                       xmin=obj["xmin"], ymin=obj["ymin"], xmax=obj["xmax"], ymax=obj["ymax"], 
                       resize_width=resize_width, resize_height=resize_height)
                count_map[hy/strip_size][wx/strip_size] = count_map[hy/strip_size][wx/strip_size] + 1
            else:
                for wx in range(obj["xmin"], obj["xmax"]):
                    for hy in range(obj["ymin"], obj["ymax"]):
                        x, y = math.trunc(float(wx)/width*resize_width), math.trunc(float(hy)/height*resize_height)
                        try:
                            count_map[x/strip_size][y/strip_size] = count_map[x/strip_size][y/strip_size] + 1
                        except IndexError, e:
                            print "ErrorIndex:",x, y
                            return
    # width
    x = [i*strip_size for _ in xrange(resize_height/strip_size) for i in xrange(resize_width/strip_size)]
    # height
    y = [i*strip_size for i in xrange(resize_height/strip_size) for _ in xrange(resize_width/strip_size)]
    z = np.array(count_map).flatten()
    # z = [count_map[i][j] for i in xrange(resize_height/strip_size) for j in xrange(resize_width/strip_size)]

    draw_bar3d(z, resize_width, resize_height, strip_size, bar_png)
    draw_histmap(z, x, y, hist_map)
    draw_blubble(z, x, y, blubble_map)
    draw_heatmap(count_map, [i*strip_size for i in xrange(resize_height/strip_size)], [i*strip_size for i in xrange(resize_width/strip_size)], heat_map)

    # sorted the result following the value size
    wh_aspect_radio_order = OrderedDict(sorted(wh_aspect_radio.items(), key=lambda t: t[1]))
    write_counter(wh_aspect_radio_order, wh_aspect_radio_file)
    hw_aspect_radio_order = OrderedDict(sorted(hw_aspect_radio.items(), key=lambda t: t[1]))
    write_counter(hw_aspect_radio_order, hw_aspect_radio_file)

    write_map(count_map, count_file)



data_dir = "../data"
result_dir = "../{}_result".format(TRAIN)
if TRAIN == "train":
    annotdir_path = os.path.abspath("{}/{}".format(data_dir, "train/VOC2007/Annotations"))
elif TRAIN == "test":
    annotdir_path = os.path.abspath("{}/{}".format(data_dir, "test/VOC2007/Annotations"))
else:
    annotdir_path = os.path.abspath("../data/test/test")
dataset = get_annotations_filepaths(annotdir_path)


if __name__ == '__main__':
    main(dataset, resize_width, resize_height, strip_size, 
         have_half, is_cover, result_dir)

