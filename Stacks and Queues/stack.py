class Stack(object):
	def __init__(self):
		self.__items = []

	def push(self,item):
		self.__items.append(item)

	def pop(self):
		return self.__items.pop()

	def peek(self):
		return self.__items[-1]

	def isEmpty(self):
		return self.__items == []

	def size(self):
		return len(self.__items)

	def getStack(self):
		return self.__items

if __name__ == '__main__':
	s = Stack()
	print "Pushing 0"
	s.push(0)
	print "Pushing 1"
	s.push(1)
	print "Pushing 2"
	s.push(2)
	print s.getStack()
	print "Pop 2"
	print s.pop()
	print "Peek stack"
	print s.peek()
	print "is empty?"
	print s.isEmpty()
	print "what size?"
	print s.size()