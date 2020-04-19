#Write a recursive function to compute x raised to the power of n.

def recursiveFunc(x,n):
    if n!=0:
        return x*recursiveFunc(x,n-1)
    else:
        return 1

while(1):
    number = int(input('Enter the number '))
    exponent = int(input('Enter exponential number '))
    result = recursiveFunc(number,abs(exponent))
    print(result)
