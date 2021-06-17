# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# importing math module
import math

# function to add numbers
def add(X, Y):
    return X + Y

# function to subtract numbers
def subtract(X, Y):
    return X - Y

# function to multiply number
def multiply(X, Y):
    return  X * Y

# function to divide number
def divide(X, Y):
    return int(X / Y)

# function to find square root of number
def sqrt(X):
    return math.sqrt(X)

# function to find square of number
def square(X):
    return int(X ** 2)

# function to find sin value of number
def sin(X):
    return math.sin(X)

# function to find cos value of number
def cos(X):
    return math.cos(X)

# function to find tan value of number
def tan(X):
    return math.tan(X)

# menu function
def menu():
    print("""
        1. Addition(X, Y)
        2. Subtraction(X, Y)
        3. Multiplication(X, Y)
        4. Divide(X, Y)
        5. Square(X)
        6. Square Root(X)
        7. sin(X)
        8. cos(X)
        9. tan(X)""")
    print()
    return int(input("Select the operation which you want to perform : "))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Console Base Scientific Calculator!!!!")

    # call menu() and store the value in variable
    op_num = menu()

    # while loop to perform different calculation tasks
    while op_num < 10:
        if op_num == 1:
            X = int(input("Enter first number: "))
            Y = int(input("Enter first number: "))
            print("Addition is: ",add(X, Y))
        elif op_num == 2:
            X = int(input("Enter first number: "))
            Y = int(input("Enter first number: "))
            print("Subtraction is: ",subtract(X, Y))
        elif op_num == 3:
            X = int(input("Enter first number: "))
            Y = int(input("Enter first number: "))
            print("Multiplication is: ",multiply(X, Y))
        elif op_num == 4:
            X = int(input("Enter first number: "))
            Y = int(input("Enter first number: "))
            print("Division is: ",divide(X, Y))
        elif op_num == 5:
            X = int(input("Enter a number: "))
            print("Square is: ",square(X))
        elif op_num == 6:
            X = int(input("Enter a number: "))
            print("Square root is: ",sqrt(X))
        elif op_num == 7:
            X = int(input("Enter a number: "))
            print("Sin is: ",sin(X))
        elif op_num == 8:
            X = int(input("Enter a number: "))
            print("cos is: ",cos(X))
        elif op_num == 9:
            X = int(input("Enter a number: "))
            print("tan is: ",tan(X))
        else:
            print("Choose another operation!!!")

        # Ask user to continue or stop
        con_val = int(input("Choose 1 - Yes and 0 - No to continue!!!"))
        if con_val == 1:
            op_num = menu()
        else:
            print("Thank you for using calculator!!!")
            break
        
        
        

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
