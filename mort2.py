import math

# input values
years = 10  # number of years making monthly deposits
D = 100  # dollars deposited per month

# output (calculated) values
p = 0.075 / 12  # monthly rate
T = years * 12  # number of months
S = D * ((math.pow(1 + p, T) - 1) / p)

# echoing input values, not rounded
print("In", years, "years, $", end="")
print(D, "deposited per month will grow to $" + str("{:0.02f}".format(S)), end="")