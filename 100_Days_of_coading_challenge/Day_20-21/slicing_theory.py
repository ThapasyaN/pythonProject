piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# to slice it from position c to e i.e 2 to 5:
print(piano_keys[2:5])

# to slice from position 2 to the end of the list:
print(piano_keys[2:])

# to slice from starting position to the position 5 :
print(piano_keys[:5])

# slicing between 2 positions by incrementing it by certain number:
print(piano_keys[2:5:2])

# to slice everything by 2 phases :
print(piano_keys[::2])

# to reverse the order of the list:
print(piano_keys[::-1])

"""ALL THESE METHOD OF SLICING CAN ALSO BE USED IN A TUPLES """

piano_tuple = ["do", "re", "mi", "fa", "so", "la", "ti"]
print(piano_tuple[2:])



