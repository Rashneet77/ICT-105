# Worksheet 1 Session 2: Syntax, Variables, Types, and Operators
# Name: Rashneet Takhi
# Student ID: 12045112
# ICT105 Worksheet 1
# Advanced Network Security - Session 9 & 10
# Author: Tosh

# 1. Declare two variables, a and b.
a = 15
b = 12

print("1. Variable declaration and types:")
print("a =", a)
print("b =", b)
print("type(a) =", type(a))
print("type(b) =", type(b))
print()

# 2. Basic arithmetic operations
print("2. Basic arithmetic operations:")
sum_result = a + b
print("a + b =", sum_result, "# expected output: 27")

sub_result = a - b
print("a - b =", sub_result, "# expected output: 3")

mul_result = a * b
print("a * b =", mul_result, "# expected output: 180")

div_result = a / b
print("a / b =", div_result, "# expected output: 1.25")
print()

# 3. Using variables and type casting
c = int(a / b)
print("3. Integer division result stored in c:")
print("c =", c, "# expected output: 1")
print("type(c) =", type(c), "# expected output: <class 'int'>")

c_float = float(c)
print("c as float:")
print("c_float =", c_float, "# expected output: 1.0")
print("type(c_float) =", type(c_float), "# expected output: <class 'float'>")
print()

# 4. Working with strings
message = "The result of a divided by b is?"
print("4. Working with strings:")
print(message)
print(message, str(c), "# expected output: The result of a divided by b is? 1")
print()

# 5. Comparison operators
print("5. Comparison results:")
print("a > b is", a > b, "# expected output: True")
print("a == b is", a == b, "# expected output: False")