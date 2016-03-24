def binary_search_rec(arr,ele):
	#Base Case
	if len(arr) == 0:
		return False

	else:
		mid = len(arr) / 2

		if arr[mid] == ele:
			return True
		else:
			if ele < arr[mid]:
				binary_search_rec([:mid],ele)
			else:
				binary_search_rec([mid+1:],ele)

"""
#First Step
if len(arr) or 10 == 0: False
Then
	mid = len(arr) or 10 / 2 = 5

		arr[5] or 6 == 9: False

		if 9 < arr[5] or 6: False then binary_search_rec([mid (5) + 1:], 9)
		or binary_search_rec([7,8,9,10],9)

#Second Step
arr = [7,8,9,10]

if len(arr) or 4 == 0: False
Then
	mid = len(arr) or 4 / 2 = 2
		arr[2] or 9 == 9 ? True

9 was found! return True
compared to Binary search iterative, it only took 2 steps
to find 9!
"""

print binary_search_rec([1,2,3,4,5,6,7,8,9,10],9)

"""
#First Step
arr = [1,2,3,4,5,6,7,8,9,10]

if len(arr) or 10 == 0: False
Then
	mid = len(arr) or 10 / 2 = 5
		arr[5] or 6 == 1 ? False
		Then
		if 1 < arr[5] or 6 ? True Then binary_search_rec([:mid],1)
		or binary_search_rec([1,2,3,4,5],1)

#Second Step
arr = [1,2,3,4,5]

if len(arr) or 5 == 0: False
Then
	mid = len(arr) or 5 / 2 = 2
		arr[2] or 3 == 5: False
		Then
		if 1 < arr[2] or 3: True Then binary_search_rec[:mid],1)
		or binary_search_rec([1,2],1)

#Third Step
arr = [1,2]

if len(arr) or 2 == 0: False
Then
	mid = len(arr) or 2 / 2 = 1
	if arr[1] or 2 == 1: False
	Then
	if 1 < arr[1] or 2: True Then binary_search_rec([:mid],1)
	or binary_search_rec([1],1)

#Fourth Step
arr = [1]

if len(arr) or 1 == 0: False
Then
	mid = len(arr) or 1 / 2 = 0
	if arr[0] or 1 == 1 : True

1 was found! return True
It took 4 steps to find 1, compared to sequential search
O(1) best case scenario!
"""
print binary_search_rec([1,2,3,4,5,6,7,8,9,10],1)
