class Queue:
	def __init__(self):
		self.queue = [] 
		self.max_capacity = 5

	def enqueue(self, elem):
		self.queue.append(elem)

	def dequeue(self):
		if len(self.queue) == 0:
			return None
		else:
			self.queue.pop(0)

	def isEmpty(self):
		if len(self.queue) == 0:
			return True
		else:
			return False

	def isFull(self):
		if len(self.queue) >= self.max_capacity:
			return True
		else:
			return False

	def show_queue(self):
		return self.queue

	def peek(self):
		return self.queue[0]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.isEmpty())
print(q.isFull())
print(q.peek())
print(q.show_queue())
