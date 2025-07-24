#write a program to rotate the value of x,y,z such that x has the value of y,y has the value of z and z has the value of x
x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
z=int(input("Enter the number:"))
x,y,z=y,z,x
print("The value of x:",x)
print("The value of y:",y)
print("The value of z:",z)