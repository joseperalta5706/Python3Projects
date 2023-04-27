days = [60, 61, 62, 63, 64]
print("Fort Bragg, California forecast temperatures:")
print("Monday, Aug 25, " + str(days[0]) + " degrees")
print("Tuesday, Aug 26 " + str(days[1]) + " degrees")
print("Wednesday, Aug 27, " + str(days[2]) + " degrees")
print("Thursday, Aug 28, " + str(days[3]) + " degrees")
print("Friday, Aug 29, " + str(days[4]) + " degrees")
print("Source: me")
lowest = 1000
highest = 1
for i in range(len(days)):
  if (days[i] < lowest):
    lowest = days[i]
  if (days[i] > highest):
    highest = days[i]

print("The low for the week is " + str(lowest))  
print("The high for the week is " + str(highest))
