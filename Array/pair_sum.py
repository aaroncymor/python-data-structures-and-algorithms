def pair_sum(numbers,n):
	count = 0
	i = 0
	reset = False
	while i < len(numbers):
		j = 0
		while j < len(numbers):
			if j == i:
				pass
			else:
				if (numbers[j] + numbers[i]) == n:
					del numbers[j]
					del numbers[i]
					count +=1
					reset = True
					break
			j += 1
		if reset:
			i = 0
			reset = False
		else:
			i += 1
	return count

def pair_sum_sol1(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output),output, seen
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))

if __name__ == '__main__':

	print pair_sum_sol1([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
	print pair_sum_sol1([1,2,3,1],3)
	print pair_sum_sol1([1,3,2,2],4)

	from nose.tools import assert_equal

	class TestPair(object):
	    
	    def test(self,sol):
	        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
	        assert_equal(sol([1,2,3,1],3),1)
	        assert_equal(sol([1,3,2,2],4),2)
	        print 'ALL TEST CASES PASSED'
	        
	#Run tests
	t = TestPair()
	t.test(pair_sum)