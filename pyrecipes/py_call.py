class A(object):
	def __call__(self):
		print("invoking __call__ from A!")


class C(object):
	'''There is comment
	'''
	def __len__(self):
		return 5


def test_default_len():
	c = C()
	c.__len__ = lambda: 10
	print "the instance __dict__"
	print c.__dict__
	print len(c)

	print 
	print "the object __dict__"
	print type(c).__dict__
	print len(c)



def test_default_call():
	a = A()
	a()# output: invoking __call__ from A
	a.__call__ = lambda: "invoking __call__ from lambda"
	print a.__call__()
	a()
	b = A()
	b()


if __name__ == "__main__":
	
	test_default_call()

	test_default_len()