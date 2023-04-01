print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_right = input('There is a fork in the road which direction do you choose to go "left" or "right"?\n').lower()
if left_right == 'right':
    print('Wrong path wild bear, you die. Sorry...\n')
    exit()
elif left_right != 'left':
    print('Learn to spell. You died\n')
    exit()

swim_wait = input('You reached the end of the road and see the ocean. What do you do, "swim" or "wait"?\n').lower()
if swim_wait == 'swim':
    print('The ocean is dangerous sharks kill you bad choice.\n')
    exit()
elif swim_wait != 'wait':
    print('Learn to spell. You died\n')
    exit()

door = input('A boat comes by in brings you to a secret cove where three doors are etched into the side of a cliff. Which door do you choose? Blue, Yellow, or Red\n').lower()

if door == 'yellow':
    print('Congratulations you found the treasure. There was a 100 million dollars worth of gold in it. You retire early and live a long fulfilling life.\n')
    exit()
else:
    color = door.upper()
    print(f'{color}! Really?! Dead. You die now.\n')