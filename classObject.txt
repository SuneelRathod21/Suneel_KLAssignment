# creating a class for calculator and defining all the functions like(+,-,*,/).
class Calculator:
    def addition(self):
        print(a + b)
    def subtraction(self):
        print(a - b)
    def multiplication(self):
        print(a * b)
    def division(self):
        print(a / b)
        
# taking input from the user
a = int(input("Enter first num_1:"))
b = int(input("Enter first num_2:"))

# creating a object for calculator
obj = Calculator()
choice = 1
while choice != 0:
    print("1. ADDITION:\n","2. SUBTRACTION:\n","3. MULTIPLICATION:\n","4. DIVISION\n:")
    
    # getting choice input from the user 
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(obj.addition())
    elif choice == 2:
        print(obj.subtraction())
    elif choice == 3:
        print(obj.multiplication())
    elif choice == 4:
        print(obj.division())
    else:
        print("enter valid choice")
