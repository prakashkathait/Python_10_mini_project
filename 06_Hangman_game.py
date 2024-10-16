'''6. Hangman Game

Concepts: Loops, Strings, Lists
Description: A word-guessing game where the player tries to guess 
the word by suggesting letters.
Track the player’s incorrect guesses and limit the number of attempts.'''

import random 

words = ['prakash','singh','kathait']

def choose_word():
    #function will select the random word from the list
    return random.choice(words)

def display_word(word,correct_guesses):
    '''function will display the word with guessed letters and underscores'''
    display = [letter if letter in correct_guesses else '_' for letter in word]
    return ' '.join(display)

def play_game():
    print("Welcome to Hangman!")

    #choose a random word
    word = choose_word()
    attempts = 7 #chances given 
    correct_guesses =[] #stores correct guesses
    incorrect_guesses =[] #stores incorrect guesses

    while attempts > 0:
        print(f"\nWord to guess: {display_word(word,correct_guesses)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input! Please guess a single letter.")
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You have already guessed that letter. Try again!")
            continue

        if guess in word:
            correct_guesses.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.append(guess)
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        
        #check if the player has guessed the entire word correctly 

        if all(letter in correct_guesses for letter in word):
            print("Congratulations!! You've guessed the word '{word}' !")
            break
    else:
        print(f"\nGame over! You've run out of attempts. The word was '{word}'.")
    
play_game()
            






