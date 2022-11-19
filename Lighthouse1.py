""" Program to determine how far a boat can see a lighthouse at sea in miles """
import math 
def view_distance():
    # 'h' is the height of a lighthouse in feet, as a whole number
    h = 200
    distance = math.sqrt(.8 * h)
    print("A " + str(h) + " foot tall lighthouse can be seen from " + str(distance) + " miles away")
 
view_distance()
