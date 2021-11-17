import time
from colors import *

def selectionsort(data,draw,Tick):
    for i in range(99):
        mini=i
        for j in range(i+1,100):
            colorstore = [YELLOW if x == j or x == i else RED for x in range(0,100)]
            draw(data, colorstore)
            time.sleep(Tick)
            if data[j] < data[mini]:
                mini=j
        data[mini],data[i] = data[i],data[mini]
        colorstore = [YELLOW if x == mini or x == i else RED for x in range(0,100)]
        draw(data, colorstore)
        time.sleep(Tick) 
    
    color = [LIGHT_GREEN for x in range(0,100)]
    draw(data,color)