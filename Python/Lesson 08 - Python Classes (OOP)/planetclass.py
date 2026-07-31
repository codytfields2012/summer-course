

class Planet():
    def __init__(self, name, coordinates, danger, resources, atmosphere):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self)-> str:
        return f" Planet {self.name}\nlocated here: {self.coordinates}\n \
            danger level: {self.danger}\n resources available: {self.resources}\n atmosphere: {self.atmosphere}"

    def distance_calc(self, other_planet):
        return abs(self.coordinates - other_planet.coordinates) #abs returns absolute values, no negative numbers

earth = Planet("Earth", 10, 2, 100, "Breathable")
mars = Planet("Mars", 8, 5, 65, "Thin")

print(earth.distance_calc(mars))