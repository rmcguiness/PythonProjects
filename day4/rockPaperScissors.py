import random 
done = False
while done == False :
    user_choice = input("Enter 1 for Rock, 2 for paper, 3 for Scissors, or X to exit game: \n")
    computer = random.randint(0,2)

    if user_choice == "X" or user_choice == "x":
        done = True
        break
    elif user_choice == "1" :
        if computer == 0 :
            print("Tie! Computer played rock too.")
        elif computer == 1:
            print("You Lose! Computer played Paper.")
        elif computer == 2:
            print("Winner! Computer played Scissors.")
    elif user_choice == "2":
        if computer == 0 :
            print("Winner! Computer played Rock.")
        elif computer == 1:
            print("Tie! Computer played Paper too.")
        elif computer == 2:
            print("You Lose! Computer played Scissors.")
    elif user_choice == "3":
        if computer == 0 :
            print("You Lose! Computer played Rock.")
        elif computer == 1:
            print("Winner! Computer played Paper.")
        elif computer == 2:
            print("Tie! Computer played Scissors too.")
    else:
        print("Input error please try again")