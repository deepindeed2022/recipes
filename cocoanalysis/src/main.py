#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os.path
import math
from collections import Counter,OrderedDict

from util import *
from config import *
from plot import *
from cocojson import getImages

def main(dataset, resize_width, resize_height, strip_size, 
         have_half, is_cover, result_dir):
    hist_map = "{}/{}_{}_{}_{}.png".format(result_dir,"hist_map",resize_width, resize_height, strip_size)
    heat_map = "{}/{}_{}_{}_{}.png".format(result_dir,"heat_map", resize_width, resize_height, strip_size)
    blubble_map = "{}/{}_{}_{}.png".format(result_dir,"blubble_map", resize_width, resize_height, strip_size)
    bar_png = "{}/{}_{}_{}_{}.png".format(result_dir,"bar",resize_width, resize_height, strip_size)

    count_file = "{}/count_{}_{}_{}.txt".format(result_dir, resize_width, resize_height, strip_size)
    # GroundTruth box aspect radio
    wh_aspect_radio = Counter()
    wh_aspect_radio_file = "{}/wh_aspect_radio_{}_{}_{}.txt".format(result_dir,resize_width, resize_height, strip_size)
    hw_aspect_radio = Counter()
    hw_aspect_radio_file = "{}/hw_aspect_radio_{}_{}_{}.txt".format(result_dir,resize_width, resize_height, strip_size)
     
    count_map = [[0 for _ in xrange(resize_width/strip_size)] for _ in xrange(resize_height/strip_size)]

    image_count = 0
    images = getImages(dataset)
    for picid, image in images.items():
        image_count += 1
        width = image["width"]
        height = image["height"]
        objs = image['objects']
        for obj in objs:

            objw, objh = obj[2], obj[3]
            
            if not have_half:
                wh_aspect_radio[round(float(objw)/objh)] += 1
                hw_aspect_radio[round(float(objh)/objw)] += 1
            else: # get include .5 aspect radio result
                wh_aspect_radio[float(round(float(objw*2)/objh))/2] += 1
                hw_aspect_radio[float(round(float(objh*2)/objw))/2] += 1

            # classname we not use it, but have the information

            wx, hy = getwh_center_point(width=width, height=height, 
                   xmin=obj[0], ymin=obj[1], owidth=obj[2], oheight=obj[3], 
                   resize_width=resize_width, resize_height=resize_height)
            count_map[hy/strip_size][wx/strip_size] = count_map[hy/strip_size][wx/strip_size] + 1
            #count_map[wx/strip_size][hy/strip_size] = count_map[wx/strip_size][hy/strip_size] + 1
        if image_count % 10 == 0:
            print "have get %d images" %(image_count)
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

if __name__ == '__main__':

    if len(sys.argv) > 2:
        TRAIN = sys.argv[1]
        strip_size = int(sys.argv[2])
    else:
        TRAIN = "train"
    data_dir = "../annotations"
    result_dir = "../result/{}".format(TRAIN)
    annot_path=""
    if TRAIN == "train":
        annot_path = os.path.abspath("{}/{}".format(data_dir, "instances_train2014.json"))
    elif TRAIN == "test":
        annot_path = os.path.abspath("{}/{}".format(data_dir, "instances_val2014.json"))
    print "init params finished"
    main(annot_path, resize_width, resize_height, strip_size, 
         have_half, is_cover, result_dir)
