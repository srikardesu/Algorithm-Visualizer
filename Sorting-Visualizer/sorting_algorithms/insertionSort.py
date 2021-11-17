import time
from colors import *

def insertionsort(data,draw,Tick):
    for i in range(len(data)):
        store = data[i]
        temp = i
        while temp > 0 and store < data[temp-1]:
            colorstore = [YELLOW if x == temp or x == i else RED for x in range(0,100)]
            draw(data, colorstore)
            time.sleep(Tick)
            data[temp]=data[temp-1]
            temp -= 1
        data[temp] = store
        colorstore = [YELLOW if x == temp or x == i else RED for x in range(0,100)]
        draw(data, colorstore)
        time.sleep(Tick)
    
    color = [LIGHT_GREEN for x in range(0,100)]
    draw(data,color)