# map function provide the functionality to the elements of any iterable items.

def cube(x):
    return x**3

l= [1, 4, 7, 8, 5, 2, 3]
# newl = []
# for i in l:
#     newl.append(cube(i))
# print(newl)


newl = list(map(cube, l))
print(newl)