from calculator_art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculation():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operators:
        print(symbol)

    should_continue = True
    while should_continue:
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculator_function = operators[operator_symbol]
        # the operator chosen by the user is stored in the variable calculator_function
        answer = float(calculator_function(num1, num2))
        print(f"{num1} {operator_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            print("Thank you")
            should_continue = False
            calculation()


calculation()
