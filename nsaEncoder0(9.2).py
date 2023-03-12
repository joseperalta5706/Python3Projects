import math
# Encoder for scrambling text that the user has input
text1 = input("Enter a line of text: ") # get text to be scrambled from user

# to build encoded string, add 1 to the ASCII code of each letter
text2 = "" # an scrambled version of sOld
for i in range(len(text1)): # for each char...
 text2 += chr(ord(text1[i]) + 1) # bump its ASCII code by 1
print(text2)
