#write a program to accept the principal amount,rate of interest, and duration from thr user. calculate the interest amount and the total amount(principal+interest)
p=float(input("Enter principal amount:"))
r=float(input("Enter rate:"))
t=float(input("Enter time:"))
SI=(p*r*t)/100
print("The simple interest is:",SI)
print("The total amount is:",p+SI)