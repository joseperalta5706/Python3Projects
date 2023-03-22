import math
# function to check questions to the answers
counter = 0
def ask_questions(q, a):
  global counter 
  if q == a or q == a11 or q == a31:
    counter += 1
    print("Good job, that's right!")
  else:
    print("Sorry that's the wrong answer")


# Users first Q and A 
a1 = "50"
a11 = "fifty"
q1 = input("How many states are there in the U.S?:").lower()
ask_questions(q1, a1 or a11) # function call using the values from q1 and a1


if q1 == a1 or a11 is True:
  print("True")
# Users second Q and A 
a2 = "meter" 
q2 = input("What is longer a yard or a meter?:").lower()
ask_questions(q2, a2) # function call using the values from q2 and a2

# Users third Q and A 
a3 = "george washington"
a31 = "washington"
q3 = input("Who was the first President?:").lower() # function call using the values from q3 and a3
ask_questions(q3, a3)
print("You got " + str(counter)m + " questions right out of 3.")
