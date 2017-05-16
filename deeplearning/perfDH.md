## 测试配置
vendor_id	: GenuineIntel
cpu family	: 6
model		: 63
model name	: Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz
stepping	: 2
microcode	: 0x2b
cpu MHz		: 1201.031
cache size	: 15360 KB
physical id	: 0
siblings	: 12
core id		: 5
cpu cores	: 6
apicid		: 11
initial apicid	: 11
fpu		: yes
fpu_exception	: yes
cpuid level	: 15
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
bogomips	: 4788.39
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual

## SSDH的时间性能测评(AlexNet as Based Network)

I0515 10:57:49.628947 22577 caffe.cpp:354] Average time per layer: 
I0515 10:57:49.628958 22577 caffe.cpp:357]      conv1	forward: 107.053 ms.
I0515 10:57:49.628969 22577 caffe.cpp:360]      conv1	backward: 105.425 ms.
I0515 10:57:49.628979 22577 caffe.cpp:357]      relu1	forward: 2.84564 ms.
I0515 10:57:49.628988 22577 caffe.cpp:360]      relu1	backward: 0.00078 ms.
I0515 10:57:49.628998 22577 caffe.cpp:357]      pool1	forward: 10.6856 ms.
I0515 10:57:49.629007 22577 caffe.cpp:360]      pool1	backward: 0.0012 ms.
I0515 10:57:49.629015 22577 caffe.cpp:357]      norm1	forward: 25.3017 ms.
I0515 10:57:49.629079 22577 caffe.cpp:360]      norm1	backward: 27.1995 ms.
I0515 10:57:49.629089 22577 caffe.cpp:357]      conv2	forward: 215.88 ms.
I0515 10:57:49.629098 22577 caffe.cpp:360]      conv2	backward: 207.647 ms.
I0515 10:57:49.629107 22577 caffe.cpp:357]      relu2	forward: 1.8269 ms.
I0515 10:57:49.629115 22577 caffe.cpp:360]      relu2	backward: 0.00078 ms.
I0515 10:57:49.629139 22577 caffe.cpp:357]      pool2	forward: 7.11902 ms.
I0515 10:57:49.629149 22577 caffe.cpp:360]      pool2	backward: 0.001 ms.
I0515 10:57:49.629158 22577 caffe.cpp:357]      norm2	forward: 25.614 ms.
I0515 10:57:49.629168 22577 caffe.cpp:360]      norm2	backward: 26.1617 ms.
I0515 10:57:49.629178 22577 caffe.cpp:357]      conv3	forward: 134.347 ms.
I0515 10:57:49.629202 22577 caffe.cpp:360]      conv3	backward: 128.527 ms.
I0515 10:57:49.629212 22577 caffe.cpp:357]      relu3	forward: 0.61962 ms.
I0515 10:57:49.629223 22577 caffe.cpp:360]      relu3	backward: 0.00086 ms.
I0515 10:57:49.629232 22577 caffe.cpp:357]      conv4	forward: 105.862 ms.
I0515 10:57:49.629242 22577 caffe.cpp:360]      conv4	backward: 101.532 ms.
I0515 10:57:49.629252 22577 caffe.cpp:357]      relu4	forward: 0.61826 ms.
I0515 10:57:49.629261 22577 caffe.cpp:360]      relu4	backward: 0.00078 ms.
I0515 10:57:49.629271 22577 caffe.cpp:357]      conv5	forward: 74.0428 ms.
I0515 10:57:49.629307 22577 caffe.cpp:360]      conv5	backward: 70.8545 ms.
I0515 10:57:49.629325 22577 caffe.cpp:357]      relu5	forward: 0.41396 ms.
I0515 10:57:49.629334 22577 caffe.cpp:360]      relu5	backward: 0.00078 ms.
I0515 10:57:49.629344 22577 caffe.cpp:357]      pool5	forward: 2.84446 ms.
I0515 10:57:49.629360 22577 caffe.cpp:360]      pool5	backward: 0.00114 ms.
I0515 10:57:49.629369 22577 caffe.cpp:357]        fc6	forward: 58.0599 ms.
I0515 10:57:49.629386 22577 caffe.cpp:360]        fc6	backward: 46.34 ms.
I0515 10:57:49.629396 22577 caffe.cpp:357]      relu6	forward: 0.04094 ms.
I0515 10:57:49.629415 22577 caffe.cpp:360]      relu6	backward: 0.00068 ms.
I0515 10:57:49.629423 22577 caffe.cpp:357]      drop6	forward: 0.33852 ms.
I0515 10:57:49.629434 22577 caffe.cpp:360]      drop6	backward: 0.00128 ms.
I0515 10:57:49.629451 22577 caffe.cpp:357]        fc7	forward: 25.66 ms.
I0515 10:57:49.629462 22577 caffe.cpp:360]        fc7	backward: 22.1418 ms.
I0515 10:57:49.629472 22577 caffe.cpp:357]      relu7	forward: 0.04096 ms.
I0515 10:57:49.629495 22577 caffe.cpp:360]      relu7	backward: 0.00072 ms.
I0515 10:57:49.629539 22577 caffe.cpp:357]      drop7	forward: 0.33168 ms.
I0515 10:57:49.629554 22577 caffe.cpp:360]      drop7	backward: 0.00076 ms.
I0515 10:57:49.629565 22577 caffe.cpp:357]     latent	forward: 0.31342 ms.
I0515 10:57:49.629575 22577 caffe.cpp:360]     latent	backward: 0.25514 ms.
I0515 10:57:49.629585 22577 caffe.cpp:357] latent_sigmoid	forward: 0.0209 ms.
I0515 10:57:49.629597 22577 caffe.cpp:360] latent_sigmoid	backward: 0.00086 ms.
I0515 10:57:49.629612 22577 caffe.cpp:365] Average Forward pass: 799.935 ms.
I0515 10:57:49.629623 22577 caffe.cpp:367] Average Backward pass: 736.139 ms.
I0515 10:57:49.629631 22577 caffe.cpp:369] Average Forward-Backward: 1536.14 ms.
I0515 10:57:49.629642 22577 caffe.cpp:371] Total Time: 76807 ms.
I0515 10:57:49.629648 22577 caffe.cpp:372] *** Benchmark ends ***

