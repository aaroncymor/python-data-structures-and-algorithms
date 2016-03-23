class Node:
	
	def __init__(self,value):
		self.value = value
		self.next_node = None

if __name__ == '__main__':
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)

	a.next_node = b
	b.next_node = c
	c.next_node = d
	d.next_node = e

	print b.next_node.value