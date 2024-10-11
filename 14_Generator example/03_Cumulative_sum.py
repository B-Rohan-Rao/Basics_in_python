from typing import Generator

def cumulative_sum():
    """
    yield total: This pauses the generator and returns the current value of total. When yield is used in 
    conjunction with .send(), the generator can receive a value (in this case, new_value) and continue execution.

    new_value = yield total: After pausing and yielding total, the generator waits for the next value to be sent 
    in by the .send() method (which we will see later in the code). The sent value is assigned to new_value.

    total += new_value: Once a new value is received through .send(), this line adds new_value to the cumulative 
    sum (total), updating it.

    next(cumulative_generator): The first call to next() is used to "prime" the generator. This advances the 
    generator to the first yield statement, allowing it to be ready to receive values using .send().

    Yields:
        _type_: _description_
    """
    total:float = 0
    while True:
        new_value:float = yield total
        total += new_value

cumulative_generator = cumulative_sum()
next(cumulative_generator)

while True:
    value = float(input("Enter a value : "))
    current_sum = cumulative_generator.send(value)
    print(f'Cumulative sum = {current_sum}')