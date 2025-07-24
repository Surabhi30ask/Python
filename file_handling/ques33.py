# Program to count the number of lines in a text file

# Open the text file in read mode 
text_file = open("sample.txt", "r") 

# Initialize the count 
count = 0

# Iterate over each line 
for line in text_file: 
	# Increment the count 
	count += 1

# Print the number of lines 
print("Number of lines in the file:", count) 

# Close the file 
text_file.close()