### 结论
从中可以看出，卷积过程是占用时间最长的时间，最后添加的隐层时间几乎可以忽略。也就是说如果选用更快的基础网络就可以获得更好的时间性能。但是，当前比较好的分类网络往往时间性能越差。就如下面采用VGG16的基础网络的测评结果。

## SSDH-VGG16-48 时间测评
I0515 11:06:09.363750 25325 caffe.cpp:322] *** Benchmark begins ***
I0515 11:06:09.363757 25325 caffe.cpp:323] Testing for 10 iterations.
I0515 11:06:38.296090 25325 caffe.cpp:351] Iteration: 1 forward-backward time: 28932 ms.
I0515 11:07:06.840222 25325 caffe.cpp:351] Iteration: 2 forward-backward time: 28539 ms.
I0515 11:07:35.316598 25325 caffe.cpp:351] Iteration: 3 forward-backward time: 28476 ms.
I0515 11:08:03.979251 25325 caffe.cpp:351] Iteration: 4 forward-backward time: 28662 ms.
I0515 11:08:32.425041 25325 caffe.cpp:351] Iteration: 5 forward-backward time: 28445 ms.
I0515 11:09:00.922821 25325 caffe.cpp:351] Iteration: 6 forward-backward time: 28497 ms.
I0515 11:09:29.456508 25325 caffe.cpp:351] Iteration: 7 forward-backward time: 28533 ms.
I0515 11:09:58.017192 25325 caffe.cpp:351] Iteration: 8 forward-backward time: 28560 ms.
I0515 11:10:26.747658 25325 caffe.cpp:351] Iteration: 9 forward-backward time: 28730 ms.
I0515 11:10:55.526351 25325 caffe.cpp:351] Iteration: 10 forward-backward time: 28778 ms.
I0515 11:10:55.526403 25325 caffe.cpp:354] Average time per layer: 
I0515 11:10:55.526415 25325 caffe.cpp:357]    conv1_1   forward: 126.859 ms.
I0515 11:10:55.526427 25325 caffe.cpp:360]    conv1_1   backward: 126.866 ms.
I0515 11:10:55.526438 25325 caffe.cpp:357]    relu1_1   forward: 32.3856 ms.
I0515 11:10:55.526502 25325 caffe.cpp:360]    relu1_1   backward: 0.0017 ms.
I0515 11:10:55.526513 25325 caffe.cpp:357]    conv1_2   forward: 2051.78 ms.
I0515 11:10:55.526522 25325 caffe.cpp:360]    conv1_2   backward: 1957.98 ms.
I0515 11:10:55.526531 25325 caffe.cpp:357]    relu1_2   forward: 31.9145 ms.
I0515 11:10:55.526549 25325 caffe.cpp:360]    relu1_2   backward: 0.001 ms.
I0515 11:10:55.526559 25325 caffe.cpp:357]      pool1   forward: 84.4491 ms.
I0515 11:10:55.526568 25325 caffe.cpp:360]      pool1   backward: 0.0017 ms.
I0515 11:10:55.526577 25325 caffe.cpp:357]    conv2_1   forward: 897.776 ms.
I0515 11:10:55.526587 25325 caffe.cpp:360]    conv2_1   backward: 872.623 ms.
I0515 11:10:55.526597 25325 caffe.cpp:357]    relu2_1   forward: 15.9782 ms.
I0515 11:10:55.526618 25325 caffe.cpp:360]    relu2_1   backward: 0.0017 ms.
I0515 11:10:55.526628 25325 caffe.cpp:357]    conv2_2   forward: 1789.78 ms.
I0515 11:10:55.526639 25325 caffe.cpp:360]    conv2_2   backward: 1731.79 ms.
I0515 11:10:55.526657 25325 caffe.cpp:357]    relu2_2   forward: 16.0203 ms.
I0515 11:10:55.526667 25325 caffe.cpp:360]    relu2_2   backward: 0.0029 ms.
I0515 11:10:55.526679 25325 caffe.cpp:357]      pool2   forward: 40.6898 ms.
I0515 11:10:55.526695 25325 caffe.cpp:360]      pool2   backward: 0.0015 ms.
I0515 11:10:55.526706 25325 caffe.cpp:357]    conv3_1   forward: 821.037 ms.
I0515 11:10:55.526718 25325 caffe.cpp:360]    conv3_1   backward: 819.12 ms.
I0515 11:10:55.526736 25325 caffe.cpp:357]    relu3_1   forward: 7.9143 ms.
I0515 11:10:55.526746 25325 caffe.cpp:360]    relu3_1   backward: 0.0031 ms.
I0515 11:10:55.526756 25325 caffe.cpp:357]    conv3_2   forward: 1654.11 ms.
I0515 11:10:55.526772 25325 caffe.cpp:360]    conv3_2   backward: 1634.94 ms.
I0515 11:10:55.526782 25325 caffe.cpp:357]    relu3_2   forward: 8.2196 ms.
I0515 11:10:55.526794 25325 caffe.cpp:360]    relu3_2   backward: 0.0016 ms.
I0515 11:10:55.526806 25325 caffe.cpp:357]    conv3_3   forward: 1645.52 ms.
I0515 11:10:55.526818 25325 caffe.cpp:360]    conv3_3   backward: 1618.82 ms.
I0515 11:10:55.526829 25325 caffe.cpp:357]    relu3_3   forward: 7.9277 ms.
I0515 11:10:55.526840 25325 caffe.cpp:360]    relu3_3   backward: 0.001 ms.
I0515 11:10:55.526851 25325 caffe.cpp:357]      pool3   forward: 20.8674 ms.
I0515 11:10:55.526865 25325 caffe.cpp:360]      pool3   backward: 0.0015 ms.
I0515 11:10:55.526875 25325 caffe.cpp:357]    conv4_1   forward: 783.157 ms.
I0515 11:10:55.526888 25325 caffe.cpp:360]    conv4_1   backward: 774.697 ms.
I0515 11:10:55.526899 25325 caffe.cpp:357]    relu4_1   forward: 3.9715 ms.
I0515 11:10:55.526911 25325 caffe.cpp:360]    relu4_1   backward: 0.0013 ms.
I0515 11:10:55.526922 25325 caffe.cpp:357]    conv4_2   forward: 1580.95 ms.
I0515 11:10:55.526934 25325 caffe.cpp:360]    conv4_2   backward: 1550.26 ms.
I0515 11:10:55.526945 25325 caffe.cpp:357]    relu4_2   forward: 3.9339 ms.
I0515 11:10:55.526957 25325 caffe.cpp:360]    relu4_2   backward: 0.0033 ms.
I0515 11:10:55.526968 25325 caffe.cpp:357]    conv4_3   forward: 1570.48 ms.
I0515 11:10:55.526980 25325 caffe.cpp:360]    conv4_3   backward: 1582.85 ms.
I0515 11:10:55.526993 25325 caffe.cpp:357]    relu4_3   forward: 3.9051 ms.
I0515 11:10:55.527004 25325 caffe.cpp:360]    relu4_3   backward: 0.001 ms.
I0515 11:10:55.527029 25325 caffe.cpp:357]      pool4   forward: 11.5586 ms.
I0515 11:10:55.527040 25325 caffe.cpp:360]      pool4   backward: 0.0014 ms.
I0515 11:10:55.527051 25325 caffe.cpp:357]    conv5_1   forward: 405.793 ms.
I0515 11:10:55.527063 25325 caffe.cpp:360]    conv5_1   backward: 388.631 ms.
I0515 11:10:55.527073 25325 caffe.cpp:357]    relu5_1   forward: 0.9914 ms.
I0515 11:10:55.527084 25325 caffe.cpp:360]    relu5_1   backward: 0.0014 ms.
I0515 11:10:55.527096 25325 caffe.cpp:357]    conv5_2   forward: 408.445 ms.
I0515 11:10:55.527148 25325 caffe.cpp:360]    conv5_2   backward: 388.297 ms.
I0515 11:10:55.527161 25325 caffe.cpp:357]    relu5_2   forward: 0.9862 ms.
I0515 11:10:55.527173 25325 caffe.cpp:360]    relu5_2   backward: 0.0016 ms.
I0515 11:10:55.527184 25325 caffe.cpp:357]    conv5_3   forward: 405.668 ms.
I0515 11:10:55.527194 25325 caffe.cpp:360]    conv5_3   backward: 389.269 ms.
I0515 11:10:55.527206 25325 caffe.cpp:357]    relu5_3   forward: 0.986 ms.
I0515 11:10:55.527221 25325 caffe.cpp:360]    relu5_3   backward: 0.0008 ms.
I0515 11:10:55.527235 25325 caffe.cpp:357]      pool5   forward: 3.7119 ms.
I0515 11:10:55.527246 25325 caffe.cpp:360]      pool5   backward: 0.0012 ms.
I0515 11:10:55.527256 25325 caffe.cpp:357]        fc6   forward: 162.774 ms.
I0515 11:10:55.527266 25325 caffe.cpp:360]        fc6   backward: 127.987 ms.
I0515 11:10:55.527276 25325 caffe.cpp:357]      relu6   forward: 0.042 ms.
I0515 11:10:55.527287 25325 caffe.cpp:360]      relu6   backward: 0.0009 ms.
I0515 11:10:55.527297 25325 caffe.cpp:357]      drop6   forward: 0.3486 ms.
I0515 11:10:55.527307 25325 caffe.cpp:360]      drop6   backward: 0.0016 ms.
I0515 11:10:55.527315 25325 caffe.cpp:357]        fc7   forward: 25.9295 ms.
I0515 11:10:55.527328 25325 caffe.cpp:360]        fc7   backward: 23.196 ms.
I0515 11:10:55.527339 25325 caffe.cpp:357]      relu7   forward: 0.0419 ms.
I0515 11:10:55.527351 25325 caffe.cpp:360]      relu7   backward: 0.0009 ms.
I0515 11:10:55.527361 25325 caffe.cpp:357]      drop7   forward: 0.346 ms.
I0515 11:10:55.527371 25325 caffe.cpp:360]      drop7   backward: 0.0007 ms.
I0515 11:10:55.527382 25325 caffe.cpp:357] latent_layer forward: 0.3628 ms.
I0515 11:10:55.527392 25325 caffe.cpp:360] latent_layer backward: 0.3135 ms.
I0515 11:10:55.527402 25325 caffe.cpp:357] encode_neuron    forward: 0.008 ms.
I0515 11:10:55.527412 25325 caffe.cpp:360] encode_neuron    backward: 0.0012 ms.
I0515 11:10:55.527431 25325 caffe.cpp:365] Average Forward pass: 14627.8 ms.
I0515 11:10:55.527439 25325 caffe.cpp:367] Average Backward pass: 13987.8 ms.
I0515 11:10:55.527447 25325 caffe.cpp:369] Average Forward-Backward: 28616.3 ms.
I0515 11:10:55.527456 25325 caffe.cpp:371] Total Time: 286163 ms.
I0515 11:10:55.527464 25325 caffe.cpp:372] *** Benchmark ends ***

