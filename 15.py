#write a program to check whether a given number is a prime number or not
number=int(input("Enter any number:"))
if number>1:
    for i in range(2,number):
        if(number%i)==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:
    print(number,"is not a prime number")