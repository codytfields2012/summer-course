# Write a function 'pizzas_needed(people, slices_per_person, slices_per_pizza) that calculates and returns how many whole pizzas to order 
# always round up - you never want to run short!


# Write another function leftover_slices(people, slices_per_person, slices_per_pizza) that returns how many slices will be leftover.

# Use input statements to ask how many guests, slices per person, and slices per pizza
# using your user defined functions, print the PARTY SUMMARY 

# def pizza_party():
    
#     slices_per_pizza = int(input("How many slices per pizza?  \n"))
#     slices_per_person = int(input("How many slices of pizza are you allocating per person? \n"))
#     people = int(input("How many guests will be attending the Pizza party?  \n "))
#     print("=====*PIZZA PARTY PLANNER*=====")
#     print(f"Guests invited:  {people}")
#     print(f"Pizza slices per person:  {slices_per_person}")
#     print(f"Slices per pie:  {slices_per_pizza}")

#     print("=====*PARTY SUMMARY*=====")
#     slices_needed = people * slices_per_person
#     pizzas_needed = slices_needed / slices_per_pizza
#     total_pizzas = int(pizzas_needed)
    
    
#     if pizzas_needed > total_pizzas:
#         total_pizzas = total_pizzas + 1
#     total_slices = total_pizzas * slices_per_pizza
#     leftovers = total_slices - slices_needed
#     print(f"Guests:  {people}")
#     print(f"Pizzas to order:  {total_pizzas}")
#     print(f"Total slices:  {total_slices}")
#     print(f"Leftover slices:  {leftovers}")
        
# pizza_party()


## PROBLEM 2 ###
## Write a simulation that tracks O2 levels and triggers alerts. 

# def o2_status(level):
#     if level < 15:
#         return "CRITICAL"
#     elif level < 19:
#         return "LOW"
#     elif level < 24:
#         return "NORMAL"
#     else:
#         return "HIGH"

# ### STEP 2 ###
# ## USE A 'for' LOOP TO PROCESS EACH READING, CALL YOUR FUNCTION, AND PRINT THE HOUR AND STATUS


# readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21] # creates a variable named "readings", it holds a 'list' of 12 numbers, this variable keeps track of these numbers
# # Counting hours per category - a new tool, the dictionary
# # you need to count how many hours land in each category. A clean way to do this is a 'dictionary' - think of it as a set of labeled boxes, one per category, each holding a running count:
# counts = {"CRITICAL": 0, "LOW": 0, "NORMAL": 0, "HIGH": 0}
# # This creates 4 "boxes", all starting at 0. Later, counts["LOW"] += 1 means "look up the box labeled LOW, add 1 to whatever's inside of it"
# # (+= is shorthand for 'counts["LOW"] = counts["LOW"] + 1 - same idea as total = total + number from way earlier.)

# # for, this keyward tells python "i'm about to start a loop"
# # in, this keyword connects the variable name to the collection you're looping over. 
# # enumerate(), is a function that gives you both the bosition (index) and the value as you loop - instead of just the value like a normal for loop
# # enumerate(), doest create text at all, it takes a list, for each item, hands back a pair: (position, value)
# for hour, reading in enumerate(readings, start=1): # enumerate(readings, start=1) - takes the readings list and converts it into a list of pairs: (1, 21), (2, 20)....etc
#     #hour, reading- two variable names we chose. On each pass through the loop, python takes the next pair from enumerate() and splits it into these two variables:
#     #hour = the counter (1, then 2, then 3...) 
#     #reading = the actual list value (21, then 20, then 19...)
#     status = o2_status(reading) # calls your function onces per loop pass, gets back one of the 4 category strings, and stores it. 
#     print(f"Hour {hour:2}: {reading}% - {status}") # {hour: 2} inside the f-string is a small formatting trick - the :2 means "pad this number to take up at least 2 characters"
#                                                    # so 1 prints as " 1" and lines up neatly under 12. Purely cosmetic, doesnt change the value
                                                   

#     if status == "CRITICAL": # a normal conditional check after printing the main line. since its not elif/else, it doesnt interfere with anything else - it just optionally -
#         print("*** ALERT: TAKE ACTION IMMEDIATELY ***")                                                        # adds an extra line when the condition matches.

#     counts[status] += 1 #instead of writing 4 seperate if checks to figure out which counter to bump, you can use the status string directly as the lookup key.
#                         # If status is "LOW", this line does the same thing as "counts["LOW"] += 1"

# print()
# print("=== STATUS SUMMARY ===")
# print(f"NORMAL:    {counts['NORMAL']} hours")
# print(f"LOW:       {counts['LOW']} hours")
# print(f"CRITICAL:  {counts['CRITICAL']} hours")
# print(f"HIGH:      {counts['HIGH']} hour")

