""" Program to decode messages from a user's file using ASCII code for key """
!touch /content/drive/MyDrive/Github/myfiles/secret.txt
import math 

userfile = open("/content/drive/MyDrive/Github/myfiles/secret.txt", "r") # open user's file, open(path, opentype) /opentype r = read only
codedmessage = userfile.read() # pull out contents as a str 
userfile.close() # close file

decodedmessage = "" # set decodedmessage as a blank str.

for i in range(len(codedmessage)): # for every character in 'codedmessage' do next steps.
  decodedmessage += chr(ord(codedmessage[i]) - 1) # lower all 'codedmessage' ASCII characters codes by -1.

print(decodedmessage) # print(decodedmessage) aka(codedmessage/userfile/secret.txt) new ASCII code adjusted characters to reveal file message.
