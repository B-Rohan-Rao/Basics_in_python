import sys

"""
Iterators and generators in Python are both used to iterate over data, but they have key differences in how 
they work and are implemented.

>>Iterator: 
An iterator is an object in Python that implements two methods: __iter__() and __next__(). 
It maintains its internal state and produces one item at a time when next() is called.
It should be noted that iterators May use more memory since the entire sequence might need to be stored in 
memory.
It terminates when there are no more elements, raising a StopIteration exception.

>>Generator: 
A generator is a special type of iterator defined using a function that uses the yield keyword. 
It allows you to iterate over data lazily without creating the entire sequence in memory at once.
It terminates automatically when the function finishes or a StopIteration is raised.
"""

# ITERATOR---------->
class MyIterator:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_val:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Usage
it = MyIterator(5)
for value in it:
    print(value)


# GENERATOR--------->
def my_generator(max_val):
    current = 0
    while current < max_val:
        current += 1
        yield current

# Usage
gen = my_generator(5)
for value in gen:
    print(value)


"""
The code above demonstrates the use of iterators and generators in Python.

The key takeaway is that generators are often simpler and more memory-efficient, especially when handling 
large datasets. A practical example of this can be seen when processing large datasets where we only care about 
the current iteration, without needing to revisit previous or future iterations. For instance, when searching 
for a specific word in a large file, we only need the current line being read.

In such cases, generators are particularly useful because they allow us to avoid loading the entire dataset into 
memory at once. By generating values lazily, one at a time, they help optimize memory usage while processing 
large amounts of data.
"""


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> COMPREHENTION <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

my_list = [i for i in range(1000000)]  # List comprehension (iterator-like)
print(sys.getsizeof(my_list)) # <-- Output = 8448728
# Stores all 1,000,000 items in memory


my_gen = (i for i in range(1000000))  # Generator expression
print(sys.getsizeof(my_gen)) # <-- Output = 192
# Stores only the current item and state in memory
