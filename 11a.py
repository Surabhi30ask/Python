#write a program to print the following patterns
#           1
#           2,3
#           4,5,6
#           7,8,9,10
#           11,12,13,14,15
current_num=1
rows=5
stop=2
for i in range(rows):
    for column in range(1,stop):
        print(current_num,end=' ')
        current_num+=1
    print("")
    stop+=1