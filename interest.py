#write a program to accept the principal amount, rate of interest, and duration from the user.Calculate the interest amount and the total amount(principal+interest)
p=(float(input("Enter amount:")))
r=(float(input("Enter rate:")))
t=(float(input("Enter time:")))
i=(p*r*t)/100
amt=(p+i)
print("The interest amount:",i)
print("The total amount:",amt)