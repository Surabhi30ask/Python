#Write a Python program to construct the following patterns, using a nested for loop. using python in file handling
#Pattern-II 
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15 for i in range(1, 16):

for i in range(1, 16):
    for j in range(1,i+1):
        print(j, end=" ")
    print("\n")