# -*- coding:UTF-8 -*-
import time
import sys

from xmltestcase import ExceutionType

sys.setdefaultencoding('utf8')
date = (long(time.time())/86400)*86400
custom_fields = {}

# Following is tester configure information
custom_fields['测试用例设计日期'] = str(date)
custom_fields['测试用例-检测参数'] = "功能"
EXCUTION_TYPE = ExceutionType.MANUAL
req_spec_title = "用户文档测试"
custom_fields['测试环境需求-测试用例'] = \
'''
测试机:兆芯C1  
硬件配置:
    型号：兆芯C 
    CPU：C-QuadCore C4600@2.0GHz 4核 
    内存：8192MB
	硬盘：200G     
软件配置:
    操作系统：cdos 1.10.0 - 0728 
    中间件：wine1.8.5
'''


# user ignore it
req_spec_title = "[%s]" % (req_spec_title,)