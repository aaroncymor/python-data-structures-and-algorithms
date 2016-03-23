def compress(s):
	"""
	1st step: get all unique characters.
	e.g., AABBCCDDaabbccdd = ABCDabcd AABBAA = ABA
	"""
	unique = ""
	temp = ""
	for i in range(len(s)):
		if i == 0:
			unique += s[i]
			temp = s[i]

		if temp == s[i]:
			pass
		else:
			unique += s[i]
			temp = s[i]
	"""
	2nd step: for each unique letter check it in the given string for compression.
	if unique letter is equal to the char of given string, count +=1
	else, break the loop and change given string to s[count:].

	e.g., unique =ABC given = AAABBBCC
		first unique char is 'A' and will loop through AAABBBCC
		while 'A' = given s[index] count +=1
		when 'A' hits 'B' which are not equal at count 3,
		given s will become [count:] which means it will turn to BBBCC
		and break the loop so that unique will shift to 'B'
		index starts at zero again checking BBBCC instead of AAABBBCC
	"""
	comp = ""
	for c in unique:
		i,count = 0,0

		while i < len(s):
			if c == s[i]:
				count += 1
			else:
				s = s[count:]
				break
			i += 1
		comp += c + str(count)
	return comp

def compress_sol1(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    
    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # Check for length 0
    if l == 0:
        return ""
    
    # Check for length 1
    if l == 1:
        return s + "1"
    
    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1
            
        # Add to index count to terminate while loop
        i += 1
    
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)
    
    return r
if __name__ == '__main__':
	from nose.tools import assert_equal

	class TestCompress(object):

	    def test(self, sol):
	        assert_equal(sol(''), '')
	        assert_equal(sol('AABBCC'), 'A2B2C2')
	        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
	        print 'ALL TEST CASES PASSED'

	# Run Tests
	t = TestCompress()
	t.test(compress)