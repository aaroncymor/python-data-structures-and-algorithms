class Queue2Stacks(object):

	def __init__(self):

		#Two Stacks
		self.stack1 = []
		self.stack2 = []

	def enqueue(self, element):
		if len(self.stack2) == 0:
			self.stack1.append(element)

	def dequeue(self):
		popped = 0
		l1 = len(self.stack1)
		if l1 >= 1:
			i = 0
			while i < l1 - 1:
				self.stack2.append(self.stack1.pop())
				i += 1

			popped = self.stack1.pop()

			l2 = len(self.stack2)
			j = 0
			while j < l2:
				self.stack1.append(self.stack2.pop())
				j += 1

		return popped, self.stack1

q = Queue2Stacks()

#for i in xrange(5):
#    q.enqueue(i)
    
#for i in xrange(5):
#    print q.dequeue()

q.enqueue(1)
q.enqueue(2)
print q.dequeue()
q.enqueue(3)
q.enqueue(4)
print q.dequeue()