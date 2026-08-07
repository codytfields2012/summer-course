# def factorial(n):
#     if n == 1 or n == 0:
#         print("best case reached")
#         return 1
#     print(f"computing factorial {n-1}")
#     return n * factorial(n-1)

# factorial(7)


# def palindrome(input_str):
#     if input_str == "":
#         return True
#     if len(input_str) == 1:
#         return True

#     if input_str[0] != input_str[-1]:
#         return False



#     print(f"computing {input_str[1:-1]}") # input_str[1:-1], is slicing [start:stop]
#     result = palindrome(input_str[1:-1]) # 1 means start at index 1, -1 means stop at -1, negative indexing counts from the end
#     print(f"received {result} for {input_str[1:-1]}") # so -1 refers to the last character, since stop is exclusive the last character gets left out too
#     return result
# print(palindrome('level'))
# print(palindrome('3335'))


### CALCULATE THE SUM OF A LIST OF NUMBERS USING RECURSION
# my_numbers = [2, 4, 6, 8, 10] #step 1, create a list
# def sum_list(num_list: list[int]) -> int: 
#     #step 2, build the 'BASE CASE'
#     if len(num_list) == 0:
#         return 0
#     # step 3, figure out the recursive case, 'what do you do otherwise?'
#     return num_list[0] + my_numbers()


## instructor code
def sum_list(input_list):
    #base case
    if len(input_list) == 0:
        return 0
    #recursive step
    print(f'evaluating {input_list}')
    result = input_list[0] + sum_list(input_list[1:])
    print(f'received {result} for {input_list}')
    return result

print(sum_list([]))
print(sum_list([1]))
print(sum_list([1, 2, 3]))