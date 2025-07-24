#write a program to detect whether two strings are anagrams or not
str1=input("Enter string 1:")
str2=input("Enter string 2:")
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)
if((sorted_str1)==(sorted_str2)):
    print("The given string is anagrams")
else:
    print("The given string is not a anagrams")