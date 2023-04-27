# read the scores and build the sum 
scoreTotal = 0
scores = []
for i in range(4):
  aScore = int(input("Enter a score: ")) 
  scoreTotal += aScore
  scores.append(aScore)

# calculate and output the average 
average = scoreTotal / 4
print("The average of 4 numbers is: " + str(average))


counter = 0
for i in range(len(scores)):
  if scores[i] > average:
    counter += 1
    
print(str(counter) + " scores are greater than the average.")    
