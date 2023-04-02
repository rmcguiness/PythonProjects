height_list = input('Input the list of heights you want to find the average of: \n').split()
total = 0
count = 0 
for height in  height_list:
    total += int(height)
    count += 1

average_height = round(total / count)

print(f'The average height is {average_height}')