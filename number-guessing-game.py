print("Welcome to the Number Guessing Game!")
print("")
print("")

import random
number = random.randint(1, 10)

while True:
  correct = 0
  if correct == 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if number == guess:
      print("")
      print("")
      print("")
      print("You guessed the correct number!")
      import random
      number = random.randint(1, 10)
      correct = 1
    elif guess < number:
      print("")
      print("")
      print("Your guess is too low. Go higher")
    elif guess > number:
      print("")
      print("")
      print("Your guess is too high. Go lower")
    
    if correct == 1:
      input("Do you want to play again? (Y/N): ")
      if input == "Y":
        print("")
        correct = 0
      if input == "N":
        print("")
        print("Thanks for playing!")
        break