import random

# Define a class named spacecraft
# name, fuel_level, fuel_efficiency
class spacecraft():
    def __init__(self, name, fuel_level, fuel_efficiency):
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency
        self.max_fuel = 100_000

#create a method to add fuel
    def add_fuel(self, amount: float)-> None: #when you add fuel its probably an amount or quanity that you're adding
        self.fuel_level = min(self.max_fuel, self.fuel_level + amount)
        self.fuel_level = max(self.fuel_level, 0)

# create a method to calculate fuel required for a given distance
    def fuel_needed(self, distance: float) -> float: #"given distance", means "distance" should be an arguement
        return distance / self.fuel_efficiency

# check if enough fuel is available to travel that distance
    def travel_distance(self, distance: float)-> bool:

        # figure out how much fuel this trip will use.
        fuel_required = self.fuel_needed(distance)

        # check if the spacecraft has enough fuel
        if fuel_required <= self.fuel_level:

            # If it does, subtract the fuel used. 
            self.fuel_level -= fuel_required

            # Tell the caller the trip was successful.
            return True
        
        # Otherwise, there wasn't enough fuel
        return False

    
# launch the spacecraft and deduct fuel if successful
    def launch(self, distance)-> bool:
       if self.travel_distance(distance):
           self.fuel_level -= self.fuel_needed(distance)
           print(f"Launched {self.name} {distance} killometers.")
        else:
           print(f"{self.name} doesnt have enough fuel to travel {distance}")
    
sp1 = spacecraft("vostok 1", 250, 1.5)
sp2 = spacecraft("voyager1", 400, 2.0)
sp1.launch(400)
sp2.launch(200)


