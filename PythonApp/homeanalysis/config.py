#!/usr/bin/python
#-*-coding:utf-8-*-
cites = [
(u'北京','http://bj.fang.lianjia.com/loupan/pg%snht1nhs3/',8),
(u'上海','http://sh.fang.lianjia.com/loupan/pg%s/',32),
(u'深圳','http://sz.fang.lianjia.com/loupan/pg%s/',50),
(u'西安','http://xa.fang.lianjia.com/loupan/pg%s/',40),
(u'长沙','http://cs.fang.lianjia.com/loupan/pg%s', 21),
(u'南京','http://nj.fang.lianjia.com/loupan/pg%s/',10),
(u'广州','http://gz.fang.lianjia.com/loupan/pg%s/',34),
(u'厦门','http://xm.fang.lianjia.com/loupan/pg%s/',5),
(u'重庆','http://cq.fang.lianjia.com/loupan/pg%s/',20),
(u'苏州','http://su.fang.lianjia.com/loupan/pg%s/',-1),
(u'大连','https://dl.lianjia.com/loupan/pg%s/',17),
(u'青岛','https://qd.lianjia.com/loupan/pg%s/',8)
]
## 像中文，在windows下输出全是乱码的情况，可以在中文的前面加上小u进行标示，标示属于utf-8的字符串

ershoufang = [
(u'北京','http://bj.fang.lianjia.com/ershoufang/pg%snht1nhs3/',8),
(u'上海','http://sh.fang.lianjia.com/ershoufang/pg%s/',32),
(u'深圳','http://sz.fang.lianjia.com/ershoufang/pg%s/',50),
(u'西安','http://xa.fang.lianjia.com/ershoufang/pg%s/',40),
(u'长沙','http://cs.fang.lianjia.com/ershoufang/pg%s', 21),
(u'南京','http://nj.fang.lianjia.com/ershoufang/pg%s/',10),
(u'广州','http://gz.fang.lianjia.com/ershoufang/pg%s/',34),
(u'厦门','https://xm.lianjia.com/ershoufang/pg%s/',100),
(u'重庆','http://cq.fang.lianjia.com/ershoufang/pg%s/',20),
(u'苏州','http://su.fang.lianjia.com/ershoufang/pg%s/',-1),
(u'大连','https://dl.lianjia.com/ershoufang/pg%s/',17),
(u'青岛','https://qd.lianjia.com/ershoufang/pg%s/',8)
]

# #!/usr/bin/python
# import time
# import random
# print "Start : %s" % time.ctime()
# time.sleep(random.random()*120)
# print "End : %s" % time.ctime()