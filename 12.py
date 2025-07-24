#write a program using a while loop to print all the odd numbers within a given range
start=int(input("Enter start number:"))
end=int(input("Enter end number:"))
for num in range(start,end+1):
    if num%2!=0:
        print(num,end=" ")