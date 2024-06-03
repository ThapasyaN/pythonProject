import random
names = ["Thapasya", "Siddhartha", "Sushma", "Sandeep", "Rishi", "Sandeepanirishi"]
num_items = len(names)
print(f"there are {num_items} members to be picked to pay the bill")
random_choice = random.randint(0,num_items-1)
# its (item-1) because randint counts (the names) from 0 whereas the len function
# counts (the names) from 1
the_person_to_pay_the_bill = names[random_choice]
print(f"the person to pay the bill is {the_person_to_pay_the_bill}")

