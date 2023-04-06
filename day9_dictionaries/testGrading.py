score_dict = {}
grade_dict = {}
names = input('Type the names of all the students: \n').split(',')
for name in names:
    score_dict[name] = float(input(f'Input score that {name} recieved: \n'))

for key, value in score_dict.items():
    if value > 90 and value <= 100:
        grade_dict[key] = 'A'
    elif value > 80 : 
        grade_dict[key] = 'B'
    elif value > 70:
        grade_dict[key] = 'C'
    elif value > 65:
        grade_dict[key] = 'D'
    elif value > 0:
        grade_dict[key] = 'F'
    else:
        grade_dict[key] = 'Invalid Score'

for name in names:
    print(f'{name} scored {score_dict[name]} and received grade {grade_dict[name]}')

