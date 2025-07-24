#write a program to sort three numbers using if-elif-else
x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
z=int(input("Enter the number:"))
if x>y and x>z:
    if y>z:
        print("The sorted no is:",x,y,z)
    else:
        print("The soretd no is:",x,z,y)
elif y>x and y>z:
    if x>z:
         print("The sorted no is:",y,x,z)
    else:
        print("The sorted no is:",y,z,x)
else:
    if y>x:
        print("The sorted no is:",z,y,x)
    else:
        print("The sorted no is:",z,x,y)