# def trend(readings):
#     last_three = readings[-3:]  # This is slicing. Negative indexes count from the end of a list (-1 is the last item, -2 second-to-the-last, etc.).
#                                 # [-3:] means "start 3 from the end, and go to the end" - ie., "give me the last 3 items"
#     if last_three[0] < last_three[1] < last_three[2]: # chain comparison, equivalent to writing last_three[0] < last_three[1] and last_three[1] < last_three[2], but shorter.
#                                                       # "is item 0 less than item 1, and is item 1 less than item 2?" strictly increasing all the way through.
#         return "IMPROVING"
#     elif last_three[0] > last_three[1] > last_three[2]:
#         return "DECLINING"
#     else:
#         return "STABLE"

# test2 = [10,15,21,19,21]
# print(trend(test2))
# test_up = [30,25,17,19,21]
# test_down = [10,15,21,19,17]
# print(trend(test_up))
# print(trend(test_down))


###PROBLEM 3###

# import random
# attack_range = [1, 101] # this as (min, max) bounds
# ## write a function 'attack(defender_hp, damage)' that subtracts damage from defender HP and returns the new HP (minimum 0)
# def attack(defender_hp: int, damage: int):
#     return max(0, defender_hp - damage) #max() a built in python function that takes two (or more) values and returns whichever is larger

# def is_alive(hp):
#     return hp > 0 # ">" is an operator that always produces a boolean, so this produces a True or False immediately

# def critical_hit(damage):
#     if random.randint(1, 10) <= 2:
#         return damage * 2, True

#     else:
#         return damage, False

# hero_hp = 100
# monster_hp = 100
# round_num = 1
# while is_alive(hero_hp) and is_alive(monster_hp):
#     hero_damage = random.randint(attack_range[0], attack_range[1])
#     hero_damage, crit = critical_hit(hero_damage)
#     if crit:
#         print("*** CRITICAL HIT! ***")
#     monster_hp = attack(monster_hp, hero_damage)

#     if is_alive(monster_hp):
#         monster_damage = random.randint(attack_range[0], attack_range[1])
#         hero_hp = attack(hero_hp, monster_damage)

#     print(f" Round {round_num}\n Monster Attack = {monster_damage}\nHero Attack = {hero_damage}\nHero HP = {hero_hp}\n Monster HP = {monster_hp}")
#     round_num += 1

# if is_alive(hero_hp) and not is_alive(monster_hp):
#     print("The hero wins!")

# elif is_alive(monster_hp) and not is_alive(hero_hp):
#     print("The hero falls!")

# else:
#     print("DRAW")


### problem 4 ###

# def check_fitness(score):
#     return score >= 70

# ranks = ['Corporal', 'Sergeant', 'Lieutenant']
# def check_rank(rank):
#     return rank in ranks

# def check_service_years(years):
#     return years >= 2

# name = input("Enter Soldier's Name:  \n")
# s_rank = input("Enter Soldier's Rank: \n")
# fitness_score = int(input(f"Enter {s_rank} {name}'s fitness score: \n"))
# years_of_service = int(input(f"Enter {s_rank} {name}'s current years of service: \n"))

# # 'checks' is a list of tuples - each pairing a label like "rank" with the true/false result of calling that check function.
# checks = [("Rank", check_rank(s_rank)), ("Fitness", check_fitness(fitness_score)), ("Years of Service", check_service_years(years_of_service))]

# results = []
# # the for loop then walks through each tuple, unpacking it into 'check_name' and 'result', and appends just the boolean into a separate 'results' list.
# for check_name, result in checks:
#     results.append(result)

# # all() is a built-in function that returns 'True' only if every item in the list is 'True' - the moment it finds one 'False', the whole thing short-circuits to 'False'. 
# # thats a clean way to express "all three checks must pass", instead of writing 'check1 and check2 and check3' by hand
# cleared = all(results)

# print(f"\n --- Clearance Report for {s_rank} {name} ---")

# # this loops over 'checks' agagin (this time using both the name and result) to print a line per check, coverting the raw boolean into a readable "PASS" or "FAIL" label. 
# # Do your fitness score and years-of-service thresholds match what I assumed (70+ and 2+)

# for check_name, result in checks:
#     status = "Pass" if result else "FAIL"
#     print(f"{check_name}: {status}")

# if cleared:
#     print(f"\nFinal Decision: {s_rank} {name} is CLEARED.")
# else:
#     print(f"\nFinal Decision: {s_rank} {name} is NOT CLEARED.")



### PROBLEM 5 ###

## 
