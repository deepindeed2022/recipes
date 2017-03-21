#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os.path
import math
from collections import Counter,OrderedDict
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from util import get_annotations_filepaths, get_center_point,get_width_height
from xmlio import xml_iter

def plot3d_countmap(x, y, z, savefile="count_map.png"):
    fig = plt.figure()
    ax = Axes3D(fig)
    #ax = fig.gca(projection='3d')
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_zlabel('Objects Count')
    plt.show()
    plt.savefig("{}/{}".format(os.path.dirname(annotdir_path), savefile))

def plot32_surface(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Plot the surface.
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                           linewidth=1, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(0, 2000)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def draw_heatmap(data, xlabels, ylabels):
    figure=plt.figure(facecolor='w')
    ax=figure.add_subplot(2,1,1,position=[1,1,1,1])
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax=data[0][0]
    vmin=data[0][0]
    for i in data:
        for j in i:
            if j>vmax:
                vmax=j
            if j<vmin:
                vmin=j
    _map = ax.imshow(data,interpolation='lanczos',cmap='viridis',aspect='auto',vmin=vmin,vmax=vmax)
    cb = plt.colorbar(mappable=_map,cax=None,ax=None,shrink=2)
    plt.show()
    plt.savefig("{}/{}".format(os.path.dirname(annotdir_path), "heatmap.png"))

def draw_blubble(data, x, y):
    colors = np.random.rand(len(x))
    plt.scatter(x, y, s=data, c=colors, alpha=1)
    plt.show()

def writefile(cmap, filename):
    with open(filename, "w") as f:
        assert( len(cmap) > 0 and len(cmap[0]) > 0)
        print >> f, "%d  %d" % (len(cmap[0]), len(cmap)) 
        for i in xrange(len(cmap)):
            for j in xrange(len(cmap[0])):
                print >> f, "%d  " % (cmap[i][j]) ,
            print >> f
# print out the counter to file
def write_counter(filename, obj_table):
    with open(filename, "w") as f:
        for key, val in reversed(obj_table.items()):
            print >> f, "%s  %d" % (key, val)
# configure the super parameters

annotdir_path = os.path.abspath("../VOC2007/Annotations")
# annotdir_path = os.path.abspath("../test/VOC2007/Annotations")
resize_width = 400
resize_height = 400
filepaths = get_annotations_filepaths(annotdir_path)
strip_size = 20
obj_table = Counter()
wh_aspect_radio = Counter()
hw_aspect_radio = Counter()

count_map = [[0 for _ in xrange(resize_width/strip_size)] for _ in xrange(resize_height/strip_size)]
def main():
    filecount = 0
    for picname, size, objs in xml_iter(filepaths):
        filecount += 1
        if filecount % 100 == 0:
            print "have process %d xml files" %(filecount)
        width = size["width"]
        height = size["height"]
        for obj in objs:
            obj_table[obj["classname"]] += 1
            objw, objh = get_width_height(xmin=obj["xmin"], ymin=obj["ymin"], xmax=obj["xmax"], ymax=obj["ymax"])
            #k = float(math.trunc((float(objw)/objh)*10))/10
            wh_aspect_radio[round(float(objw)/objh)] += 1
            hw_aspect_radio[round(float(objh)/objw)] += 1
            #wh_aspect_radioat(round(float(objw*2)/objh))/2] += 1
            #hw_aspect_radio[float(round(float(objh*2)/objw))/2] += 1
            # classname we not use it, but have the information
            wx, hy = get_center_point(width=width, height=height, 
                    xmin=obj["xmin"], ymin=obj["ymin"], xmax=obj["xmax"], ymax=obj["ymax"], 
                    resize_width=resize_width, resize_height=resize_height)
            count_map[hy/strip_size][wx/strip_size] = count_map[hy/strip_size][wx/strip_size] + 1
            
            # for wx in range(obj["xmin"], obj["xmax"]):
            #     for hy in range(obj["ymin"], obj["ymax"]):
            #         wx, hy = math.trunc(wx/width*resize_width), math.trunc(hy/height*resize_height)
            #         try:
            #             count_map[wx/strip_size][hy/strip_size] = count_map[wx/strip_size][hy/strip_size] + 1
            #         except IndexError, e:
            #             print wx, hy
            #             return
    writefile(count_map, "result.map")
    # width
    x = [i*strip_size for _ in xrange(resize_height/strip_size) for i in xrange(resize_width/strip_size)]
    # height
    y = [i*strip_size for i in xrange(resize_height/strip_size) for _ in xrange(resize_width/strip_size)]
    z = [count_map[i][j] for i in xrange(resize_height/strip_size) for j in xrange(resize_width/strip_size)]
    
    # print the max value accur index
    #wh = z.index(max(z))
    #print wh/(resize_width/strip_size), wh%(resize_height/strip_size), max(z)
    #plot3d_countmap(x, y, z)

    #draw_blubble(z, x, y)
    draw_heatmap(count_map, [i*strip_size for i in xrange(resize_height/strip_size)], [i*strip_size for i in xrange(resize_width/strip_size)])

    #aspect_radio_order = OrderedDict(sorted(aspect_radio.items(), key=lambda t: t[1]))
    write_counter("class_type_counter.txt", obj_table)
    wh_aspect_radio_order = OrderedDict(sorted(wh_aspect_radio.items(), key=lambda t: t[1]))
    hw_aspect_radio_order = OrderedDict(sorted(hw_aspect_radio.items(), key=lambda t: t[1]))
    write_counter("wh_aspect_radio.txt", wh_aspect_radio_order)
    write_counter("hw_aspect_radio.txt", hw_aspect_radio_order)




if __name__ == '__main__':
    main()

