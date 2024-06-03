import math


def print_calc(height, width, cover):
    num_cans = ((height * width) / cover)
    round_of_cans = math.ceil(num_cans)
    print(f"you need {round_of_cans} cans to paint")


test_h = int(input("Enter the height-"))
test_w = int(input("Enter the width-"))
coverage = 5
print_calc(height=test_h, width=test_w, cover=coverage)
