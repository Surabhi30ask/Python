#write a program to read a string and check whether the string is a palindrone or not
string=input("Enter the string to be check:")
string=string.casefold()
reverse_string=reversed(string)
if list(string)==list(reverse_string):
    print("The string is a palindrone")
else:
    print("The string is not a palindrone")