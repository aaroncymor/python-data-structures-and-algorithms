def binary_search(arr,ele):
	first = 0
	last = len(arr) - 1
	found = False

	while first <= last and not found:

		mid = (first+last)/2

		if arr[mid] == ele:
			found = True
		else:
			if ele < arr[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found

"""
#First Step
first = 0
last = 9

mid = (0 + 9) / 2 => 4
	arr[4] or 5 == 9 ? False

	if 9 < 5: False else: first = mid (4)  + 1 or 5

#Second Step
first = 5
last = 9

mid = (5 + 9) / 2 = 14 / 2 = 7
	arr[7] or 8 == 9 ? False

	if 9 < arr[7] or 8 : False else: first = mid (7) + 1

#Third Step
first = 8
last = 9

mid = (8 + 9) 17 / 2
mid = 8
	arr[8] or 9 == 9 ? True

9 is found!

Conclusion: It only took 3 steps for binary search O(log n)
instead of 8 steps for sequential search O(n) or O(8)
"""
print binary_search([1,2,3,4,5,6,7,8,9,10],9)

"""
#First Step:
first = 0
last = len(arr) - 1 or 9

mid = (0 + 9) / 2 = 9 / 2 = 4

	arr[4] or 5 == 1 ? : False

	if 1 < 5 : True then last = mid (4) - 1

#Second Step:
first = 0
last = 3

mid = (0 + 3) / 2 = 1

	arr[1] or 2 == 1 ? False

	if 1 < 2: True then last = mid (1) - 1 or 0

#Third Step:
first = 0
last = 0

mid = (0 + 0) / 2 = 0

	arr[0] or 1 == 1 ? True

1 is found! took only three steps vs O(1) for sequential
"""
print binary_search([1,2,3,4,5,6,7,8,9,10],1)

"""
#First Step

first = 0
last = len(arr) - 1 or 2

mid = (0 + 2) / 2 or 1
	
	arr[1] or 2 == -1 : False

	if -1 < arr[1] or 2: True: then last = mid (1) -1 or 0

#Second Step
first = 0
last = 0

mid = (0 + 0) / 2 or 0

	arr[0] or 1 == -1: False

	if -1 < arr[0] or 1: True then last = mid (0) - 1 or -1

#Third Step
first = 0
last = -1
End while loop since conditions where not met:
(while first <= last: or 0 <= -1)

return False

Took 3 steps for binary search compared to O(3) for sequential
same as O(3) for sequential
"""
print binary_search([1,2,3],-1)