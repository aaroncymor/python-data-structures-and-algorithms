def sum_func(n):
	if n == 0:
		return 0
	return n % 10 + sum_func(n / 10)

	#4321 % 10 + sum_func(4321 / 10)	> 1 + 9 return 10
	#432 % 10 + sum_func(432/10)		> 2 + 7 return 9
	#43 % 10 + sum_func(43/10)			> 3 + 4 return 7
	#4 % 10 + sum_func(4 /10) 			> 4 + 0 return 4

print sum_func(54321)