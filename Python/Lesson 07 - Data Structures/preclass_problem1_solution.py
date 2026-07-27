
with open("preclass_problem1_data.txt", "r") as file:
    values = [float(line.strip()) for line in file]

result = sum(sorted(values, reverse=True)[:5]) / 10
print(result)


