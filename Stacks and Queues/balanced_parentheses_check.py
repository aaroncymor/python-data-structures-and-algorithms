def balance_check(s):
	parentheses = {'[':']','(':')','{':'}','<':'>'}
	l = []
	for c in s:
		if c in parentheses.keys():
			l.append(c)
		else:
			try:
				for key, value in parentheses.items():
					if value == c:
						l.remove(key)
			except ValueError:
				return False
	return l == []

def balance_check_sol1(s):
    #Edge case. Check if even number of parentheses
    if len(s)%2 != 0:
        return False
    
    #Create a set of opening brackets
    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])
    
    stack = []
    
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            
            last_open = stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack) == 0

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print 'ALL TEST CASES PASSED'
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)