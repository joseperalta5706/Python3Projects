import math, random

# initialize counter
counter = 0

while counter < 3:
  # whlle counter less than 3
  # do some work

  # generate random numbers
  num1 = random.randint(0, 10)
  num2 = random.randint(0, 10)
  
  operater_list = ['+', '-']
  random_number = random.randint(0, 10)
  op = operater_list[random_number % 2]
  # show a problem with those numbers:
  my_string = str(num1) + op + str(num2)
  print(my_string)
  
  # increase i to next problem
  counter += 1

  my_answer1 = eval(my_string)
  equation1 = int(input(""))
  
  if equation1 == my_answer1:
    print("Good work - your answer is correct!")
  else:
    print("Nice job, but a better answer is " + str(my_answer1))
    
