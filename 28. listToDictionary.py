#Using given list L = ['a', 'b', 'c', 'd']
#create a dictionary of key:values.

L = ['a', 'b', 'c', 'd']
x = {}
for i,j in enumerate(L):
	x.update(dict.fromkeys(j,i))

print(x)
