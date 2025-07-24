#swap two variables without using third variable
a=(int(input("Enter value of a:")))
b=(int(input("Enter value of b:")))
a=a+b
b=a-b
a=a-b
print("The value is:",a,b)