#Python program to interchange first and last elements in a list

def swapFisrtLastElement(a):
    print(a)
    a[0],a[-1] = a[-1],a[0]
    print(a)

l = [10,2,31,3,4,11,3,4,16,75]
swapFisrtLastElement(l)



    
    
