def word_split(phrase,list_of_words, output = None):
    '''
    Note: This is a very "python-y" solution.
    ''' 
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output  

def word_split_not_recursion(phrase,list_of_words,output=None):
	phrase_length = len(phrase)
	to_sort = []
	copy_phrase = phrase
	for word in list_of_words:
		word_length = len(word)
		i = 0
		while i < phrase_length:
			if word_length <= phrase_length:
				if phrase[i:word_length] == word:
					copy_phrase = copy_phrase.replace(word,'')
					to_sort.append((i,word))
			word_length += 1
			i += 1
	if copy_phrase != '':
		return []
	return [word for i, word in sorted(to_sort)]

print word_split_not_recursion('themanran',['the','ran','man'])
print word_split_not_recursion('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
print word_split_not_recursion('themanran',['clown','ran','man'])