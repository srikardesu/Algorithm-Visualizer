import time
from colors import *

def merge(data, start, mid, end, draw, Tick):
    colorstore1 = [RED if x >= start and x < mid else YELLOW if x == mid else DARK_BLUE if x > mid and x <= end else WHITE for x in range(len(data))]
    draw(data, colorstore1)
    time.sleep(Tick)
    l = start
    r = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if l > mid:
            tempArray.append(data[r])
            r+=1
        elif r > end:
            tempArray.append(data[l])
            l+=1
        elif data[l] < data[r]:
            tempArray.append(data[l])
            l+=1
        else:
            tempArray.append(data[r])
            r+=1

    for l in range(len(tempArray)):
        data[start] = tempArray[l]
        start += 1

def mergesort(data, start, end, draw, Tick):
    if start < end:
        mid = int((start + end) / 2)
        mergesort(data, start, mid, draw, Tick)
        mergesort(data, mid+1, end, draw, Tick)
        merge(data, start, mid, end, draw, Tick)
