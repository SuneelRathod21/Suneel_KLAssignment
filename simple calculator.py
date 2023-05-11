# defining functions for add, sub, mul, div
def add(a, b):
    # returns the addition of two numbers
    return a + b


def sub(a, b):
    # returns the subtraction of two numbers
    return a - b


def mul(a, b):
    # returns the multiplication of two numbers
    return a * b


def div(a, b):
    # returns the division of two numbers
    return a / b


print("choose the operation given below")
print(" 1 for add:\n", "2 for sub:\n", "3 for multiplication:\n", "4 for division\n: ")
choice = input("Please enter choice:")

# taking two input from the user
a = int(input("enter a number_1:"))
b = int(input("enter a number_2:"))

# we use if, elif and else statements to execute particular operation
if choice == '1':
    print(add(a, b))

elif choice == '2':
    print(sub(a, b))

elif choice == '3':
    print(mul(a, b))
elif choice == '4':
    print(div(a, b))
else:
    # this statement will executes if all the above conditions fails
    print("Invalid choice choose the correct choice")
    
