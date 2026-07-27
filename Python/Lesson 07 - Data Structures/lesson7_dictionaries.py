# my_dict = {}
# my_dict['a'] = 1
# print(my_dict)
# my_dict['a'] = 2
# print(my_dict)
# my_dict['a'] = 1
# my_dict['b'] = 2
# my_dict['c'] = [3, 4, 5]
# print(my_dict)
# for key in my_dict.keys():
#     print(key)


# for key in my_dict.keys():
#     print(key, my_dict[key])

# for key, value in my_dict.items():
#     print(key, value)

# for index, (key, value) in enumerate(my_dict.items()):
#     value = index
#     print(value)


# for index, key in enumerate(my_dict.keys()):
#     my_dict[key] = index
#     print(my_dict)

# my_dict.get('d')
# my_dict.get('d', 5)
# print(my_dict.get('d'))

# my_dict.update([('d', 5)])
# print(my_dict)

## Hands on #2- Dictionary

## You are building a simple database for a military unit. Each Soldier has a name, rank, and years of service.
## Your job is to store this information and write a function that lets the commanding officer quickly look up any
## Soldiers details by their last name. 

## Create a dictionary called unit where each key is a soldier's last name and each value is another dictionary containing
## rank and years_of_service

## populate it with at least 5 Soldiers

## Write a function lookup_soldier(unit, last_name) that takes the dictionary and a last name and prints the Soldier's full profile,
## or a friendly message if the soldier is not found.

# rank = {"E5": "SGT", "E6": "SSG", "E4": "SPC", "WO1": "W1"}
# years_of_service = 

## instructor code
unit = {}

unit['Hernandez'] = {'rank': 'CPT', 'years_of_service': 8}
unit['Smith'] = {'rank': 'SGT', 'years_of_service': 3}
unit['Fields'] = {'rank': 'CW2', 'years_of_service': 15}
unit['Price'] = {'rank': 'W1', 'years_of_service': 16}
unit['Love'] = {'rank': 'SSG', 'years_of_service': 10}

def lookup_soldier(unit, last_name):
    if last_name in unit:
        rank = unit[last_name]["rank"]
        years_of_service = unit[last_name]["years_of_service"]
        print(f'Found {last_name}')
        print(f'\t Rank: {rank}')
        print(f"\t Years of Service: {years_of_service}")

    else:
        print('Could not find Soldier')

user_input = input("Which Soldier would you like to lookup?  \n")
lookup_soldier(unit, user_input.strip())


## add a line that lets you type the names in all caps or all lowercase