mydict={
    "Fast":"in a quick manner",
    "Rohan":"A coder",
    "Marks": "[1,2,3,4]",
    "anotherdict":{'Rohan':'another player'}
}
print(mydict["Fast"])
print(mydict["Rohan"])
mydict["Marks"]=[45,89,76]
print(mydict["Marks"])
print(mydict['anotherdict']['Rohan'])

print(mydict.keys())  # PRINTS THE KEYS OF THE DICTIONARIES
print(mydict.values())  # PRINT THE VALUES OF THE DICTIONARY
print(mydict.items())  # prints the keys and values for all contents IN A DORMATE OF A TUPPLE.
print(mydict.update({
    "Rohit":"friend",
    "Rajat":"friend"

}))
print(mydict)  # OTHER METHORD WORKING OR NOT WORKING.. CHECK IT
print(mydict.get("Rohan")) # THROWS NONE IF NOT PRESENT IN DICTIONARY.
# print(mydict["Rohan"]) DOES SAME THING BUT IT THROWS AN ERROR IF NOT PRESENT IN DICTIONARY
