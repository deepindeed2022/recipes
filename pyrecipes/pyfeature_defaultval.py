from pprint import pprint

def f(x, L = []):
	for i in range(x):
		L.append(i*i)
	print L

f(2)
f(2, [1,2,3])
f(3)