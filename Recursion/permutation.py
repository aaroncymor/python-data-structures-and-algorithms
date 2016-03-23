def permutationsOf(s):
	result = []
	if len(s) == 1:
		return [s]
	else:
		first = s[0]
		rest = s[1:]
		simpler = permutationsOf(rest)
		print simpler

		for permutation in simpler:
			result = insertToAllPositions(first,permutation)
			#result.append(addition)
	return result


def insertToAllPositions(c,s):
	result = []
	for i in range(len(s) + 1):
		insert = s[:i] + c + s[i:]
		result.append(insert)
	return result

#print permutationsOf('abc')


def permute(s):
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):
            print permute(s[:i] + s[i+1:])
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                
                # Add it to output
                out += [let + perm]

    return out

permute('abc')