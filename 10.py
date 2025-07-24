#write a program to calculate simple interest with the following conditions.
#if the principal amount is less than 2,00,000 the interest rate is 10%
#if the principal amount is 2,00,000 - 10,00,000 the interest rate is 12%
#if the principal amount is greater than 10,00,000 the interest rate is 15%
p=int(input("Enter principal amount:"))
t=int(input("Enter time:"))
if p<=200000:
    print("The simple interest:",(p*r*t)/100)
elif p>200000 and p<=1000000:
    print("The simple interest:",(p*t*12)/100)
else:
    print("The simple interest:",(p*t*15)/100)