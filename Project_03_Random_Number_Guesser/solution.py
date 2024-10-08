import random

num = random.randrange(0,100)

number_guessed = False

while not number_guessed:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess == num:
        print(f"Hurraaa you won! {guess} was the corret guess.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y": 
            num = random.randrange(0,100)
        else:
            number_guessed = True
    elif guess > num:
        print("Go lower!")
    else:
        print("Go higher!")