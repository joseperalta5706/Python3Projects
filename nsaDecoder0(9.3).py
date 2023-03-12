import math
# Decoder for unscrambling text that the user has input
text1 = input("Enter a line of text: ") # get text to be unscrambled from user

# to build decoded string, minus 1 to the ASCII code of each letter
text2 = "" # an unscrambled version of text1
for i in range(len(text1)): # for each char...
 text2 += chr(ord(text1[i]) - 1) # lower its ASCII code by 1
print(text2)
