def reverse(s):
	if len(s) == 1:
		return s
	l = list(s)
	del l[-1]
	return s[-1] + reverse(''.join(l))

def reverse_sol1(s):
    
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]

if __name__ == '__main__':
	'''
	RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
	'''

	from nose.tools import assert_equal

	class TestReverse(object):
	    
	    def test_rev(self,solution):
	        assert_equal(solution('hello'),'olleh')
	        assert_equal(solution('hello world'),'dlrow olleh')
	        assert_equal(solution('123456789'),'987654321')
	        
	        print 'PASSED ALL TEST CASES!'
	        
	# Run Tests
	test = TestReverse()
	test.test_rev(reverse)