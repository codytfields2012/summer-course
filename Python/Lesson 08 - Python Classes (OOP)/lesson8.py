
## Class Objects
# class MyClass():  #Attributes - stored data
#     my_name = 'Milo'

#     def meow(self):  # Methods - what the class can do
#         print(f'{self.my_name} meows') # 'self.' is used to call your attributes

# milo = MyClass()   # Objects are instantiations of classes
# milo.my_name
# milo.meow()


### DEMO work ###
# print(dir(list))   # dir funtion, research

### instructor code
import random

class Pokemon():
    #attributes
    def __init__(self, name, species, health, level, speed, gender, strength, defense, \
                 spatk, spdef, types, moves ) -> None:
        pass
        self.name = name
        self.level = level
        self.health = health
        self.speed = speed



    #health
    #level
    #speed
    #gender
    #strength
    #defense
    #sp atk
    #sp def
    #types
    #moves
    #evolution requirements

    #things it can do (methods):
    def level_up(self):
        self.health += random.randint(5, 10)
        self.name += random.randint(5, 10)
        self.level += random.randint(5, 10)
        self.speed += random.randint(5, 10)


        if all(self.evolution_requirements):
            self.evolve()

#level up test

    #attack
    # - misses
    # - status effect
    #buff
    #defend
    #evolve
    #
    pass

class type():
    pass

class trainer():
    pass



