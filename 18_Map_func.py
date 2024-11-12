# map function provide the functionality to the elements of any iterable items.

l= [1, 4, 7, 8, 5, 2, 3]
# newl = []
# for i in l:
#     newl.append(cube(i))
# print(newl)
newl = list(map(lambda x: x*x*x, l))
print(newl)



# returns elements based on the the case if the qualify the test case or not

def filter_function(a):
    return a > 4

l= [1, 4, 7, 8, 5, 2, 3]
newl = list(filter(filter_function, l))
print(newl) # prints [7, 8, 5]