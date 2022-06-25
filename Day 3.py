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

if (number%2)==0:
    print("This is an even number.")
else:
    print("This is an odd number.")



