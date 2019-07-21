import sys
import os

r=open('text','r')
bit=r.read()
print(bit)
i=0
while(i<30000):
    b=i/2
    print(b)
    if(i%2==0):
        g=open('text',"w+")
        g.write("1")
        g.close()

    elif(i%2==1):
        g=open('text',"w+")
        g.write("0")
        g.close()

    r=open('text','r')
    bit=r.read()
    if(bit==1):
        print("one")

    elif(bit=="1"):
        print("string one")

    elif(bit==0):
        print("zero")

    elif(bit=="0"):
        print("string zero")

    i=i+1
