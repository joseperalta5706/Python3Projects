import math
""" App to calculate earnings through a savings plan using user input values. """
# input values
years = int(input("Years to retirement: "))  # number of years making monthly deposits
D = int(input("Amount to be deposited per month: $"))  # dollars deposited per month

# output (calculated) values
p = float(input("Annual interest rate: %"))
p = p / 12  # monthly rate
T = years * 12  # number of months
S = D * ((math.pow(1 + p, T) - 1) / p)

# echoing input values, not rounded
print("In", years, "years, $", end="")
print(D, "deposited per month at an annual rate of %" + str("{:0.03f}".format(p)) + " interest will grow to $" + str("{:0.02f}".format(S)),
      end=".")