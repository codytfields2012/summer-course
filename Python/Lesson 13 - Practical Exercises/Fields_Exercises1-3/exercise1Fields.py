# ask the user if they would like to input either "Miles above Mars" or "Kilometers above Mars".
miles_or_kilometers = input(
    'Miles above Mars? or Kilometers above Mars?\n Type "M" for miles, or "K" for kilometers:\n'
).lower()
if miles_or_kilometers != "k" or "m":
    print("Invalid input")


# If they choose Miles, the program should then prompt them to enter the number of miles
if miles_or_kilometers == "m":
    num_of_miles = int(input("Enter the number of miles:\n"))
    miles_to_yards = num_of_miles * 1760
    miles_to_feet = num_of_miles * 5280
    miles_to_inches = num_of_miles * 63360
    print(
        f"Miles: {num_of_miles}\nYards: {miles_to_yards}\nFeet: {miles_to_feet}\nInches: {miles_to_inches}"
    )
if miles_or_kilometers == "k":
    num_of_kilometers = int(input("Enter the number of kilometers:\n"))
    km_to_meters = num_of_kilometers * 1000
    km_to_centimeters = num_of_kilometers * 100000
    km_to_millimeters = num_of_kilometers * 1000000
    print(
        f"Kilometers: {num_of_kilometers}\nMeters: {km_to_meters}\nCentimeters: {km_to_centimeters}\nMillimeters: {km_to_millimeters}"
    )
# The program should display the number of yards, feet, and inches that are in that many miles.
# 1 mile = 1760 yards
# 1 mile = 5280 feet
# 1 mile = 63360 inches
