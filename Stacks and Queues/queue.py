class Queue(object):

	def __init__(self):
		self.__items = []

	def isEmpty(self):
		return self.__items == []

	def enqueue(self,item):
		self.__items.insert(0,item)

	def dequeue(self):
		return self.__items.pop()

	def size(self):
		return len(self.__items)

	def getQueue(self):
		return self.__items

if __name__ == '__main__':
	q = Queue()
	print q.isEmpty()
	q.enqueue(0)
	print "enqueue 0"
	print q.getQueue()
	q.enqueue(1)
	print "enqueue 1"
	print q.getQueue()
	q.enqueue(2)
	print "enqueue 2"
	print q.getQueue()

	print "dequeue"
	print q.dequeue()
	print "queue size"
	print q.size()