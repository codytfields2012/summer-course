# a tuple cannot be changed after its created. 
# cant append, extend, replace, delete (immutable)

# # creating tuples
# #empty tuple
# my_tuple = ()
# my_tuple = tuple()

# #with values
# my_tuple = (1, 2, 3)

# # parentheses are actually optional
# my_tuple = 1, 2, 3

my_tuple = 5, 6, 7
print(my_tuple)
print(my_tuple + (8,))
print(my_tuple)

def my_func():
    return 1, 2, 3
print(my_func())
a, b, c = my_func()
print(a)
print(b)
print(c)
print(a, b, c)