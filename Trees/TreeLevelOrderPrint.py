class Node:
	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val

		def __str__(self):
			return self.val

def levelOrderPrint(tree):
	l = [tree]
	s = ""
	while True:
		nl = []
		i = 0
		while i < len(l):
			s += str(l[i].val) + " "
			if l[i].left != None:
				nl.append(l[i].left)
			if l[i].right != None:
				nl.append(l[i].right)
			i += 1
		if nl != []:
			l = nl
		else:
			break
		s += '\n'
	return s


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

b.left = d
c.left = e
c.right = f
a.left = b
a.right = c

print levelOrderPrint(a)
