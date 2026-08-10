import time
import random
import os
if os.name == "nt":
    os.system("")
n = int(input("请输入次数"))
print ("\033[32mAdmimistrator@SK-3000888JSAI" + " " + "\033[35mMINGW64" + " " + "\033[33m~")
print ("\033[37m$ ping -n"+" "+str(n)+" "+"github.com")
print ()
print ("正在 Ping github.com [20.205.243.166] 具有 32 字节的数据:")
agree = 0
tmax = 0
tlim = 100000000
for i in range(n):
    a = random.randint(0,4)
    if a == 0:
        t = random.randint(100,5000)
        time.sleep(t/1000)
        print(f"来自 20.205.243.166 的回复：字节=32 时间={t}ms TTL=112")
        if t / 1000 > tmax:
            tmax = t
        if t / 1000 < tlim:
            tlim = t
        agree += 1
    else:
        time.sleep(5)
        print("请求超时")
if tlim == 100000000:
    tlim = 0
print ()
print ("20.205.243.166 的 Ping 统计信息：")
print (f"    数据包：已发送 = {n}，已接收 = {agree}，丢失 = {n-agree}（{(100/n)*(n-agree)}% 丢失），")
print ("往返行程的估计时间（以毫秒为单位）：")
print (f"    最短 = {tlim}ms，最长 = {tmax}ms，平均 = {(tmax + tlim) / n}ms")
print ()
print ("\033[32mAdmimistrator@SK-3000888JSAI" + " " + "\033[35mMINGW64" + " " + "\033[33m~")
input ("\033[37m$")