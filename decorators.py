# def func(f):
# 	# Any number of postional or keyword arguments
# 	def wrapper(*args, **kwargs):
# 		print("Started")
# 		rv = f(*args, **kwargs)
# 		print("Ended")
# 		return rv
# 	return wrapper

# @func
# def func2(x, y):
# 	print(x)
# 	return y

# @func
# def func3():
# 	print("I am func3")

# x = func2(5, 6)
# print(x)

import time

def timer(func):
	def wrapper(*agrs, **kwargs):
		start = time.time()
		rv = func()
		total = time.time() - start
		print("Time: ", total)
		return rv

	return wrapper

@timer
def test():
	for _ in range(1000000):
		pass

@timer
def test2():
	time.sleep(2)

test2()
test()



