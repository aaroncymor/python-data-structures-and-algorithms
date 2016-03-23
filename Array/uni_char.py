def uni_char(s):
	l = []

	for c in s:
		if c not in l:
			l.append(c)
		else:
			return False
	return True

def uni_char_sol1(s):
	#If length of the set of the string is equal to
	#the length of the string. Means, all char is unique
	return len(set(s)) == len(s)

def uni_char_sol2(s):
	chars = set()

	for let in s:
		if let in chars:
			return False
		else:
			char.add(let)
	return True


if __name__ == '__main__':
	from nose.tools import assert_equal

	class TestUnique(object):

	    def test(self, sol):
	        assert_equal(sol(''), True)
	        assert_equal(sol('goo'), False)
	        assert_equal(sol('abcdefg'), True)
	        print 'ALL TEST CASES PASSED'
	        
	# Run Tests
	t = TestUnique()
	t.test(uni_char)