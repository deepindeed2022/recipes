#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from xml.etree import ElementTree as ET 

def parse_xmltree(tree):
	'''
	argv:
		tree    ElementTree
	return:
		picname 图片的名称
		size    图片的大小
		objects 几个boundingbox的列表
	'''
	size = dict()
	objs = []
	filename = tree.find("filename")
	picname = filename.text
	for i in tree.find("size"):
		size[i.tag] = int(i.text)
	#需要更多的数据集信息，更改这里
	for obj in tree.findall("object"):
		bbox = dict()
		for tags in obj:
			if "name" == tags.tag:
				bbox["classname"] = tags.text
			elif "bndbox" == tags.tag:
				for p in tags:
					bbox[p.tag] = int(p.text)
		objs.append(bbox)
	return picname, size, objs

def xml_iter(filepaths):
	for filepath in filepaths:
		tree = ET.parse(filepath)
		yield parse_xmltree(tree)
		