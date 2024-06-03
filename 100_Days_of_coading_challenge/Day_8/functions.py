# function that allows for an input
# def greet(name):
#     print(f"hi {name}")
#     print(f"hello {name}")
#     print(f"welcome back {name}")
#
#
# greet("Thapasya")


# argument: it is the actual piece of data that is passed to the function when it is called.
# parameter:it is the name of the data that , it is used inside the function to refer
# to it and to do things with it.
# In the above sentence name is the parameter and Thapasya is the argument

# *functions that allows for a multiple inputs- and those arguments are called positional arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with(location="India", name="Thapasya")
# or
# greet_with("THapasya", "India")
# *location="India" and name= "Thapasya" are the- keyword arguments
