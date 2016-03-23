class Node(object):

	def __init__(self,value):
		self.value = value
		self.nextnode = None

def nth_to_last_node(n, head):
	l = []
	while head != None:
		l.append(head)
		head = head.nextnode
	return l[-n]

if __name__ == '__main__':
	"""
	RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

	PLEASE NOTE THIS IS JUST ONE CASE
	"""

	from nose.tools import assert_equal

	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)

	a.nextnode = b
	b.nextnode = c
	c.nextnode = d
	d.nextnode = e

	####

	class TestNLast(object):
	    
	    def test(self,sol):
	        
	        assert_equal(sol(2,a),d)
	        print 'ALL TEST CASES PASSED'
	        
	# Run tests
	t = TestNLast()
	t.test(nth_to_last_node)