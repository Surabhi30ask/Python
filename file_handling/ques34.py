# Python program to count 
# frequency of words in a file 
def word_count(fname): 
	with open(fname) as f: 
		if f.mode == 'r': 
			contents =f.read() 
	
	# split() divides the string into 
	# words and returns them in a 
	# list of words 
	words = contents.split() 
	
	for word in words: 
		# remove punctuations 
		word = word.replace(",", "") 
		word = word.replace(".", "") 
	
	# give the frequency of each word 
	for i in words: 
		freq = words.count(i) 
		print(i, freq) 

# Driver Code 
if __name__ == "__main__": 
	fname = "test.txt"
	word_count(fname)