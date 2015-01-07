class Stack(object):
	def __init__(self):
		self.stack = {}
		self.index =0
		pass

	def push(self, item):
		self.stack[self.index]=0
		self.index++
		pass

	def pop(self):
		self.index--
		top= self.stack[self.index]
		del self.stack[self.index]
		return top_element
		pass

	def size(self):
		return self.index 
		pass

s= Stack()
print s.dict
s.push(3)
s.push(5)
print s.dict