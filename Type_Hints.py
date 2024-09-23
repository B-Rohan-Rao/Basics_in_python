"""
While creating any kind of variable, we can assign them a type Of which we want to store the data. 
For example, string floating point numbers, integers or Boolean types.
"""
age : int
name : str
is_adult : bool
height: float
# This is the syntax to assign datatypes to any variables.


# We can do the same with fuictions.
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else: 
        can_drive = False
    return can_drive


"""
The above function states that the argument passes to the function must be of integer type. Because of this, 
the error will be Highlighted in the code itself if any other data type agrgument is passes.
It also hard codes the return type of the function. In out case, It is boolean.

This is called `Type hint` in python.
This is used when we want our ide to spot any Potential bugs and keep the code safer and less prone to crashing 
of the program
"""

police_check(13)