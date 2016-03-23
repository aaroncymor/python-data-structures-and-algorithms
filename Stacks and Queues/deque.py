class Deque(object):

	def __init__(self):
		self.__items = []

	def getDeque(self):
		return self.__items

	def addFront(self,item):
		self.__items.append(item)
		return self.getDeque()

	def addRear(self, item):
		self.__items.insert(0,item)
		return self.getDeque()

	def removeFront(self):
		return self.__items.pop()

	def removeRear(self):
		return self.__items.pop(0)

	def size(self):
		return len(self.__items)

	def isEmpty(self):
		return self.__items == []

if __name__ == '__main__':
	d = Deque()
	print d.isEmpty()
	print d.addFront(1)
	print d.addFront(2)
	print d.addFront(3)
	print d.addRear(4)
	print d.addRear(5)

	print d.removeFront()
	print d.removeRear()

	print d.size()
	print d.isEmpty()