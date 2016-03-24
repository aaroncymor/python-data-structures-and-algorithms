def seq_search(arr,ele):
	"""
	Sequential search O(n)
	"""
	pos = 0 #position
	found = False

	while pos < len(arr) and not found:
		#print pos
		if arr[pos] == ele:
			found = True
		else:
			pos += 1
	return found

print seq_search([1,2,3,4,5],3)
print seq_search([1,2,3,4,5],2.2)