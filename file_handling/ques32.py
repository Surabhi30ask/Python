#Write a program to find the longest word of a text file. using file handing in python

#The program to find the longest word of a text file
 
#open and read the file
f = open("textfile.txt", "r")
text = f.read() 
#split the text into words
words = text.split() 
#find the longest word
longest_word = ''
for word in words:
  if len(word) > len(longest_word):
    longest_word = word
#print the longest word
print("The longest word in the text file is:", longest_word)