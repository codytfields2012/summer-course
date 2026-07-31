# Problem 1
#ask the user for their name and their favorite number

# name = input("What is your name?\n")
# fav_num = input("What is your favorite number?\n")

# print("***************************************")
# print(f"*           Hello, {name}!              *")
# print(f"*     Your favorite number is {fav_num}.     *")
# print("***************************************")

# print("Raw input type:", type(name))
# print("Raw input type:", type(fav_num))
# as_int = int(fav_num)
# print(as_int)
# print(type(as_int))
# as_float = float(fav_num)
# print(as_float)
# print(type(as_float))

# Problem 2

# Use range() to print each sequence on a single line with values separated by spaces.
# all integers from 1 to 15 (inclusive)
# for i in range(1, 16):  # version 1
#     print(i, end=", ")

# print("\n", *range(1, 16))  # version 2, *range, unpacks the range directly into print, which uses spaces between arguments.

# print(*range(1, 16), sep=", ") # version 3, sep is a 'seperator' function that only places characters between items

# #all even numbers from 2 to 30 (inclusive)
# for e in range(2, 31, 2): #version 1, use the 'step' (start, stop, step), lets you skip however much you want
#     print(e, end=" ")

# for ei in range(2, 31): # version 2, use the % modulo, any number thats evenly divided by 2 will be printed
#     if ei % 2 == 0:
#         print(ei, end=" ")

# PROBLEM 3

# Ask the Soldier for their name and rank using input()
# name = input("Whats your name? \n")
# rank = input("Whats your Rank? \n")
# # Ask how many pushups they completed and how long their 2-mile run took in minutes
# push_ups = int(input("How many pushups were completed? \n"))
# run_distance = 2 # miles
# run_time = float(input("How many minutes did it take to complete the 2-mile? \n"))


# #print a formatted after-action report with their name, rank, and both scores. 
# print("***** ACFT AFTER-ACTION REPORT *****")
# print(f"*** Soldier: {rank} {name} ***")
# print(f"*** Push-ups completed: {push_ups} ***")
# print(f"*** Run Time:  {run_time} ***")
# #print the soldiers average pace per mile for the run
# pace = run_time / run_distance
# print(f"Your average pace was {pace}, per mile.")

# PROBLEM 4

# Road Trip Fuel Calculator
# ask the user for the distance of their trip in miles
distance_of_trip = float(input("What is the distance of your trip in miles?  \n"))
# as the user for their cars fuel efficiency in miles per gallon
mpg = float(input("What is your vehicles average miles per gallon? \n"))
# ask for the current price of gas per gallon in dollars
price_of_gas = float(input("What is the current cost of gas per gallon?  \n"))

#ask for the size of gas tank, how many gallons of fuel does it store?
gas_tank_size = float(input("How many gallons does your fuel tank hold? \n"))

#calculate the number of gallons needed (rounded 2 decimal places)
gallons_needed = round((distance_of_trip / mpg), 2)

# calculate the total fuel cost (rounded 2 decimal places)
fuel_cost = round((gallons_needed * price_of_gas), 2)

# calculate how many times you will need to refuel to complete the trip
gallons_per_tank = gallons_needed / gas_tank_size
refuel = int(gallons_per_tank)
if gallons_per_tank > refuel:
    refuel = refuel + 1

print("--- ROAD TRIP FUEL ESTIMATE ---")
print(f"Distance:    {distance_of_trip}")
print(f"Fuel efficiency:    {mpg}")
print(f"Gas price:  ${price_of_gas} / gallon \n")
print(f"Gallons needed: {gallons_needed}")
print(f"Total fuel cost:    ${fuel_cost}")
print(f"You will need to refuel {refuel} times during this trip.")
