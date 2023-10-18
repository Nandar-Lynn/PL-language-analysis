# Simplicity: Python's syntax is simple and minimal.
# It is demonstrated by calculating the square of a number in the following function:

def square(num):
    return num ** 2


# Orthogonality:  Python constructs can be used in consistent and independent ways.
# It is demonstrated by computing the circle area in the following function:
import math
    
def circle_area(radius):
    return math.pi * radius ** 2
    

# Data types: Python dynamically allocates the variables.
# This function shows data type manipulations (numeric, string, and list types).
    
def data_types():
    num = 3.3
    string = 'Hello'
    listObj = [1, 2, 3]
    print(type(num), type(string), type(listObj))


# Syntax Design: Python uses indentation and whitespaces for simple and readable syntax.
# To demonstrate, here's a simple for loop that iterates over a list.

def syntax_design():
    fruits = ['kiwi', 'mango', 'orange']
    for item in fruits:
        print(f'This is a {item}')


# Abstraction: This can be done through classes and functions.

class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def get_descriptives(self):
        return f"{self.name} {self.age} {self.phone}"


# Expressivity: Python has good high level constructs => list comprehensions.
# This function demonstrates Python's expressivity.

def expressivity():
    numbers = [1, 2, 3, 4, 5]
    squares = [num ** 2 for num in numbers]
    print(squares)


# Type Checking: Python has dynamic but strong type system. 

def addition(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Inputs x and y must be numeric")
    return x + y

# Exception Handling: Python has try/except/finally blocks for this.

def exception_handling():
    try:
        answer = 10 / 0
    except ZeroDivisionError:
        print("You can't divide by zero!")
    finally:
        print("This is executed after the try and except blocks!")

    
# Restricted aliasing: Python restricts two variables from pointing at the same object in memory. 

def restricted_aliasing():
    x = [1, 2, 3]
    y = x[:]
    y.append(4)
    print(f"x: {x}")  # [1, 2, 3]
    print(f"y: {y}")  # [1, 2, 3, 4]
    

def main():
    print(square(10))
    print(circle_area(5))
    data_types()
    syntax_design()

    newPerson = Person('Alex', '22', '1234567890')
    print(newPerson.get_descriptives())

    expressivity()
    print(addition(2, 3))
    exception_handling()
    restricted_aliasing()


if __name__ == "__main__":
    main()
