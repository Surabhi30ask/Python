#wrute a program to swap two numbers using bitwise operators
a=(int(input("Enter 1st number:")))
b=(int(input("Enter 2nd number:")))
a=a^b
b=a^b
a=a^b
print("After the swapping:")
print("The value of a:",a)
print("The value of b:",b)