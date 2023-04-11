import math

""" Program to find monthly on mortgage loan, input from file/output to file."""


def payment_amount():

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

    print("Amount borrowed: " + str(borrowed))
    print("Annual interest rate: " + str(interest_rate))
    print("Payback period: " + str(n))
    print("Monthly payments: " + str(monthly))
    f = open("/content/drive/MyDrive/Github/myfiles/mortgage.txt","w+")
    f.write("Amount borrowed: " + str(borrowed) + "\n")
    f.write("Annual interest rate: " + str(interest_rate) + "\n")
    f.write("Loan length: " + str(n) + "\n" + "\n")
    f.write("Montly Payment: " + str(monthly))

    f.close()
payment_amount()
