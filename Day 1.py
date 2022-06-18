#Day 1 

# - Printing start
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Write a program that prints the number of characters in a user's name. 
print(len(input("What is your name?")))

# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

c=a 
a=b
b=c

print("a: " + a)
print("b: " + b)



# Day 1 project - Band Name generator
print ("Welcome to the Band Name Generator")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print ("Your band name could be "+city + " "+pet)