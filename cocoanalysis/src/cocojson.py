#!/usr/bin/python
#-*-encoding:utf-8-*-
import json
from collections import defaultdict

def getImages(filename):
    print "start read %s" % (filename)
    data = ""
    with open(filename, "r") as f:
        line = f.readline() 
        data = json.loads(line)
    print "finished load data"
    leyer1_keys = data.keys()

    assert 'annotations' in leyer1_keys
    assert 'images' in leyer1.keys
    print "assert correct"
    _images = data['images']
    _annotations = data['annotations']

    images = dict()
    count = 0
    print "start combined the images"
    try:
        for image in _images:
            count += 1
            images[image['id']] = { 'width':image['width'], 'height':image['height'],'objects':list()}
            if count % 100 == 0:
                print "read %d image information " % (count)
    except KeyError, e:
        print "KeyError %dth image " % (count)
        return

    anno_count = 0
    img_id = -1
    try:
        for anno in _annotations:
            anno_count += 1
            img_id = anno['anno']
            area = anno['area']
            bbox = anno['bbox']
            images[img_id]['objects'].append(bbox)
            if anno_count % 100 == 0:
                print "read %d image objects information " % (anno_count)
    except KeyError, e:
        print "KeyError %s" % (img_id)
        return 
    return images

    
