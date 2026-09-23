import random
import sys

guesses = 0

for i in range (1000):

  n = random.randint(1, 1000)

  response = input("Please guess a number! Type 'bye' or 'exit' to quit the program ")

  while True: 

    if response == "bye":
      print("Goodbye!")
      sys.exit()

    if response == "exit":
      print("Goodbye!")
      sys.exit()

    if int(response) > n:
      print("Too high!")
      response = input("Please guess a number! Type 'bye' or 'exit' to quit the program ")
      guesses += 1

    if int(response) < n:
      print("Too low!")
      response = input("Please guess a number! Type 'bye' or 'exit' to quit the program ")
      guesses += 1

    if int(response) == n:
      print("Congratulations! You guessed the number!")
      print("It took you", guesses, "guesses")
      guesses = 1
      break