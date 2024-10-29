"""
decorators can be simply understood and a function that changes and returns other functions.
"""

# For example consider the following snippet of code.
def hello_world():
    print("Hello World")

hello_world()    

# This will print "Hello World" on the console. It is without any kind of decorator.We can create a decorator and
# decorate same function

def greet(fx):
    def wrapper():
        print("Good morning")
        fx()
        print("Good night")
    return wrapper

@greet
def hello():
    print("Hello World")


hello()    
"""
    `greet(hello())()`
We can also use the above syntax if we not want to write the decorator above the function. But using decorator
keyword is easier to understand.
"""


# >>>>>>>>>>>>>> Use case example <<<<<<<<<<<<<<<<<<<

import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_func_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with arguments as {args} and kwargs as {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_func_call
def my_function(a, b):
    return a + b

my_function(1, 3)
