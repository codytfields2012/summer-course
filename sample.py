"""This is a definition of what this module (file) does"""

TEST = "3"


def my_func(func_input: str) -> str:
    """this is what my func does"""
    print(type(func_input))
    user_entered = input("input here")
    return user_entered


print(my_func(TEST))
