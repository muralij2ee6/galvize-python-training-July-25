# Learning Objectives 

# 1. Understand the basics of Python syntax and data types.
# 2. Work with variables, strings, and numbers, and booleans 
# 3. Use some built in functions (print, type, len, input)
# 4. Basic String formatting and operations 
# 5. implement some conditional lgoic using if,elif, else statements
# 6. basic loops


name = "Alice"
age = 30 # integer value
is_developer = True # boolean value - true or false
salary = 100000.50 # float value

# print(name)'
print("Hello, " + name + "!")  # Concatenating strings
# print("Your age is: " + age)
print("Your age is: " + str(age))  # Converting integer to string for

print(type(age)) # integer type
print(type(str(age))) # string type

print(f"{name}, who is {age} years old, is a developer: {is_developer}.")  # f-string formatting


# basic math 

x = 10 
y = 3

print(f"Addition: {x + y}")  # Addition
print(f"Subtraction: {x - y}")  # Subtraction
print(f"Multiplication: {x * y}")  # Multiplication
print(f"Division: {x / y}")  # Division
print(f"Integer Division: {x // y}")  # Integer Division
print(f"Modulus: {x % y}")  # Modulus
print(f"Exponentiation: {x ** y}")  # Exponentiation