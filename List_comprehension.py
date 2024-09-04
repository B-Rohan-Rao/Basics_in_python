list = [1, 2, 3]
new_list = []
for n in list:
    new_value = n + 1
    new_list.append(new_value)
print(new_list)    

# We can do this or, we can perform list comprehension to ovwercome this problem.
# new_list = [new_items for items in list]

llist = [1, 2, 3]
new_llist = [n + 1 for n in llist]
print(new_llist)   

# This comprehension works with all kinds of sequence(have proper order) like string, range and even tupple

name = "Rohan"
slice = [letters for letters in name]
print(slice)




# ADDING CONDITIONS TO COMPREHENSIONS:-
# new_list = [new_items for items in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanore", "Fraddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
Long_names = [name.upper() for name in names if len(name) > 5]
print(Long_names)