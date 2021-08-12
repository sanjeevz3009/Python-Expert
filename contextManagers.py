# class file:
# 	def __init__(self, filename, method):
# 		self.file = open(filename, method)

# 	def __enter__(self):
# 		print("Enter")
# 		return self.file

# 	def __exit__(self, type, value, traceback):
# 		print(f"{type}, {value}, {traceback}")
# 		print("Exit")
# 		self.file.close()
# 		if type == Exception:
# 			return True

# with file("file.txt", "w") as f:
# 	print("Middle")
# 	f.write("Hello!")


import contextlib
from contextlib import contextmanager

@contextmanager
def file(filename, method):
	print("Enter")
	file = open(filename, method)
	yield file
	file.close()
	print("Exit")

with file("text.txt", "w") as f:
	print("Middle")
	f.write("Hello!")