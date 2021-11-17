import time
from colors import *

def countingsort(data,draw,Tick):
    n = max(data) + 1
    count = []
    for i in range(0,n):
        count.append(0)

    for var in data:
        count[var] += 1
    
    start = 0
    for i in range(n):
        for j in range(count[i]):
            data[start] = i
            colorstore = [YELLOW if x == start else RED for x in range(0,100)]
            draw(data, colorstore)
            time.sleep(Tick)
            start += 1

    color = [LIGHT_GREEN for x in range(0,100)]
    draw(data,color)