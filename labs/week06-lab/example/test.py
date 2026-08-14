# พวกผลรันจาก function.py

# Part 2
# Example 1: Function with one parameter
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()
"""Calling greet_person with different names:
Hello, Alice! Nice to meet you.
Hello, Bob! Nice to meet you.
Hello, Charlie! Nice to meet you."""

#Example2
# Example 2: Function with multiple parameters
def introduce_person(name, age, city): #ใครอยากใช้ฉันต้องใส่ 3 ตัวเท่านั้น
    """Introduces a person with their details"""
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")
"""Calling introduce_person:
Hi! My name is Diana.
I am 25 years old.
I live in New York.

Hi! My name is Eve.
I am 30 years old.
I live in Los Angeles."""

#Example3
# Example 3: Mathematical function
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)
"""Calculating rectangle areas:
Rectangle with length 5 and width 3
Area = 5 × 3 = 15

Rectangle with length 10 and width 7
Area = 10 × 7 = 70
""""

#Part 3
#Example 1
""""Using functions that return values:
5 + 3 = 8
10 + 7 = 17
Sum of both results: 25"""

#Example 2
"""Circle calculations:
Circle with radius 5:
Area: 78.54
Circumference: 31.42"""

#Example3
"""Using return values in expressions:
multiply(4, 5) + square(3) = 20 + 9 = 29"""

#Part 4
#Example 1
"""
Using default parameters:
Hello, Mr./Ms. Smith!
Hello, Dr. Johnson!
Hello, Prof. Brown!
"""

#Example 2
"""
Multiple default parameters:
Profile: Alice, Age: 18, Country: Unknown
Profile: Bob, Age: 25, Country: Unknown
Profile: Charlie, Age: 30, Country: USA
"""

#Example 3
"""
Power function with defaults:
power(5) = 25
power(5, 3) = 125
power(2, 4) = 16
"""

#Part 5
#Global variables พาร์ทขอบเขตของตัวแปร
"""
Scope demonstration:
Before function call - Counter: 0
Inside function - Global: I'm a global variable
Inside function - Local: I'm a local variable
Counter inside function: 1
After function call - Counter: 1
Outside function - Global: I'm a global variable
"""

#Part 6
#Example 1
"""
Grade Calculator:
Score 95 = Grade A
Score 87 = Grade B
Score 73 = Grade C
Score 68 = Grade D
Score 45 = Grade F
"""

#Example 2
"""
Password Validator:
✗ 'abc123': Password too short (minimum 8 characters)
✗ 'password': Password must contain at least one number
✓ 'mypass123': Password is strong!
✗ 'str0ng!': Password too short (minimum 8 characters)
✗ 'weak': Password too short (minimum 8 characters)
"""

#Example 3
"""
Temperature Converter:
25°C = 77.0°F
77°F = 25.0°C
0°C = 32.0°F
32°F = 0.0°C
"""

#Example 4
"""
Calculator Functions:
12 + 4 = 16
12 - 4 = 8
12 × 4 = 48
12 ÷ 4 = 3.0
12 ÷ 0 = Error: Cannot divide by zero
"""
