from nose.tools import assert_equal

def anagram(str1,str2): #My Solution
	d = {}
	a,b = ''.join(str1.lower().split(' ')),''.join(str2.lower().split(' '))

	for i in a:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1

	for j in b:
		if j in d:
			d[j] -= 1
		else:
			return False

	for k in d.keys():
		if d[k] > 0 or d[k] < 0:
			return False

	return True

def anagram_sol1(s1,s2): #Tutorial's solution1
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()

	return sorted(s1) == sorted(s2)

def anagram_sol2(s1,s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False
    
    # Create counting dictionary (Note could use DefaultDict from Collections module)
    count = {}
    
    
        
    # Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    # Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True

if __name__ == '__main__':
	class AnagramTest(object):
	    
	    def test(self,sol):
	        assert_equal(sol('go go go','gggooo'),True)
	        assert_equal(sol('abc','cba'),True)
	        assert_equal(sol('hi man','hi     man'),True)
	        assert_equal(sol('aabbcc','aabbc'),False)
	        assert_equal(sol('123','1 2'),False)
	        print "ALL TEST CASES PASSED"

	# Run Tests
	t = AnagramTest()
	t.test(anagram)