#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import os.path
import logging


def root_dir():
    root_dir = os.path.split(os.path.realpath(__file__))[0]
    return root_dir


def get_logger(name):
    def local_date():
        return str(time.strftime("%Y-%m-%d", time.localtime()))
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(root_dir(), 'log', '%s-%s.log' % (name, local_date())),
                    filemode='a+')
    logger = logging.getLogger(name)
    return logger

def elapsetime(func):
    '''wapper for elapse time for function
    '''
    def wapper(*args, **kwargs):
        start = time.time()
        result  = func(*args, **kwargs)
        end = time.time()
        print("execute %s used time:%.2f s" % (func.__name__, (end - start)))
        return result
    return wapper


def elapsetime(ostream=sys.stdout):
    '''wapper for elapse time for function'''
    def decorator(func):
        def wapper(*args, **kwargs):
            start = time.time()
            result  = func(*args, **kwargs)
            end = time.time()
            print >> ostream, "execute %s used time:%.2f s" % (func.__name__, (end - start))
            return result
        return wapper
    return decorator

a = open('log.txt', 'a+')
@elapsetime(a)
def test():
    print "hello"

if __name__ == '__main__':
    test()
