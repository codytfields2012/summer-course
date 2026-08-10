# Gain remote access of Mission Control (log into VM)

# Solve telemetry systems issues (Python problem 1)

#Recalculate food resources (Python problem 2)

#Launch emergency comms rocket (python problem 3)

# HTTP Response to a request at 20.127.202.175 port 8000.
curl.exe 20.127.202.175:8000
============================================================
  BASE ONE // MISSION CONTROL // EMERGENCY UPLINK
============================================================

SIGNAL ACQUIRED. Carrier lock established.

Auth subsystem is running on backup power. Credential store
was lost in the X9.3 event, but the challenge handler is
still live and will accept a manual identity assertion.

Transmit your credentials as HTTP request headers:

    X-Username: "chief.engineer"
    X-Password: "ares-vallis-7"

Callsign on file for this rotation: chief.engineer
Access code is printed on your pre-deployment briefing card.

Awaiting authentication.

-- Cmdr. Weiss, Base One


# Test this connection with a simple HTTP request without authentication headers. 
curl.exe -H "X-Username: chief.engineer" -H "X-Password: ares-vallis-7"  20.127.202.175:8000
============================================================
  ACCESS GRANTED // WELCOME BACK, CHIEF ENGINEER
============================================================

Mission Control is yours. Remote session credentials:

    HOST:     20.127.202.175
    USERNAME: chief.tech
    PASSWORD: 1000-souls-aboard

Connect via SSH and begin restoration:

    ssh chief.tech@20.127.202.175

Your task queue:

  [1] Telemetry systems      -> Python Problem 1
Okay, great.  You found the telemetry file.

As the colonists approach Mars, you need to help them calculate their telemetry data.  To do this, you are going to
write a python program.  The program should ask the user if they would like to input either "Miles above Mars" or
"Kilometers above Mars".  If they choose "Miles above Mars", the program should then prompt them to enter the number
of miles.  Then the program should display the number of yards, feet, and inches that are in that many miles.
If the user chooses "Kilometers above Mars", the program should then prompt them to enter the number of kilometers.
Then the program should display the number of meters, centimeters, and millimeters that are in that many kilometers.

#ask the user if they would like to input either "Miles above Mars" or "Kilometers above Mars".
miles_or_kilometers = input("Miles above Mars? or Kilometers above Mars?\n Type \"M\" for miles, or \"K\" for kilometers:\n").lower()
if miles_or_kilometers != "k" or "m":
    print("Invalid input")
miles_to_yards = num_of_miles * 1760
miles_to_feet = num_of_miles * 5280
miles_to_inches = num_of_miles * 63360
km_to_meters = num_of_kilometers * 1000
km_to_centimeters = num_of_kilometers * 100000
km_to_millimeters = num_of_kilometers * 1000000
# If they choose Miles, the program should then prompt them to enter the number of miles
if miles_or_kilometers == "m":
   num_of_miles = int(input("Enter the number of miles:\n"))
   print(f"Miles: {num_of_miles}\nYards: {miles_to_yards}\nFeet: {miles_to_feet}\nInches: {miles_to_inches}")
if miles_or_kilometers == "k":
   num_of_kilometers = int(input("Enter the number of kilometers:\n"))
   print(f"Kilometers: {num_of_kilometers}\nMeters: {km_to_meters}\nCentimeters: {km_to_centimeters}\nMillimeters: {km_to_millimeters}")
# The program should display the number of yards, feet, and inches that are in that many miles.
# 1 mile = 1760 yards
# 1 mile = 5280 feet
# 1 mile = 63360 inches




Once you solve this problem, proceed to find the resource file in the file system.

  [2] Food resource recalc   -> Python Problem 2
The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

As the Chief Engineer, you decide to write a Python Script to figure out which Automatron is most efficient.  Once we avert total disaster and save all 1000 lives on board of the incoming shuttle,
we will want to welcome them with some warm, Martian pizza after all.

Write a Python Script to determine which of these are the best deal.  Use functions to calculate the areas of the pizzas.

# Function for triangle area 
def triangle_area(base, height):
   return 0.5 * base * height

# Function for square area
def square_area(side):
   return side * side

# Inputs
t_base = float(input("Enter the base of the Triangle:\n"))
t_height = float(input("Enter the height of the triangle:\n"))
s_side = float(input("Enter the side length of the square:\n"))

# Call/calculate areas
area_tri = triangle_area(t_base, t_height)
area_sq = square_area(s_side)

# Results
print(f"Triangle area:\n{area_tri}")
print(f"Square area:\n{area_sq}")

Once you have completed this, navigate to root directory to find Problem 3.

  [3] Emergency comms rocket -> Python Problem 3
Our inbound colonists rapidly approach Mars atmosphere, but we still do not have reliable comms with them.
We must rapidly launch our spare rocket to establish comms and share the correct telemetry data with them before they smash into Mars!

There's no time to unload the modules that are on the rocket, and we must begin fueling right away.
The problem is, we do not know how much fuel we need.

As you rush to the rocket, you notice a list of all of the modules' mass on board (your python file input).

Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.

As the Chief Engineer, you need to calculate the total fuel requirement.
To find the total fuel requirement, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

Once you solve this problem, issue a pull request with all three of your solutions to the International Space Station (https://github.com/Ryan-L-N/cohort-7-practical.git).
To keep the International Space Station's file system clean, your solutions should be inside of a folder with your last name.

Finally, create a broadcast beacon with Earth to state that the crisis was averted.
To do this, create a VM, host a website with a picture of your choice on the VM, and share the public IP address of your website with the International Space Station.
  [4] Submit solutions       -> pull request
  [5] Broadcast beacon       -> host a site from your VM

72 hours on the clock. Move.

-- Cmdr. Weiss, Base One
# Once you have those, send a simple HTTP request with these authentication headers to get the login information for mission control.

