from __future__ import division
import math


clip = False
def prior_box_layer(kmeans_ratios, 
    min_sizes, max_sizes, step, offset, layer_width, 
    flip=True, img_width=321, img_height=321):
    assert len(kmeans_ratios) == 3
    assert len(min_sizes) == 1
    assert len(max_sizes) == 1

    assert offset <= img_width
    assert step <= img_width

    aspect_ratios = [1.]
    for i in range(len(kmeans_ratios)):
        ar = kmeans_ratios[i]
        already_exist = False
        for tar in aspect_ratios:
            if abs(tar - ar) < 1e-6:
                already_exist = True
                break
        if not already_exist:
            aspect_ratios.append(ar)
            if flip:
                aspect_ratios.append(1./ar);
    # print "aspect_ratios:", aspect_ratios

    num_priors = len(aspect_ratios) * len(min_sizes)

    # using max_size
    for i in range(len(max_sizes)):
       assert max_sizes[i] > min_sizes[i]
       num_priors += 1 

    step_h = step
    step_w = step    
    offset_ = offset
    # step_h = img_height/layer_height
    # step_w = img_width/layer_width

    layer_height = layer_width
    top_data = [[0.0, 0.0, 0.0, 0.0]] * (num_priors * layer_width * layer_height)
    center_data = [[0.0, 0.0]] * (layer_width * layer_height)
    idx = 0
    cidx = 0
    center_x = center_y = 0.
    for h in xrange(layer_height):
        for w in xrange(layer_width):
            # center_x = (w + offset_/(img_width/layer_width)) * step_w
            # center_y = (h + offset_/(img_height/layer_height)) * step_h
            
            center_x = (w + offset_) * step_w
            center_y = (h + offset_) * step_h

            center_data[cidx] = [center_x, center_y]
            # print center_data[cidx], cidx
            cidx += 1
            for s in xrange(len(min_sizes)):
                # first prior: aspect_ratio = 1, size = min_size
                min_size_ = min_sizes[s]
                box_height = min_size_
                box_width =  min_size_
                # print box_height
                # xmin
                top_data[idx][0] = (center_x - box_width/2.)/img_width
                # ymin
                top_data[idx][1] = (center_y - box_height/2.)/img_height
                # xmax
                top_data[idx][2] = (center_x + box_width/2.)/img_width
                # ymax
                top_data[idx][3] = (center_y + box_height/2.)/img_height
                
                # print top_data[idx]
                idx += 1
                if len(max_sizes) > 0: 
                    max_size_ = max_sizes[s]
                    # second prior: aspect_ratio = 1, size = sqrt(min_size * max_size)
                    box_height = math.sqrt(min_size_*max_size_)
                    box_width = box_height
                    # print box_height
                    # xmin
                    top_data[idx][0] = (center_x - box_width / 2.) / img_width
                    # ymin
                    top_data[idx][1] = (center_y - box_height / 2.) / img_height
                    # xmax
                    top_data[idx][2] = (center_x + box_width / 2.) / img_width
                    # ymax
                    top_data[idx][3] = (center_y + box_height / 2.) / img_height
         
                    idx += 1
                # print top_data[idx - 1]
                # print top_data[idx - 2]
                # return   
                for r in xrange(len(aspect_ratios)):
                    ar = aspect_ratios[r]
                    if abs(1.0 - ar) < 1e-6: continue
                    box_width = min_size_ * math.sqrt(ar)
                    box_height = min_size_ / math.sqrt(ar)
                    # print box_height
                    # xmin
                    top_data[idx][0] = (center_x - box_width / 2.) / img_width
                    # ymin
                    top_data[idx][1] = (center_y - box_height / 2.) / img_height
                    # xmax
                    top_data[idx][2] = (center_x + box_width / 2.) / img_width
                    # ymax
                    top_data[idx][3] = (center_y + box_height / 2.) / img_height
        
                    idx += 1

    if clip:
        for i in xrange(len(top_data)):
            top_data[i][0] = min(max(top_data[i][0], 0.0), 1.0)
            top_data[i][1] = min(max(top_data[i][1], 0.0), 1.0)
            top_data[i][2] = min(max(top_data[i][2], 0.0), 1.0)
            top_data[i][3] = min(max(top_data[i][3], 0.0), 1.0)

    return top_data, center_data

def main():
    # parameters for generating priors.
    # minimum dimension of input image
    min_dim = 321
    # res3b3_relu ==> 48 x 48
    # res5c_relu ==> 24 x 24
    # res6_relu ==> 12 x 12
    # res7_relu ==> 6 x 6
    # res8_relu ==> 3 x 3
    # res9_relu ==> 1x1
    mbox_source_layers = ['res3b3_relu', 'res5c_relu', 'res6_relu', 'res7_relu', 'res8_relu', 'res9_relu']
    # print mbox_source_layers[4::-1]
    layer_widths = [40, 20, 10, 5, 3, 1]
    #layer_widths = [48, 24, 12, 6, 3, 1]

    # in percent %
    min_ratio = 20
    max_ratio = 95
    step = int(math.floor((max_ratio - min_ratio) / (len(mbox_source_layers) - 2)))
    min_sizes = []
    max_sizes = []
    for ratio in xrange(min_ratio, max_ratio + 1, step):
      min_sizes.append(min_dim * ratio / 100.)
      max_sizes.append(min_dim * (ratio + step) / 100.)
    min_sizes = [min_dim * 10 / 100.] + min_sizes
    max_sizes = [min_dim * 20 / 100.] + max_sizes
    steps = [8, 16, 32, 64, 64, 321]

    cell_offsets = [2.5, 2.5, 10.5, 26.5, 90.5, 160.5]
    # get the offset_radio

    for i in xrange(len(steps)):
        cell_offsets[i] = cell_offsets[i]/(min_dim/layer_widths[i])

    print cell_offsets
    kmeans_ratios = [1.60, 2.0, 3.0]
    # inter_layer_depth = [[256], [256], [256], [256], [256], [256]]
    # prediction_kernels= [5, 5, 3, 3, 3, 3]
    # prediction_pads = [2,2,1,1,1,1]

    img_width = img_height = 321
    flip = True
    def print_init():
        print "Layer:",
        for i in xrange(len(mbox_source_layers)): print mbox_source_layers[i], " ",
        print

        print "step:",
        for i in xrange(len(mbox_source_layers)): print steps[i], " ",
        print
        print "offset:",
        for i in xrange(len(mbox_source_layers)): print cell_offsets[i], " ",
        print
        print "min_size:",
        for i in xrange(len(mbox_source_layers)): print min_sizes[i], " ",
        print

        print "max_size:",
        for i in xrange(len(mbox_source_layers)): print max_sizes[i], " ",
        print
    # print_init()
    for i in xrange(len(mbox_source_layers)):
        top_data, center = prior_box_layer(kmeans_ratios=kmeans_ratios, 
            min_sizes=[min_sizes[i]], max_sizes=[max_sizes[i]], 
                    step=steps[i], offset=cell_offsets[i], layer_width=layer_widths[i])
        # for j in xrange(len(top_data)):
        #     mbox = top_data[j]
        #     print "(%f, %f, %f, %f)" % (mbox[0], mbox[1], mbox[2], mbox[3])
        assert len(top_data) == layer_widths[i]**2*8
        assert len(center) == layer_widths[i]**2
        for j in xrange(len(center)):
            print "(%f, %f)" % (center[j][0], center[j][1])


if __name__ == '__main__':
    main()
