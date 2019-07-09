import hackergenerator
import time
import sys

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
        print(hackergenerator.sentence())
        print("")
    time.sleep(i)
