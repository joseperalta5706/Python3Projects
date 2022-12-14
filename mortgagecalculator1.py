"""jose. app for calculating monthly mortgage payments per month using amount borrowed, interest rate, and payback period.

input: amount_borrowed, annual_interest_rate, payback_period.

output: monthly_payment.
"""
def monthly_payment():

  # int or float. user value for amount borrowed.
  amount_borrowed = float(input("enter the     amount borrowed: "))

  # int or float. user value for interest     rate on loan.
  annual_interest_rate = float(input("enter   interest rate loan amount: "))

  # amount to be paid per month.
  payback_period = int(input("enter the amount of months the loan is to be paid in:   "))

  monthly = float(amount_borrowed * (1 + annual_interest_rate)**payback_period * annual_interest_rate) / ((1 + annual_interest_rate)**payback_period - 1)

  print("Monthly payment is: " + "$" + "{:0.2f}".format(monthly))
 
monthly_payment()
