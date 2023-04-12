import random
print('Welcome to the Number Guessing Game!')
def game():
    number = random.randint(0,100)
    print('Im thinking of a number between 0 and 100.')
    difficulty = input('Choose difficulty. Type "easy" or "hard":').lower()
    guesses = 0
    if difficulty == "easy":
        guesses = 10
    elif difficulty == "hard":
        guesses = 5
    else:
        print('Invalid input try again')
        game()
    
    for i in range(1,guesses):
        print(f'You have {guesses-i+1} guesses remaining.')
        guess = int(input('Make a guess: '))
        if guess == number:
            print("Congrats you win!!!")
            break
        elif guess > number:
            print('Too High')
        elif guess < number:
            print('Too Low')
        
        if i > guesses:
            print('You lose!')
    play_again = input('Do you want to play again?(y/n)').lower()
    if play_again == 'y':
        game()
    

game()
