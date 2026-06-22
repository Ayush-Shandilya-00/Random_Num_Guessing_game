# This is a number guessing game between user and computer

# Import Random module
import random
random_number = random.randint(1,100)
attempt =0
while True: # While condition for running loop until the condition becomes false
    guess= int(input("Guess the number between 1 and 100: "))
    attempt+=1
    if guess > 100:
        print("Enter number between 1 and 100!")
        break
    elif guess < random_number:
        print("Too Low!")
    elif guess > random_number:
        print("Too High!")
    elif guess == random_number:
        print(f"Correct guess in {attempt} attempts!")
        break
    else:
     print("Guess is Invalid")
