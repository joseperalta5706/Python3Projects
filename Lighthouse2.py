import math
""" App for calculating how far away a Lighthouse can be seen, using console inputs. """

def view_distance():

    # use the console to input the height of a lighthouse.
    height = float(input("Lighthouse height in feet: "))
   # use this formula to determine the view distance in miles(integer); distance = square root of: 0.8 times the height in feet
    distance = math.sqrt(.8 * height)

    print("A " + str(height) + "foot lighthouse can be seen from a distance of " + str("{:0.0f}".format(distance)) + " miles away.")

view_distance()