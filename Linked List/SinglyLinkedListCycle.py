class Node(object):

	def __init__(self,value):
		self.value = value
		self.next_node = None

def cycle_check(node):
	#Node should not be pointing to itself.
	#if node.next_node != node and node.next_node != None:
	#	print node.value
	#	node = node.next_node
	#	print node.value
	body = [None]
	if node:
		first_node = node
		#If first node is not equal to itself and is not null
		if node.next_node != node:
			while True:
				node = node.next_node
				if node == first_node:
					return True
				elif node in body:
					return False
				body.append(node)

def cycle_check(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:
        
        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False


if __name__ == '__main__':
	"""
	RUN THIS CELL TO TEST YOUR SOLUTION
	"""
	from nose.tools import assert_equal

	# CREATE CYCLE LIST
	a = Node(1)
	b = Node(2)
	c = Node(3)

	a.next_node = b
	b.next_node = c
	c.next_node = a # Cycle Here!


	# CREATE NON CYCLE LIST
	x = Node(1)
	y = Node(2)
	z = Node(3)

	x.next_node = y
	y.next_node = z

	#############
	class TestCycleCheck(object):
	    
	    def test(self,sol):
	        assert_equal(sol(a),True)
	        assert_equal(sol(x),False)
	        
	        print "ALL TEST CASES PASSED"
	        
	# Run Tests

	t = TestCycleCheck()
	t.test(cycle_check)