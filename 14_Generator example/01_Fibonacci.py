from typing import Generator


def fibonacci_generator():
    """
        a, b = 0, 1: This initializes the first two numbers of the Fibonacci sequence (a = 0, b = 1).

        while True: This creates an infinite loop, meaning the generator will keep running until manually stopped.

        yield a: Instead of returning a value (like in regular functions), yield pauses the function and returns 
        the current value of a. On the next call, the function resumes from where it left off.

        a, b = b, (a+b): This updates a and b so that a becomes the next Fibonacci number and b is the sum of the 
        previous two Fibonacci numbers. This is how the Fibonacci sequence works.
    Yields:
        _type_: _description_
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a+b)


fib_gen = fibonacci_generator()
print("This is fibonacci Series without generator")
n = 10
line_break = '-' * 20  
while True:
    input(f'Press "Enter" for the next {n} number of fibonacci:') 
    print(line_break) 
    for i in range(n):
        print(f'{next(fib_gen)}')

    print(line_break)         

