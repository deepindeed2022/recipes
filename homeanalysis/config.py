#!/usr/bin/python
#-*-coding:utf-8-*-
cites = [
('北京','http://bj.fang.lianjia.com/loupan/pg%snht1nhs3/',8),
('上海','http://sh.fang.lianjia.com/loupan/pg%s/',32),
('深圳','http://sz.fang.lianjia.com/loupan/pg%s/',50),
('西安','http://xa.fang.lianjia.com/loupan/pg%s/',40),
('长沙','http://cs.fang.lianjia.com/loupan/pg%s', 21),
('南京','http://nj.fang.lianjia.com/loupan/pg%s/',10),
('广州','http://gz.fang.lianjia.com/loupan/pg%s/',34),
('厦门','http://xm.fang.lianjia.com/loupan/pg%s/',5),
('重庆','http://cq.fang.lianjia.com/loupan/pg%s/',20),
('苏州','http://su.fang.lianjia.com/loupan/pg%s/',-1),
('大连','https://dl.lianjia.com/loupan/pg%s/',17),
('青岛','https://qd.lianjia.com/loupan/pg%s/',8)
]


ershoufang = [
('北京','http://bj.fang.lianjia.com/ershoufang/pg%snht1nhs3/',8),
('上海','http://sh.fang.lianjia.com/ershoufang/pg%s/',32),
('深圳','http://sz.fang.lianjia.com/ershoufang/pg%s/',50),
('西安','http://xa.fang.lianjia.com/ershoufang/pg%s/',40),
('长沙','http://cs.fang.lianjia.com/ershoufang/pg%s', 21),
('南京','http://nj.fang.lianjia.com/ershoufang/pg%s/',10),
('广州','http://gz.fang.lianjia.com/ershoufang/pg%s/',34),
('厦门','https://xm.lianjia.com/ershoufang/pg%s/',100),
('重庆','',),
('苏州','',),
('苏州','',),
('大连','',),
('青岛','',)
]

#!/usr/bin/python
import time
import random
print "Start : %s" % time.ctime()
time.sleep(random.random()*120)
print "End : %s" % time.ctime()