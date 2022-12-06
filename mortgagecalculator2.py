import math
""" Program to determine montly payments on a mortgage loan that has a thirty year return date."""

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

    print("A loan of $" + str(p) + " at an interest rate of %" + str(r) +
          " over 30years would come out to payments of $" + str("{:0.2f}".format(monthly)) + ".")

payment_amount()