import math
# while loop to ask for input and set the user password
for i in range(3):
  # ask the user for the password:
  user_input = input("Password:") 
  # Set the user password here
  actual_password = ("password1" )
  
  if user_input == actual_password: # check input against password 
  # if they match continue on with asking for interest rate info from user
      
      # Dollar amount borrowed as a whole number
    borrowed = int(input("Loan amount in dollars:$ "))
    p = borrowed

    # Interest rate on loan. Include decimal point(float)
    interest_rate = float(input("Interest rate on loan, include decimal:% "))
    r = interest_rate

    # Fixed payment length on loan. (30 years).
    loan_length = int(30)
    n = loan_length

    monthly = (p * (1 + r) ** n * r / ((1 + r) ** n - 1))

    print("A loan of $" + str(p) + " at an interest rate of %" + str(r) +
          " over 30years would come to monthly payments of $" + str("{:0.2f}".format(monthly)) + ".")
    break
  else: 
    print("Wrong password")
