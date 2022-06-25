# Control flow and logical operators

# IF condition
print("Welcome to rollercoaster")
height = int(input("Enter the height?"))
if height > 120 or height == 120:  # Can use >= instead as well
    print("you can ride the rollercoaster")
else:
    print("You will have to grow taller!!")

# program that works out whether if a given number is an odd or even number
number = int(input("Which number do you want to check? "))

if (number % 2) == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    condition = 'underweight'
elif 18.5 <= bmi < 25:  # Another way is to just mention 'elif bmi < 25' and it does work!!!
    condition = "normal weight"
elif 25 <= bmi < 30:
    condition = "slightly overweight"
elif 30 <= bmi < 35:
    condition = "obese"
else:
    condition = "clinically obese"

intbmi = round(bmi)

if (condition != "normal weight"):
    print(f'Your BMI is {intbmi}, you are {condition}.')
else:
    print(f'Your BMI is {intbmi}, you have a {condition}.')

# Program to check if a given year is a leap year
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")

# build an automatic pizza order program.
# Based on a user's order, work out their final bill.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == 'S':
    if (add_pepperoni == 'Y'):
        bill = 15 + 2
    else:
        bill = 15

elif size == 'M' or size == 'L':
    if size == 'M':
        bill = 20
    if size == 'L':
        bill = 25

    if (add_pepperoni == 'Y'):
        bill += 3
if (extra_cheese == 'Y'):
    bill += 1

print(f"Your final bill is: ${bill}.")

# LOVE CALCULATOR

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

comb_name = name1.lower() + name2.lower()  # You need to make it to lower case, else count function wouldn't count the uppercase characters

cat1 = comb_name.count("t") + comb_name.count("r") + comb_name.count("u") + comb_name.count("e")
cat2 = comb_name.count("l") + comb_name.count("o") + comb_name.count("v") + comb_name.count("e")

combine = str(cat1) + str(cat2)
int_comb = int(combine)

if int_comb < 10 or int_comb > 90:
    print(f"Your score is {int_comb}, you go together like coke and mentos.")
elif 40 < int_comb < 50:
    print(f"Your score is {int_comb}, you are alright together.")
else:
    print(f"Your score is {int_comb}.")

# PROJECT - TREASURE HUNT
print ("Welcome to Treasure Island.\nYour mission is to find the treasure.")
dir = input ('You\'re at a crossroad, where do you want to go? Type "left" or "right?"')

if dir.lower() == "left":
    n1 = input("swim or wait?")
    if n1.lower() == "wait":
        n2 = input("Which door? -Yellow/Blue/Red")
        if n2.lower() == "red":
            print("Burned by fire.\nGame Over.")
         elif n2.lower() == "blue":
            print("Eaten by beasts.\nGame Over.")
         elif n2.lower() == "yellow":
            print("You Win!")
        else:
            print("Game over.")
    else:
        print("Attacked by trout.\nGame Over.")

else:
    print("Fall into a hole.\nGame over.")


