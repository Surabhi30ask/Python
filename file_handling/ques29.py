#Write a function that takes a list and returns a new list with unique elements of the first list.  file handling using python
#using file handling
with open('myfile.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines] 
    unique_list = unique_list(lines)
    
print(unique_list)