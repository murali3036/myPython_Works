#Write a program which should create a dictionary of key:values.
#'A':1 'B':2 'C':3 . . . . 'Z':26 [Use dictionary comprehension]

import string
Alpha =list(string.ascii_uppercase)
x = {key:value for key,value in zip(string.ascii_uppercase,range(1,len(Alpha)+1))} 
print(x)
