# Whenever we use for loops, we need an index for traversal.

"""
marks = [12, 23, 45, 43, 65, 41]
index = 0
for mark in marks:
    print(mark)
    index += 1   
    if(index == 3):
        print("This is the third mark")
"""
     

# For the above code snippet, we need the 'index' variable to go get the index number. But this includes defining
# the varibale in a seperate line adn incrementing it in seperate line. 
# Enums eliminates this hastle


marks = [12, 23, 45, 43, 65, 41]
for index, mark in enumerate(marks):
    """Enumerate function is a nuilt-in function in python that allows us to loop over a sequence
    (such as list, tuple or string) and get the index and value of each elements of each element at the same 
    time. 
    """
    print(mark)  
    if(index == 3):
        print("This is the third mark")



