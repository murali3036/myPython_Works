# Write a for loop that prints all elements of a list
# and their position in the list.

def printLst(lst):
    for i,j in enumerate(lst):
        print("index "+str(i)+ ",element "+str(j))

lst = [4,7,3,2,5,9]

printLst(lst)
