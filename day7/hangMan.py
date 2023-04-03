import random
word_list = ['ardvark' , 'baboon', 'camel']

random_word = random.choice(word_list)
print(f'The word is {random_word}')
display = ["_" for i in range(len(random_word))]
alive = True
lives = 10
while alive:
    index = 0
    print(display)
    guess = input("Guess a letter: ").lower()
    correct = False
    for letter in random_word:
        if guess == letter:
            display[index] = letter
            correct = True
        index += 1

    if not correct:
        lives -= 1

    if lives == 0:
        alive = False

if "_" in display:
    print("YOU LOSE")
else:
    print("YOU WIN")