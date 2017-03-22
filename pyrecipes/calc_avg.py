#!/usr/bin/env python2.7

GROUP_NUM = 6
groupnum = [0 for i in range(GROUP_NUM)]
result = []
with open("data.txt", "r") as f:
    lines = f.readlines()
    linenum = 1

    for l in lines:
        groupnum[linenum % 6] = float(l.strip())
        if linenum % 6 is 0:
            avg = sum(groupnum)/GROUP_NUM
            result.append(avg)
        linenum += 1
    print result