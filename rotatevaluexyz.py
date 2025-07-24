#write a program to rotate the value of x,y,z such that x has the value of y, y has the value of z and z has the value of x
x=(int(input("Enter value of x:")))
y=(int(input("Enter value of y:")))
z=(int(input("Enter value of z:")))
n=x
x=y
y=z
z=n
print("The valus are:",x,y,z)