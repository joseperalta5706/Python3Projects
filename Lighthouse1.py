""" Program to determine how far a boat can see a lighthouse at sea in miles """

def view_distance():
    # 'h' is the height of a lighthouse in feet, as a whole number
    h = 200
    distance = sqrt(.8 * h)
    print("A " + h + " foot tall lighthouse can be seen from " + distance + " miles away")
    view_distance()