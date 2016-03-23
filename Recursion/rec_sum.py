def rec_sum(n):
	if n == 0:
		return 0
	return n + rec_sum(n - 1)

	#4 + rec_sum(3) > 4 + 6 return 10
	#3 + rec_sum(2) > 3 + 3 return 6
	#2 + rec_sum(1) > 2 + 1 return 3
	#1 + rec_sum(0) > 1 + 0 return 1

print rec_sum(4)