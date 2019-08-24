import hackergenerator
import time
import sys
import os

if(len(sys.argv) >= 2):
    i = int(sys.argv[1])
else:
    i = 10

if(len(sys.argv) >= 3):
    n = int(sys.argv[2])
else:
    n = 10

while(True):
    for x in range(0, n):
        sentence = hackergenerator.sentence()
        print(sentence)
        #os.system("espeak '" + sentence + "'") #if you are to lazy to read install espeak and uncomment this line.
        print("")
    time.sleep(i)
