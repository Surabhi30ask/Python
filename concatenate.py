m = int(input("Number of elements in the list 1:"))
n = int(input("Number of elements in the list 2:"))
lst1 = [0]*m
lst2 = [0]*n
print("Enter elements of list 1: ")
for i in range(m):
    lst1[i] = int(input())
print("Enter elements of list 2 ")
for i in range(n):
    lst2[i] = int(input())
l3 = []
for i in lst2:
    k=0
    for j in lst1:
        if i==j:
            k=1
            break;
    if k==0:
        l3.append(i)
print("Required list-",l3)