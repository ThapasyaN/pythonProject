# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
#                     # or , instead of opening and closing we can use a while loop
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
#
#                 # to write -
# # mode="a"  - to append new text to an existing code
# #         "r" - it goes to read only mode
# #         "w"  - to write new text . it erases the old text and writes the new one
#
# with open("my_file.txt", mode="a") as file:
#     file.write("\nnew text.")
#
# #     if you want to write a new text in a file that doesn't exist then the python itself creates a new file
#
#

with open("C:/Users/Siddhartha/workspace_python/pythonProject/newTextFile.txt") as file:
    contents = file.read()
    print(contents)

with open("/Users/Siddhartha/workspace_python/pythonProject/newTextFile.txt", mode="a") as file:
    file.write("welcome to my python project")