### 结论
添加的额外层：0.3636ms
base network:
由此可见，基础网络是影响性能的关键因素。

## SSDH-VGG16-Avg-48
I0515 11:10:55.526403 25325 caffe.cpp:354] Average time per layer: 
I0515 11:10:55.526415 25325 caffe.cpp:357]    conv1_1   forward: 126.859 ms.
I0515 11:10:55.526427 25325 caffe.cpp:360]    conv1_1   backward: 126.866 ms.
I0515 11:10:55.526438 25325 caffe.cpp:357]    relu1_1   forward: 32.3856 ms.
I0515 11:10:55.526502 25325 caffe.cpp:360]    relu1_1   backward: 0.0017 ms.
I0515 11:10:55.526513 25325 caffe.cpp:357]    conv1_2   forward: 2051.78 ms.
I0515 11:10:55.526522 25325 caffe.cpp:360]    conv1_2   backward: 1957.98 ms.
I0515 11:10:55.526531 25325 caffe.cpp:357]    relu1_2   forward: 31.9145 ms.
I0515 11:10:55.526549 25325 caffe.cpp:360]    relu1_2   backward: 0.001 ms.
I0515 11:10:55.526559 25325 caffe.cpp:357]      pool1   forward: 84.4491 ms.
I0515 11:10:55.526568 25325 caffe.cpp:360]      pool1   backward: 0.0017 ms.
I0515 11:10:55.526577 25325 caffe.cpp:357]    conv2_1   forward: 897.776 ms.
I0515 11:10:55.526587 25325 caffe.cpp:360]    conv2_1   backward: 872.623 ms.
I0515 11:10:55.526597 25325 caffe.cpp:357]    relu2_1   forward: 15.9782 ms.
I0515 11:10:55.526618 25325 caffe.cpp:360]    relu2_1   backward: 0.0017 ms.
I0515 11:10:55.526628 25325 caffe.cpp:357]    conv2_2   forward: 1789.78 ms.
I0515 11:10:55.526639 25325 caffe.cpp:360]    conv2_2   backward: 1731.79 ms.
I0515 11:10:55.526657 25325 caffe.cpp:357]    relu2_2   forward: 16.0203 ms.
I0515 11:10:55.526667 25325 caffe.cpp:360]    relu2_2   backward: 0.0029 ms.
I0515 11:10:55.526679 25325 caffe.cpp:357]      pool2   forward: 40.6898 ms.
I0515 11:10:55.526695 25325 caffe.cpp:360]      pool2   backward: 0.0015 ms.
I0515 11:10:55.526706 25325 caffe.cpp:357]    conv3_1   forward: 821.037 ms.
I0515 11:10:55.526718 25325 caffe.cpp:360]    conv3_1   backward: 819.12 ms.
I0515 11:10:55.526736 25325 caffe.cpp:357]    relu3_1   forward: 7.9143 ms.
I0515 11:10:55.526746 25325 caffe.cpp:360]    relu3_1   backward: 0.0031 ms.
I0515 11:10:55.526756 25325 caffe.cpp:357]    conv3_2   forward: 1654.11 ms.
I0515 11:10:55.526772 25325 caffe.cpp:360]    conv3_2   backward: 1634.94 ms.
I0515 11:10:55.526782 25325 caffe.cpp:357]    relu3_2   forward: 8.2196 ms.
I0515 11:10:55.526794 25325 caffe.cpp:360]    relu3_2   backward: 0.0016 ms.
I0515 11:10:55.526806 25325 caffe.cpp:357]    conv3_3   forward: 1645.52 ms.
I0515 11:10:55.526818 25325 caffe.cpp:360]    conv3_3   backward: 1618.82 ms.
I0515 11:10:55.526829 25325 caffe.cpp:357]    relu3_3   forward: 7.9277 ms.
I0515 11:10:55.526840 25325 caffe.cpp:360]    relu3_3   backward: 0.001 ms.
I0515 11:10:55.526851 25325 caffe.cpp:357]      pool3   forward: 20.8674 ms.
I0515 11:10:55.526865 25325 caffe.cpp:360]      pool3   backward: 0.0015 ms.
I0515 11:10:55.526875 25325 caffe.cpp:357]    conv4_1   forward: 783.157 ms.
I0515 11:10:55.526888 25325 caffe.cpp:360]    conv4_1   backward: 774.697 ms.
I0515 11:10:55.526899 25325 caffe.cpp:357]    relu4_1   forward: 3.9715 ms.
I0515 11:10:55.526911 25325 caffe.cpp:360]    relu4_1   backward: 0.0013 ms.
I0515 11:10:55.526922 25325 caffe.cpp:357]    conv4_2   forward: 1580.95 ms.
I0515 11:10:55.526934 25325 caffe.cpp:360]    conv4_2   backward: 1550.26 ms.
I0515 11:10:55.526945 25325 caffe.cpp:357]    relu4_2   forward: 3.9339 ms.
I0515 11:10:55.526957 25325 caffe.cpp:360]    relu4_2   backward: 0.0033 ms.
I0515 11:10:55.526968 25325 caffe.cpp:357]    conv4_3   forward: 1570.48 ms.
I0515 11:10:55.526980 25325 caffe.cpp:360]    conv4_3   backward: 1582.85 ms.
I0515 11:10:55.526993 25325 caffe.cpp:357]    relu4_3   forward: 3.9051 ms.
I0515 11:10:55.527004 25325 caffe.cpp:360]    relu4_3   backward: 0.001 ms.
I0515 11:10:55.527029 25325 caffe.cpp:357]      pool4   forward: 11.5586 ms.
I0515 11:10:55.527040 25325 caffe.cpp:360]      pool4   backward: 0.0014 ms.
I0515 11:10:55.527051 25325 caffe.cpp:357]    conv5_1   forward: 405.793 ms.
I0515 11:10:55.527063 25325 caffe.cpp:360]    conv5_1   backward: 388.631 ms.
I0515 11:10:55.527073 25325 caffe.cpp:357]    relu5_1   forward: 0.9914 ms.
I0515 11:10:55.527084 25325 caffe.cpp:360]    relu5_1   backward: 0.0014 ms.
I0515 11:10:55.527096 25325 caffe.cpp:357]    conv5_2   forward: 408.445 ms.
I0515 11:10:55.527148 25325 caffe.cpp:360]    conv5_2   backward: 388.297 ms.
I0515 11:10:55.527161 25325 caffe.cpp:357]    relu5_2   forward: 0.9862 ms.
I0515 11:10:55.527173 25325 caffe.cpp:360]    relu5_2   backward: 0.0016 ms.
I0515 11:10:55.527184 25325 caffe.cpp:357]    conv5_3   forward: 405.668 ms.
I0515 11:10:55.527194 25325 caffe.cpp:360]    conv5_3   backward: 389.269 ms.
I0515 11:10:55.527206 25325 caffe.cpp:357]    relu5_3   forward: 0.986 ms.
I0515 11:10:55.527221 25325 caffe.cpp:360]    relu5_3   backward: 0.0008 ms.
I0515 11:10:55.527235 25325 caffe.cpp:357]      pool5   forward: 3.7119 ms.
I0515 11:10:55.527246 25325 caffe.cpp:360]      pool5   backward: 0.0012 ms.
I0515 11:10:55.527256 25325 caffe.cpp:357]        fc6   forward: 162.774 ms.
I0515 11:10:55.527266 25325 caffe.cpp:360]        fc6   backward: 127.987 ms.
I0515 11:10:55.527276 25325 caffe.cpp:357]      relu6   forward: 0.042 ms.
I0515 11:10:55.527287 25325 caffe.cpp:360]      relu6   backward: 0.0009 ms.
I0515 11:10:55.527297 25325 caffe.cpp:357]      drop6   forward: 0.3486 ms.
I0515 11:10:55.527307 25325 caffe.cpp:360]      drop6   backward: 0.0016 ms.
I0515 11:10:55.527315 25325 caffe.cpp:357]        fc7   forward: 25.9295 ms.
I0515 11:10:55.527328 25325 caffe.cpp:360]        fc7   backward: 23.196 ms.
I0515 11:10:55.527339 25325 caffe.cpp:357]      relu7   forward: 0.0419 ms.
I0515 11:10:55.527351 25325 caffe.cpp:360]      relu7   backward: 0.0009 ms.
I0515 11:10:55.527361 25325 caffe.cpp:357]      drop7   forward: 0.346 ms.
I0515 11:10:55.527371 25325 caffe.cpp:360]      drop7   backward: 0.0007 ms.
I0515 11:10:55.527382 25325 caffe.cpp:357] latent_layer forward: 0.3628 ms.
I0515 11:10:55.527392 25325 caffe.cpp:360] latent_layer backward: 0.3135 ms.
I0515 11:10:55.527402 25325 caffe.cpp:357] encode_neuron    forward: 0.008 ms.
I0515 11:10:55.527412 25325 caffe.cpp:360] encode_neuron    backward: 0.0012 ms.
I0515 11:10:55.527431 25325 caffe.cpp:365] Average Forward pass: 14627.8 ms.
I0515 11:10:55.527439 25325 caffe.cpp:367] Average Backward pass: 13987.8 ms.
I0515 11:10:55.527447 25325 caffe.cpp:369] Average Forward-Backward: 28616.3 ms.
I0515 11:10:55.527456 25325 caffe.cpp:371] Total Time: 286163 ms.
I0515 11:10:55.527464 25325 caffe.cpp:372] *** Benchmark ends ***


## 总结
神经网络中，卷积网络占用计算时间是最为长久的。而且卷积神经网络用的次数很多。此外，使用小规模的卷积核可以提升一定的速度。