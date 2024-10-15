# Usually used to give functionality to user defined obejects.
"""
class Fruit:
    def __init__(self, name) -> None:
        self.name = name

banana = Fruit("Banana") 

print(banana * 4)
"""       

# Here '__init__' can be seen as the first dunder method that takes care of instantiating an object. 
# This is not called anywhere but it automatically happens as soon as we create an object.

"""
Rightnow if we try to multiply thjis banana with 4, then it won't be possible.
This is because we haven't defined the multiplication operator for the Fruit class yet. It will give an error of 
`TypeError: unsupported operand type(s) for *: 'Fruit' and 'int'`

But, we can provide this functionality to the class by adding a dunder method.
"""

class Fruit:
    def __init__(self, name) -> None:
        self.name = name

    def __mul__(self, num):  # <-- Not called directly. (Just one of many eg. of dunder method)
        return self.name * num 

banana = Fruit("Banana")
print(banana * 4)

# Alternate Method -->
# print(banana.__mul__(4))
