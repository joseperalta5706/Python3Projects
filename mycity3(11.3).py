my_days = []
default_temps = [60,61,62,63,64]

for i in range(0, 4):
  uservalue = input("input a temperature: ")
  if uservalue == "":
    my_days = default_temps
    break
  my_days.append(int(uservalue))

print("Fort Bragg, California forecast temperatures:")
print("Monday, Aug 25, " + str(my_days[0]) + " degrees")
print("Tuesday, Aug 26 " + str(my_days[1]) + " degrees")
print("Wednesday, Aug 27, " + str(my_days[2]) + " degrees")
print("Thursday, Aug 28, " + str(my_days[3]) + " degrees")
print("Friday, Aug 29, " + str(my_days[4]) + " degrees")
print("Source: me")
lowest = 1000
highest = 1
for i in range(len(my_days)):
  if (my_days[i] < lowest):
    lowest = my_days[i]
  if (my_days[i] > highest):
    highest = my_days[i]
    x = my_days.count(lowest)
    y = my_days.count(lowest)
print("The low for the week is " + str(lowest) + ", occuring " + str(x) + " times.")  
print("The high for the week is " + str(highest) + ", occuring " + str(y) + " times.")
