s=input("Enter string:")
x=len(s)
for i in range (x):
    for j in range (i,x):
        print(s[i:j+1])