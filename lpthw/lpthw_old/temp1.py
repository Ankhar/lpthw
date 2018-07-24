a = [1,2,3,4]
b = [x for x in a]
print a
print b
a = [[1,2],[3,4],[5,6]]
b = [x for xs in a for x in xs]
print a
print b