#SecondLargestElementInTheList

def SecondLargestElement(a):
    a.sort(reverse = True)
    print(a)
    print(a[1])


l = [10,29,583,2394,22054,23485,10394,7457,84732]
SecondLargestElement(l)
