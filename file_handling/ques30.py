# Write a program for GCD of more than two numbers stored in a list.
def gcd(a, b): 
    if a == 0 : 
        return b  
    return gcd(b % a, a) 

def lcm(a, b): 
    return (a*b) / gcd(a, b) 

def findGCD(list): 
    result = list[0] 
    for i in range(1, len(list)): 
        result = gcd(result, list[i]) 
  
    return result 

# Driver Program 
list = [4, 8, 12] 
print('GCD of', list, 'is', findGCD(list)) 

# Creating a file
f = open('GCD.txt','w+')

# Writing the result in the file
f.write(str(findGCD(list)))

# Closing the file
f.close()