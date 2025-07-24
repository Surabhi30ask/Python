#write a program to get a string from a given string where all occurences of the last character have been changed to '*' , except the last character
str=input("Enter a string:")
print(str[:-1].replace(str[len(str)-1], "*",)+str[len(str)-1])