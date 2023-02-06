import math
# function to calculate average
def calcAverage(a, b, c):
  result = 0 # step 1 set result to something
  result = (a + b + c) / 3 # step 2  add the 3 numbers and /
  return result # step 3 
# calcAverage ends here

# w, x, y take the place of a, b, c
w = int(input("Enter the first whole number:")) # user inputs 1st integer
x = int(input("second whole number:")) # 2nd integer
y = int(input("third whole number:")) # 3rd integer
z = calcAverage(w, x, y) # calls calcAverage function using whats in ()
print(z)
