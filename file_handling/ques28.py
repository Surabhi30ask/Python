#Write a function that accepts a string and calculate the number of upper case letters and lower case 
#letters. file handling using python

def count_upper_lower_case(my_string):
    upper_count = 0
    lower_count = 0
    for letter in my_string:
        if letter.isupper():
            upper_count +=1
        elif letter.islower():
            lower_count +=1
    return upper_count, lower_count

print(count_upper_lower_case('The quick Brown Fox'))