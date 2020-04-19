#Sort the list using lambda function
#mylist = [["john", 1, "a"], ["larry", 0, "b"]].
#Sort the list by second item 1 and 0


mylist = [["john", 1, "a"], ["larry", 0, "b"],["jack", 4, "d"], ["murs", 3, "c"]]

print(sorted(mylist, key = lambda i : i[1]))
