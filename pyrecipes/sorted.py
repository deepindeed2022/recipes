#!/usr/bin/python 
# -*- coding: utf-8 -*- 
"""
本页中主要针对各种排序算法进行实现和性能对比
"""

import random
import time
# using timeit to as Timer
'''
时间复杂度为O(NlogN),空间复杂度为O(logN)
'''


def quick_sort(A):
	if len(A) == 0 or A == None: return []
	else: return quick_sort([ i for i in A[1:] if i < A[0]]) + [A[0]] + quick_sort([i for i in A[1:] if i >= A[0]])

'''
时间复杂度为O(n^2),空间复杂度为O(1)
'''

def insert_sort(A):
	l = len(A)
	if l <= 1: return A
	for i in range(1, l):
		for j in range(i , 0, -1):
			if A[j] < A[j-1]: A[j], A[j-1] =  A[j-1], A[j]
	return A

def merge_sort(A):
	def merge(A, B):
		n = len(A)
		m = len(B)
		i = 0
		j = 0
		k = 0
		C = [0 for _ in xrange(n+m)]
		while i < n and j < m:
			if A[i] <= B[j]:
				C[k] = A[i]
				k += 1
				i += 1
			else:
				C[k] = B[j]
				k += 1
				j += 1
		if i < n:
			C[k:] = A[i:]
		else:
			C[k:] = B[j:]
		return C

	n = len(A)
	if n == 1: return A
	if n == 2:
		if A[0] > A[1]:
			A[0], A[1] = A[1], A[0]
		return A
	else:
		B = merge_sort(A[:n/2])
		C = merge_sort(A[n/2:])
	return merge(B, C)

def test_perf():
	_max_val = 100
	random.seed(1)
	x = [random.randint(0, _max_val) for __ in range(10**4)] 
	qsort(x[:])
	insert_sort(x[:])

def test_quick_sort():
	_max_val = 10000
	random.seed(1)
	x = [random.randint(0, _max_val) for __ in range(10**4)]
	start = time.clock()
 	for _ in range(1): x = quick_sort(x)
 	end = time.clock()
 	print "%s cost %s second"%(quick_sort.__name__, end - start)

 	start = time.clock()
 	random.shuffle(x)
 	for _ in range(1): x = quick_sort(x)
 	end = time.clock()
 	print "%s cost %s second"%(quick_sort.__name__, end - start)
	#qsort(x[::-1])
def test_merge_sort():
	_max_val = 10000
	random.seed(1)
	x = [random.randint(0, _max_val) for __ in range(10)]
	start = time.clock()
 	#print x
 	for _ in range(1): B = merge_sort(x)
 	print B
 	end = time.clock()
 	print "%s cost %s second"%(merge_sort.__name__, end - start)

if __name__ == '__main__':
	#test_perf()
	test_quick_sort()
	test_merge_sort()
	# A = [i for i in range(3)]
	# B = [0 for _ in range(4)]
	# B[1:] = A[1:]
	# print B
