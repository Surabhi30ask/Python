#write a program to find the sum of all the prime numbers within a given range
lower=int(input("Enter 1st number:"))
upper=int(input("Enter 2nd number:"))
sum=0
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
            sum+=num
print("The sum of all prime number is",sum)