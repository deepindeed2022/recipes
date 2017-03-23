#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
import os
import sys
import math

def write_map(cmap, filename):
    with open(filename, "w") as f:
        assert( len(cmap) > 0 and len(cmap[0]) > 0)
        print >> f, "%d  %d" % (len(cmap[0]), len(cmap)) 
        for i in xrange(len(cmap)):
            for j in xrange(len(cmap[0])):
                print >> f, "%d  " % (cmap[i][j]) ,
            print >> f
# print out the counter to file
def write_counter(obj_table, filename):
    with open(filename, "w") as f:
        for key, val in reversed(obj_table.items()):
            print >> f, "%s  %d" % (key, val)

def get_annotations_filepaths(annot_path):
	filenames = os.listdir(annot_path) 
	for i in xrange(len(filenames)):
		filenames[i] = "{}/{}".format(annot_path, filenames[i])
	return filenames

def get_width_height(xmin, ymin, xmax, ymax):
	return xmax-xmin+1, ymax-ymin+1

def get_center_point(width, height, xmin, ymin, xmax, ymax, resize_width=None, resize_height=None):
	assert(width > 0 and height > 0)
	assert(xmin <= width and ymin <= height)
	assert(xmax <= width and ymax <= height)
	if(resize_height == None or resize_width == None): 
		resize_width = width
		resize_height = height

	return math.trunc(((xmin + (xmax-xmin+1)/2)/(width))*resize_width), math.trunc(((ymin+(ymax-ymin+1)/2)/(height))*resize_height)
if __name__ == '__main__':
	annotdir_path = os.path.abspath("../VOC2007/Annotations")
	print get_center_point(200, 300, 1, 3, 150, 120, 400, 601)
