#!/usr/bin/python
#-*-encoding=utf-8 -*-

"""
从测试结果中获取训练时间和测试准确率等信息
@author: caowenlong
@create: 2018-07-03
"""

import os
import os.path

# 获取路径下的所有文件的路径列表
def get_subfiles(srcdir = None):
    filelist= []
    def process_dir(arg, dirname, names):
        for name in names:
            name_path = "{}{}{}".format(dirname, os.sep, name)

            if os.path.islink(name_path):
                os.path.walk(name_path, process_dir, arg)
            elif os.path.isfile(name_path):
                filelist.append(os.path.abspath(name_path))
    if srcdir == None:
        return []
    if isinstance(srcdir, str):
        os.path.walk(srcdir, process_dir, "")
        return filelist
    elif isinstance(srcdir, list):
        for sdir in srcdir:
            os.path.walk(sdir, process_dir, "")
        return filelist


def main():
    datasets = ["web", "adult","3_group", "5_group"]
    for ds in datasets:
        print "--"*30
        print "-- datasets {} result ".format(ds)
        print "--"*30
        ds_files = get_subfiles(ds)
        times = []
        accus = []
        for p in ds_files:
            if p.endswith(".time"):
                times.append(p)
            elif p.endswith(".accu"):
                accus.append(p)
        # ACCU  2018-07-03 00:09:31,002 INFO [default] Accuracy = 0.978778
        # TIME  train() time is 915.000000
        # 准确率和时间结果都是存在的情况
        if len(accus) == len(times):
            exp_len = len(accus)
            for i in xrange(exp_len):
                path_len = len(times[i].strip()) - 5
                assert times[i][:path_len] == accus[i][:path_len]
                print times[i][:path_len]
                # print open(times[i]).readlines()[-4].strip()
                # print open(accus[i]).readlines()[-1].strip()
                print open(times[i]).readlines()[-4].strip()[16:], open(accus[i]).readlines()[-1].strip()[50:]
        else:#缺少准确率或者train时间的情况
            exp_len = len(times)
            for i in xrange(exp_len):
                path_len = len(times[i].strip()) - 5
                print times[i][:path_len]
                print open(times[i]).readlines()[-4].strip()
            exp_len = len(accus)
            for i in xrange(exp_len):
                path_len = len(accus[i].strip()) - 5
                print accus[i][:path_len]
                print open(accus[i]).readlines()[-1].strip()
           
            # print open(times[i]).readlines()[-4].strip()[16:],
            # print open(accus[i]).readlines()[-1].strip()[50:]

if __name__ == '__main__':
    main()
