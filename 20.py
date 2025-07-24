#write a program to find the sum of the even-valued terms of the Fibonacci series up to 100
limit=100
sum=0
a=1
b=1
while b<limit:
    if b%2==0:
        sum+=b
        print(b)
    h=a+b
    a,b=b,h
print("The sum of all the even term is",sum)