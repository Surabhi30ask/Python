#Write a program to read a file line by line and store it into a list. 
# open the file in reading mode 


# create an empty list 
lines = []

# iterate over each line of the file 
for line in f:
  # remove the newline character from the end of the line
  line = line.strip()
  # append the line to the list 
  lines.append(line)

# close the file 
f.close()

# print the content of the list 
print(lines)
