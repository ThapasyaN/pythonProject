# A Python dictionary is a data structure that stores values in key:value pairs.
# Tuple is one of the 4 built-in data types in Python used to store collections of data, the other 3 are
# List, Set, and Dictionary, all with different qualities and usage.
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary)
# dictionaries have elements that are identified by their key
# dictionary = {key : value}

# to add the latest item in your code
programming_dictionary["loop"] = "The action of doing something over and over."
print(programming_dictionary)

# wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# edit a pre-existing item in your dictionary
programming_dictionary["Bug"] = "Insect around the flowers"
print(programming_dictionary)

# to loop through a dictionary
for key in programming_dictionary:
    print(key)  # only to print the key
    print(programming_dictionary[key])  # to print key as well as the value
