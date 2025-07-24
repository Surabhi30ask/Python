s1=input("Enter string:")
x=len(s1)
l=x-1
char=s1[x-1]
s1=s1.replace(char,'*')
s2=s1[0:l]+char
print(s2)