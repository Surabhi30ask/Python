#write a program to count the occurences of a word in a given sentence
str=input("Enter a string:")
word=input("Enter word:")
a=[]
count=0
a=str.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
print("Count of the word is:",count)