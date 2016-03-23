class Node(object):

	def __init__(self,value):
		self.value = value
		self.next_node = None

def reverse(head):
	l = []
	while head != None:
		l.append(head)
		head = head.next_node
	i = len(l) - 1
	while i > 0:
		l[i].next_node = l[i - 1]
		i -= 1

	l[0].next_node = None

def reverse_sol1(head):
    #a,b,c,d

    # Set up current,previous, and next nodes
    current = head #a
    previous = None
    nextnode = None

    # until we have gone through to the end of the list
    while current: #a,b,c,d
        
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.next_node #b,c,d,None

        # Reverse the pointer ot the next_node
        current.next_node = previous #a.nextnode = None,b.nextnode=a,c.nextnode=b,d.nextnode=c

        # Go one forward in the list
        previous = current #a,b,c,d
        current = next_node #b,c,d,None

    return previous

if __name__ == '__main__':
	# Create a list of 4 nodes
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)

	# Set up order a,b,c,d with values 1,2,3,4
	a.next_node = b
	b.next_node = c
	c.next_node = d

	print a.next_node.value
	print b.next_node.value
	print c.next_node.value
	#print d.next_node.value

	reverse(a)
	print d.next_node.value
	print c.next_node.value
	print b.next_node.value
	#print a.next_node.value