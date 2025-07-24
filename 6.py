#write a progrm to display the following numbers : 5678,678,78,8, where the given numbers is 5678
x=int(input("Enter the number:"))
y=x%1000
z=y%100
a=z%10
print("The value of x:",x,y,z,a)