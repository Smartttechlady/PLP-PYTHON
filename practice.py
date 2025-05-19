# Arithmetic
a = 10
b = 3

print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Exponent:", a ** b)        # 1000

# String operations
name = "Ibukun"
greeting = "Hello, " + name + "!"
print(greeting)

# String methods
print(name.upper())      # "IBUKUN"
print(name.lower())      # "ibukun"
print(name[0])           # "I" - First character
print(name[-1])          # "n" - Last character
print(len(name))         # 6


# Variables and types
age = 25
price = 49.99
is_online = True
username = "Smarttechlady"

# Print types
print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(is_online)) # <class 'bool'>
print(type(username))  # <class 'str'>


# Using f-strings
name = "Ibukun"
age = 25
print(f"My name is {name} and I am {age} years old.")


name = input("What is your name? ")
age = int(input("How old are you? "))
year = 2025 + (100 - age)
print(f"Hi {name}, you will turn 100 years old in the year {year}.")

