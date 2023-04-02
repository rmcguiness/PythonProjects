score_list = input("Input list of scores: \n").split()
highest = 0
num_scores = 0
total = 0

for score in score_list:
    number = int(score)
    if number > highest:
        highest = number
    
    num_scores += 1
    total += number

print (f"The highest score is:{highest}\nThe average is: {round(total/num_scores)}")