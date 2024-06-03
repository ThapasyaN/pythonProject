import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '8', '(', ')', '-', '=', '+']

print("\nWelcome to PyPassword Generator")
num_letters = int(input("How many letter do you like\n"))
num_numbers = int(input("How many numbers do you like\n"))
num_symbols = int(input("How many symbols do you like\n"))

# HARD METHOD
password_list = []
for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, num_numbers + 1):
    password_list += str(random.choice(numbers))

for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

# to convert the list into a string
# to shuffle the password

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is: {password}")

#                                              'or'
# EASY METHOD
# password = ""
# for char in range(1, num_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, num_numbers + 1):
#     password += str(random.choice(numbers))
#
# for char in range(1, num_symbols + 1):
#     password += random.choice(symbols)
#
# print(password)

