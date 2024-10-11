#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ARGS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# args are used to that the function can be made more flexible and not limiting the number of 
# arguments that are passed to that particular funtion.

def add(*args):
    print(args)
    result = 0
    for n in args:
        result += n
    return result

print(f"Result of the numbers are: {add(1,2,3,4,5,6)}")        
# Note that the arguments which are passed to the function are in the form of tupple.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KWARGS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
 
# kwargs are used to pass keyword arguments to the function which are not fixed.
# Note that the arguments which are passed to the function are in the form of dictionary.

def calculate(n, **kwargs):
    print(kwargs)
    # n += kwargs["add"]
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    n /= kwargs.get("divide")
    n -= kwargs.get("subtract")  
    """
    The benifit of using ".get()" is that if the keyword is not specified and still tried to be accessed then
    the program will not crash. Instead it will return none.
    In our case, If we would have tried to access `kwargs["add"]` functionality without spicifing `add=3` in 
    the function call then the program would have crashed. But for other kweyworInstead.ds like 
    `kwargs.get("divide")`, it will not crash and will return none
    """
    print(n)

calculate(2, add=3, multiply=5, divide=2, subtract=3)    
