"""

"""
import time

f = open('my.log', 'a+', buffering=1)
f.seek(0, 0)
n = 1
for i in f:
    n += 1

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f.write(str(n)+'.\t' + current_time + "\n")
    n += 1
    time.sleep(2)