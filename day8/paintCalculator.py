def paint_calc (height, width, coverage):
    return int(height * width / coverage)

wall_h = int(input("Height of wall: \n"))
wall_w = int(input("Width of wall: \n"))

coverage = 5
print(f"You will need {paint_calc(height = wall_h, width = wall_w, coverage = coverage)} cans of paint")