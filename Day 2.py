# Data type

# string- we can split individual characters
print("Hello"[2])

# Type conversion
# Following code will throw error as it we are trying to concat two different data types
num_char = len(input("what is your name?"))
print("Your name has " + num_char + " characters")
# To fix the above error
num_char = len(input("what is your name?"))
new_char = str(num_char)
print("Your name has " + new_char + " characters")

# to check data type
type("new_var")

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35,
# then the output should be 3 + 5= 8
two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number)) --shows us that the input is stored as str, even though its a number
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Always dividing would give you a float output
print(4 / 2)
# Alternatively we can use flow division to get a rounded of int value
print(3 // 2)
# Order of execution varies
# PEMDAS - Parentheses, Exponents, Multiplication, division, addition, subtraction

#  BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / (float(height) ** 2)
print(int(bmi))

# Approximation
print((8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))  # round to particular no of digits

score = 2
score = score + 1
print(score)
# Easier way of writing
score += 2  # Or can use -= , *=, /=
print(score)

# There is a simple way to combine multiple datatype in print statement- using F-string
# Else you need to change each one individual to avoid errors
score = 0
height = 1.8
isWinning = True
# F-string -- write f before quotes and mention variables in braces
print(f"Your score is {score},your height is {height}, you are winning is {isWinning}")

# Create a program using maths and f-Strings that tells us how many days, weeks, months
# we have left if we live until 90 years old.
age = input("What is your current age?")
ageleft = 90- int(age)

months = ageleft *12
weeks = ageleft*52
days = ageleft*365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Tip calculator - Project
print("Welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

total = bill + (bill* (tip/100))
overallsplit = total/split
roundval = round(overallsplit,2)

print(f"Each person should pay: ${roundval}")
