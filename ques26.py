# Program to convert a list of tuples into a dictionary 

# initializing list 
test_list = [("A", 1), ("B", 2), ("C", 3), ("D", 4)] 
  
# printing original list 
print("The original list is : " + str(test_list)) 

# using dict comprehension 
# to convert list to dictionary 
res = {sub[0] : sub[1] for sub in test_list} 
  
# printing result 
print("The converted Dictionary is : " +  str(res))