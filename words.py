def words(phrase):
	"""counts instances of a word in a phrase"""
	wordlist = phrase.split()
	unique_wordlist = []
	word_freq = []

  
	while wordlist:
		word_freq.append(wordlist.count(wordlist[0])) #count the instances of a word and add it to the frequencies list
		unique_wordlist.append(wordlist[0])  #add the word into a unique words list
		wordlist = list(filter((wordlist[0]).__ne__, wordlist)) #remove all other similar words from the wordlist


	n = len(word_freq)
	output = {}

	for i in range(n):
		if unique_wordlist[i].isdigit(): #convert sting digits into int
			unique_wordlist[i] = int(unique_wordlist[i])
		output[unique_wordlist[i]] = word_freq[i]  #add the unique words with their corresponding frequencies into the output dict
	
	return output
