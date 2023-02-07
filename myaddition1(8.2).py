import math, random
# function is set up
def additionProblem(topNumber, bottomNumber):
  print("\n\n\n     ", topNumber, "+", bottomNumber, "= ", end = "") 
# user inputs answer to randomly generated problems
  userAnswer = int(input())
  theAnswer = topNumber + bottomNumber 
# check the answer
  if theAnswer == userAnswer: 
    print("      Correct!") 
  else:
    print("      Very good, but a better answer is", theAnswer)
# additionProblem ends here

# 'topNumber' and 'bottomNumber' set to random.randint to generate random integers between 1-10 inclusively
additionProblem(random.randint(1,10), random.randint(1,10))
additionProblem(random.randint(1,10), random.randint(1,10))
additionProblem(random.randint(1,10), random.randint(1,10))
additionProblem(random.randint(1,10), random.randint(1,10))
additionProblem(random.randint(1,10), random.randint(1,10))
