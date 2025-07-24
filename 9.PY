#write a program to sort three numbers using if-elif-else
x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
z=int(input("Enter the number:"))
if x>y and x>z:
    if y>z:
        print("The sorted list:",x,y,z)
    else:
        print("The sorted list:",x,z,y)
elif y>z and y>x:
    if x>z:
        print("The sorted list:",y,x,z)
    else:
        print("The sorted list:",y,z,x)
else:
    if y>x:
        print("The sorted list:",z,y,x)
    else:
        print("The sorted list:",z,x,y)