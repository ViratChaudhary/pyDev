class Stack:
	def __init__(self):
		self.stack = []
		self.max_capacity = 5

	def push(self, elem):
		self.stack.append(elem)

	def pop(self):
		self.stack.pop()

	def isEmpty(self):
		if len(self.stack) < 1:
			return True
		else:
			return False

	def isFull(self):
		if self.stack >= self.max_capacity:
			return True
		else:
			return False

	def peekStack(self):
		return self.stack[-1]

	
