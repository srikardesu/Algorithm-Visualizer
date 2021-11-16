import time
from colors import *

def bubblesort(data,draw,Tick):
    for i in range(99):
        for j in range(99-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                colorstore = [YELLOW if x == j or x == j+1 else RED for x in range(0,100)]
                draw(data, colorstore)
                time.sleep(Tick)
    
    color = [LIGHT_GREEN for x in range(0,100)]
    draw(data,color)
    