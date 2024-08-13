global_var = 10  # Global variable
print("Outside the function before changing: global_var =", global_var)

def modify_global():
    global global_var  # Access the global variable
    global_var = 20  # Change the value of the global variable
    print("Inside the function: global_var =", global_var)  # Print the modified value

modify_global()  # Call the function
global_var = 30  # Modifying the variable outside of  the funcion

print("Outside the functionafter changing: global_var =", global_var) # Print the global variable after calling the function
