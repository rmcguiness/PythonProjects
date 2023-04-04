import random
import hangManStages
import hangManWords

word_list = hangManWords.word_list
stages = hangManStages.stages
random_word = random.choice(word_list)

display = ["_" for i in range(len(random_word))]
alive = True
lives = 6
guessed = []
while alive:
    index = 0
    print(' '.join(display))
    print(stages[lives])
    if not len(guessed) == 0:
        print(f"Previous guesses: \n {' '.join(guessed)}")
    guess = input("Guess a letter: ").lower()
    correct = False
    for letter in random_word:
        if guess == letter and letter not in guessed:
            display[index] = letter
            correct = True
        index += 1
    guessed.append(guess)
    if not correct:
        lives -= 1
    if "_" not in display:
        break
    if lives == 0:
        alive = False

if "_" in display:
    print("YOU LOSE")
else:
    print("YOU WIN")