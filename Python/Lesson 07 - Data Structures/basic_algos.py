# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


def mut_example(list1, list2, list3):
    if len(list1) > 2: # List 1 is [1, 2, 3], len is 3, so condition is True
        list1 = list1[:2] # creates a NEW list, from [1, 2, 3] to [1, 2]. This doesnt modify a_list
    list2[0] = "hi" # modifying the object itself, before ["a", "b", "c"], after ["hi", "b", "c"]
    list3 = "".join(list2) # join() combines strings together, but strings are immutable, so your assigning a brand-new string to list3


a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
a_str = "do-re-mi"
mut_example(a_list, b_list, a_str)
print(a_list)
print(b_list)
print(a_str)
print(type(a_str))




# Exercise 2

## What's the difference between sort and sorted?
# sort() example
numbers = [4, 2, 8, 1]
numbers.sort()
print(numbers)
# This is called in-place sorting.
# NOTE: sort() changes the list directly, it doesnt make a new list


# sorted() example
numbers = [4, 2, 8, 1]
new_numbers = sorted(numbers)
print(numbers)
print(new_numbers)
# the orginal list stayed the same.
# a new sorted list was created.

## Which one is a list method and which one is a function that works on lists?
# a method belongs to an object, you call it with a dot<.>
numbers.sort() # This means "ask this list to sort itself"

# a function is independent
sorted(numbers) # This means "Here's a list. Please return the sorted version."

## NOTE: use sort() when you no longer need the original order and want to sort the list in its place. 
## NOTE: use sorted() when you want to preserve the original data or when you're working with an iterable that isn't a list.




# Exercise 3

# Write a function that doubles the elements in a list.
def double_list(in_list):
    for index in range(len(in_list)):
        in_list[index] = in_list[index] * 2

# not in place
def double_list_two(in_list):
    return[x * 2 for x in in_list]

# Do you need to return anything here?



# Write a function that doubles the elements in a tuple.
def double_tuple(in_tuple):
    return tuple(x * 2 for x in in_tuple)


# Do you need to return anything here?



# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions
def my_pop(in_list):
    new_val = in_list[-1]
    del in_list[-1]
    return new_val

def my_count(in_list, obj):
    count = 0
    for elem in in_list:
        if obj == elem:
            count += 1
    return count

def my_extend(in_list, other_list):
    for elem in other_list:
        in_list.append(elem)

def my_reverse(in_list):
    reversed = []
    for elem in in_list[::-1]:
        reversed.append(elem)
    return reversed

def my_reverse_two(in_list):
    for index in range(len(in_list) // 2):
        in_list[index], in_list[-index -1] = in_list[-index -1], in_list[index]

def bubble_sort(in_list):
    for start_index in range(len(in_list) - 1):
        left_index = start_index
        for current_index in range(len)
# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions



# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates
def distance(coord_one, coord_two):
    x1, y1 = coord_one
    x2, y2 = coord_two

    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) )


# extension: make it work for more than two dimensions

