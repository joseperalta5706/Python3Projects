import math

# with open('/content/sample_data/change.txt') as f: 
#  lines =  f.readlines()

def calcchange(changedue):

  hundreds = int(changedue / 100)
  changedue = changedue - (hundreds * 100)

  fifties = int(hundreds / 50)
  changedue = changedue - (fifties * 50)
  twenties = int(fifties / 20)
  changedue = changedue - (twenties * 20)
  tens = int(twenties / 10)
  changedue = changedue - (tens * 10)
  fives = int(tens / 5)
  changedue = changedue - (fives * 5)
  ones = int(fives / 1)
  changedue = changedue - (ones * 1)


  if hundreds != 0: 
    print("This many hundreds: " + str(hundreds))
  if fifties != 0:
    print("This many fifties: " + str(fifties))
  if twenties != 0: 
    print("This many twenties: " + str(twenties))
  if tens != 0: 
    print("This many tens: " + str(tens))
  if ones != 0: 
    print("This many ones: " + str(ones))      
    print("Cash payment amount: $" + f"{cashpayment:,}")
    print("Amount tendered: $" + f"{amounttendered:,}")
    print("Change due: $" + f"{changedue:,}")

f = open("/content/drive/MyDrive/Github/myfiles/change.txt","r")
cashpayment = int(f.readline())
amounttendered = int(f.readline())
f.close()

changedue = amounttendered - cashpayment


if cashpayment > amounttendered:
  print("error")
if cashpayment <= 0:
  print("cash payment due is $0")  

calcchange(changedue)    
