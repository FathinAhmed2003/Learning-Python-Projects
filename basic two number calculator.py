def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


print("Welcome to the Nafees's Calculator!!")

num1 = float(input("\nEnter first number: "))
operator = input("Operator options are +, - , *, / \nEnter operator: ")
num2 = float(input("\nEnter second number: "))

if operator == "+" or operator == "+ ":
    print(addition(num1, num2))
elif operator == "-" or operator == "- ":
    print(subtraction(num1, num2))
elif operator == "*" or operator == "* ":
    print(multiplication(num1, num2))
elif operator == "/" or operator == "/ ":
    print(division(num1, num2))
else:
    print("\nPlease retry with just operators listened with no more than one space after operator symbol.")
