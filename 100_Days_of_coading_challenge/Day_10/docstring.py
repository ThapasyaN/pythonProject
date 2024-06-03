# Docstring: it converts the user defined functions into a user defined and then it gets populated in the decstring
# or it creates definitions to the user defined functions.
# or Python docstrings are the string literals that appear
# right after the definition of a function, method, class, or module. Example:
len(name)
# >>
# builtins
# [def len(__obj: Sized) -> int
# Return the number of items in a container.
# `len(__obj)` on docs. python. org\]

# the above lines will be displayed when the cursor is places on the built_in functions.
# so, the docstring will convert and display the similar type of lines to the user defined functions.

def function_output(f_name, l_name):
    """Takes the first and the last name and then formats it to a title case version of that name"""
    if f_name == "" or l_name == "":
        return "invalid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    #     or
    return f"{formated_f_name} {formated_l_name}"


print(function_output((input("Enter your first name- ")), input("Enter your last name- ")))

# multi line comment
"""HELLO THAPASYA
HOW ARE YOU 
BYE"""