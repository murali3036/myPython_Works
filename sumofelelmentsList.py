#Python program to find sum of elements in list

def sumofelelments(a):
    sum = 0
    for i in a:
        if type(i) == int:
            sum = sum + i
    print(sum)

l = [10,30,20,'a',10]
sumofelelments(l)

