#write a program to get all substrings of a given string
string=input("Enter a string:")
subs=[]
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        subs.append(string[i:j])
print(subs)