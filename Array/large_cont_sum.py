def large_cont_sum(arr):
	max_sum,max_rev_sum = 0,0
	curr_sum,rev_sum = 0,0
	i,j = 0, len(arr) - 1
	while i < len(arr) and j >= 0:
		curr_sum += arr[i]
		rev_sum += arr[j]

		if max_sum < curr_sum:
			max_sum = curr_sum
		if max_rev_sum < rev_sum:
			max_rev_sum = rev_sum

		i += 1
		j -= 1

	if max_sum < max_rev_sum:
		max_sum = max_rev_sum

	return max_sum

if __name__ == '__main__':
	from nose.tools import assert_equal

	class LargeContTest(object):
	    def test(self,sol):
	        assert_equal(sol([1,2,-1,3,4,-1]),9)
	        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
	        assert_equal(sol([-1,1]),1)
	        print 'ALL TEST CASES PASSED'
	        
	#Run Test
	t = LargeContTest()
	t.test(large_cont_sum)