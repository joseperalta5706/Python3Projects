import math
# function to check questions to the answers
a1 = "50"
a11 = "fifty"
a2 = "meter" 
a3 = "george washington"   
a31 = "washington"
def ask_questions(a, q):
  if a == q or a == a11 or a == a31:
    print("Good job, that's right!") 
  else:
    print("Sorry that's the wrong answer")
# Users first Q and A 
q1 = input("How many states are there in the U.S?:").lower()
ask_questions(q1, a1) # function call using the values from q1 and a1
# Users second Q and A 
q2 = input("What is longer a yard or a meter?:").lower()
ask_questions(q2, a2) # function call using the values from q2 and a2
# Users third Q and A 
q3 = input("Who was the first President?:").lower() # function call using the values from q3 and a3
ask_questions(q3, a3)
