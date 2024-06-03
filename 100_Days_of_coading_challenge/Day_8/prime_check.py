def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("it's not a prime number")


num = int(input("Enter a number to check whether it's a prime number or not-"))
prime_checker(number=num)
