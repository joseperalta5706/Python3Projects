!touch /content/drive/MyDrive/Github/myfiles/encoderinput.txt
!touch /content/drive/MyDrive/Github/myfiles/secret.txt
import math


userfilepath = input("Enter path of file to be encoded: ")
usermessage = open(str(userfilepath), "r")
message = usermessage.read()
outputfile = open("/content/drive/MyDrive/Github/myfiles/secret.txt", "w+")

for i in range(len(message)): # for each char...
  encodedmessage = ""
  encodedmessage += chr(ord(message[i]) + 1) # bump its ASCII code by 1
  outputfile.write(encodedmessage)

    # decode the line
    # write the decoded line to the output file
usermessage.close()
outputfile.close()
print("Finished.")
