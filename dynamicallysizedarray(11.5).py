# setup defaults
user_wants_defaults = False
DEFAULT_N = 6
DEFAULT_SCORES = [34, 12, 76, 45, 34, 90]
A_GRADE = 90

# ask the user for somtehing
n = input("how many scores [6]: ")

# if n is empty then use default
if n == "":
  n = DEFAULT_N
  # also set the default flag to True
  user_wants_defaults = True

# read and save the scores
scores = []
min, max = 1000, 0
scoreTotal = 0
any_A_grades = False

for i in range(int(n)):
  if user_wants_defaults:
    scores.append(DEFAULT_SCORES[i])
  else: # the user doesn't want defaults
    user_score = input("Enter a score: ")
    scores.append(user_score)
  # find min and max
  if min > scores[i]:
    min = scores[i]
  if max < scores[i]:
    max = scores[i]
  # calculate the average
  scoreTotal += scores[i]
  # check if A
  if scores[i] >= 90:
    any_A_grades = True

# sort in desc order
scores.sort(reverse=True)

# output the scores to the console
for i in range(len(scores)):
  print(scores[i], end = " ")

print("min: " + str(min))
print("max: " + str(max))

print("avg: " + "{:.1f}".format(scoreTotal/n))

if any_A_grades:
  print("At least one 'A' grade entered")
