# def say_hello(username):
#   print(f"hello {username}")


# say_hello("John")

# def add(a, b):
#   print(a + b)

# add(1, 2)


# number guessing game
import random

def number_guessing_game():
  number_to_guess = random.randint(1, 3)
  user_guess = int(input("Enter a number between 1 and 3: "))

  if user_guess == number_to_guess:
    print("You guessed the number!")
    number_to_guess = random.randint(1, 3)

  if user_guess == number_to_guess:
    print("You guessed the number!")
  elif user_guess < number_to_guess:
    print("Too low! the number is", number_to_guess)
  else:
    print("Too high! the number is", number_to_guess)

number_guessing_game()
