# look up what all these commands actually do
[]
type([])
my_list = [1] * 5
my_list + [6, 7, 8, 9]
my_list.extend([6, 7, 8, 9])
second_list = [10, 20, 30]
my_list.append(second_list)
my_list[-1]
my_list.append("hello")
my_list.extend(list("goodbye"))
del my_list[0:7]
del my_list[0:2]

second_list[1] = 25
print(my_list)
print(second_list)


# for index in range(len(my_list)):
#     del my_list[index]   ## be careful deleting shit, python doesnt like it because you're changing the index in the list

del my_list
del second_list

my_list = [1, 2, 3, 4, 5]
second_list = [10, 20, 30]
my_list.append(second_list)
print(my_list)
copy_list = my_list[:]
print(copy_list)
copy_list[2] = 30
print(copy_list)
print(my_list)
my_list[-1][1] = 75
print(my_list)
print(copy_list)
second_list[1] = 100
print(second_list)
print(my_list)
print(copy_list)
import copy
copy_list = copy.deepcopy(my_list)
print(copy_list)
my_list[2] = 1000
print(my_list)
print(copy_list)