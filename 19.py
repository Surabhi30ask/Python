#write a program that prompts users to enter numbers.This process repeat until the user enters -1. Finally, the program prints the count of prime and composite numbers entered.
p=0 ; c=0
while(1):
    f=0
    a=int(input("Enter number:"))
    if a==-1:
        print("Exitting")
        break
    if a==1:
        continue
    for i in range(2,a):
        if a%i==0:
            f=f+1
            break
    if f==0:
        p=p+1
    else:
        c=c+1
print("Total no. of prime number:",p)
print("Total no. of composite number",c)