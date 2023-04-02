import random

people = list(input("Input the names of all people playing: \n").split(', '))

# rand = random.randint(0, len(people)-1)
# print(f"{people[rand]} has to pay the bill")

person_who_pays = random.choice(people)
print(f"{person_who_pays} has to pay the bill")