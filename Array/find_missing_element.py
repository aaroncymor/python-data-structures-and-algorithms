def finder(arr1, arr2):
	for num in arr1:
		i = 0
		while i < len(arr2):
			if num == arr2[i]:
				del arr2[i]
				break;
			if i == len(arr2) - 1:
				return num
			i += 1
	return arr1, arr2

def finder_sol1(arr1,arr2):
	arr1.sort()
	arr2.sort()

	#zip will return a list of tupled of nth elements in each list
	#e.g., [1,2,3] [4,5,6] = [(1,4),(2,5),(3,6)]
	for num1, num2 in zip(arr1,arr2):
		if num1 != num2:
			return num1
		return arr1[-1]

import collections

def finder_sol2(arr1,arr2):
	d = collections.defaultdict(int)

	for num in arr2:
		d[num] += 1

	for num in arr1:
		if d[num] == 0:
			return num
		else:
			d[num] -=1


print finder([5,5,7,7],[5,7,7])
print finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
print finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])