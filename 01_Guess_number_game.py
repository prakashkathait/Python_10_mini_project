import random 
def guessnumber():
    ran_number = random.randint(1,10)
    attempts = 0
    guessed_number = None 
    
    print("Welcome to the guessing Game!!")
    print("I have choosen a number within range now its your turn!!")

    while guessed_number!= ran_number:
        guessed_number = int(input("Enter the number in the range of 1 to 10:"))
        attempts += 1 

        if guessed_number > ran_number:
            print("Too high!!")
        elif guessed_number < ran_number:
            print("Low!!")
        else:
            print(f'Horray!! you guessed it right!!! in{attempts} attempts.')

guessnumber()


