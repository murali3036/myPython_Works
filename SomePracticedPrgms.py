#SecondLargestElementInTheList

def SecondLargestElement(a):
    a.sort(reverse = True)
    print(a)
    print(a[1])


l = [10,29,583,2394,22054,23485,10394,7457,84732]
SecondLargestElement(l)
###################################################

#Python program to find sum of elements in list

def sumofelelments(a):
    sum = 0
    for i in a:
        if type(i) == int:
            sum = sum + i
    print(sum)

l = [10,30,20,'a',10]
sumofelelments(l)

###################################################

#Python program to interchange first and last elements in a list

def swapFisrtLastElement(a):
    print(a)
    a[0],a[-1] = a[-1],a[0]
    print(a)

l = [10,2,31,3,4,11,3,4,16,75]
swapFisrtLastElement(l)

###################################################

#


    
    


