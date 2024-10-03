# Hangman Game
import requests
import art


def play():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    response.raise_for_status()
    word = response.json()[0].lower()
    logo = art.logo
    stages = art.stages
    lives = LIVES = len(stages)
    correct_letters = []
    def word_display():
        display = ""
        for letter in word:
            if letter in correct_letters:
                display += letter
            else:
                display += '_'
        print(f"Word is: {display}")
    def is_correct_guess(guess):
        if guess in correct_letters:
            print("You've already guessed this letter before")
            return
        elif guess in word:
            return True
        else:
            print(f"You entered {guess} which is not in the word, You lost a life.")
            return False
    # Code
    print(logo)
    word_display()
    playing = True
    while playing:
        guess = input("Guess a letter: ").lower()
        guess_state = is_correct_guess(guess)
        if guess_state:
            print("Correct Guess!")
            correct_letters.append(guess)
            word_display()
        elif guess_state == False:
            print(stages[lives - 1])
            lives -= 1
            if lives > 0:
                print(f"You have {lives}/{LIVES} lives remaining")
                word_display()
            else:
                print(f"You Lost!")
                print(f"Word was {word}")
                cont = input("Do you want to play again? y:Yes , n:No ").lower()
                if cont == 'y':
                    print('\n'*50)
                    play()
                else:
                    if cont != 'n':
                        print("Invalid Input!\nGame is closing.")
                    else:
                        print("Thank You for using our game!\nGoodBye.")
                    exit()

play()