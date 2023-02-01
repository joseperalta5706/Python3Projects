# coin flip program
import random

# function to generate rando # between 1 - 2 INCLUSIVELY
def coin_flip():
  result = (random.randint(1, 2))

  # if the random number is 1 prints heads or it will print tails
  if result == 1:
    print("Heads")
  else:
    print("Tails")

coin_flip()
