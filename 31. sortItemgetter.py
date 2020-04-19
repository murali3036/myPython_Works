#Sort the list using operator.itemgetter function
#mylist = [["john", 1, "a"], ["larry", 0, "b"]].
#Sort the list by second item 1 and 0.

from operator import itemgetter

mylist = [["john", 1, "a"], ["larry", 0, "b"],["jack", 4, "d"], ["murs", 3, "c"]]
print(sorted(mylist, key = itemgetter(1)))
