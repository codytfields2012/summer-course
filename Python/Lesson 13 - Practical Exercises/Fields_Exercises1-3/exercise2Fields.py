def triangle_area(base, height):
    return 0.5 * base * height


# Function for square area
def square_area(side):
    return side * side


# Inputs
t_base = float(input("Enter the base of the Triangle:\n"))
t_height = float(input("Enter the height of the triangle:\n"))
s_side = float(input("Enter the side length of the square:\n"))

# Call/calculate areas
area_tri = triangle_area(t_base, t_height)
area_sq = square_area(s_side)

# Results
print(f"Triangle area:\n{area_tri}")
print(f"Square area:\n{area_sq}")
if area_tri > area_sq:
    print("Triangle Pizza's the way to go!")
else:
    print("Square is the way to go.")
