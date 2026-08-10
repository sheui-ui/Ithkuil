import time
import random
import os
if os.name == "nt":
    os.system("")
n = int(input("Please enter the number of times"))
print ("\033[32mAdmimistrator@SK-3000888ZJID" + " " + "\033[35mMINGW64" + " " + "\033[33m~")
print ("\033[37m$ ping -n"+" "+str(n)+" "+"github.com")
print ()
print ("Pinging github.com [20.205.243.166] with 32 bytes of data:")
agree = 0
tmax = 0
tlim = 100000000
for i in range(n):
    a = random.randint(0,4)
    if a == 0:
        t = random.randint(100,5000)
        time.sleep(t/1000)
        print(f"Reply from 20.205.243.166: Bytes=32 Time={t}ms TTL=112")
        if t / 1000 > tmax:
            tmax = t
        if t / 1000 < tlim:
            tlim = t
        agree += 1
    else:
        time.sleep(5)
        print("Request timed out")
if tlim == 100000000:
    tlim = 0
print ()
print ("Ping statistics for 20.205.243.166:")
print (f"    Packets: Sent = {n}, Received = {agree}, Lost = {n-agree} ({(100/n)*(n-agree)}% lost),")
print ("Estimated round-trip time (in milliseconds):")
print (f"    Minimum = {tlim} ms, Maximum = {tmax} ms, Average = {(tmax + tlim) / n} ms")
print ()
print ("\033[32mAdmimistrator@SK-3000888ZJID" + " " + "\033[35mMINGW64" + " " + "\033[33m~")
input ("\033[37m$")