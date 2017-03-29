#!/usr/bin/python
#-*-encoding:utf-8-*-
import json


def getImages(filename):
    print "start read %s" % (filename)
    data = ""
    with open(filename, "r") as f:
        data = json.load(f)

    leyer1_keys = data.keys()

    assert 'annotations' in leyer1_keys
    assert 'images' in leyer1_keys

    _images = data['images']
    _annotations = data['annotations']

    images = dict()
    count = 0
    print "\n\n-------------start combined the images----------------\n\n"
    try:
        for image in _images:
            count += 1
            images[image['id']] = { 'width':image['width'], 'height':image['height'],'objects':[]}
            if count % 1000 == 0:
                print "%d images information" % (count)
    except KeyError, e:
        print "KeyError %dth image " % (count)
        return
    print '---------------total images number:%d---------------' % (count)

    anno_count = 0
    img_id = -1
    print "\n\n-------------start insert bbox----------------\n\n"
    try:
        for anno in _annotations:
            anno_count += 1
            img_id = anno['image_id']
            area = anno['area']
            assert 'bbox' in anno.keys()
            bbox = anno['bbox']
            images[img_id]['objects'].append(bbox)
            if anno_count % 1000 == 0:
                print "%d image objects inserted" % (anno_count)
                return images
    except KeyError, e:
        print "KeyError %s" % (img_id)
        return images
    return images

    
if __name__ == '__main__':
    data = ""
    fname = '../annotations/test.json'

    images = getImages(fname)
    print images
    for image in images.values():
        if len(image['objects']):
            print image
    # with open('test.json', "r") as f:
    #     data = json.load(f)
    # with open("small.json", 'w') as f:
    #     print f, json.dumps(data, indent=2)
