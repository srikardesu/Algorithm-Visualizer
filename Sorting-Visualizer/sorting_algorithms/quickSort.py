import time
from colors import *

def partition(data, head, tail, draw, Tick):
    border = head
    pivot = data[tail]
    draw(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(Tick)
    for j in range(head, tail):
        if data[j] < pivot:
            draw(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(Tick)
            data[border], data[j] = data[j], data[border]
            border = border + 1
        draw(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(Tick)
    draw(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(Tick)
    data[border], data[tail] = data[tail], data[border]
    return border

def quicksort(data, head, tail, draw, Tick):
    if head < tail:
        partitionIdx = partition(data, head, tail, draw, Tick)
        quicksort(data, head, partitionIdx-1, draw, Tick)
        quicksort(data, partitionIdx+1, tail, draw, Tick)
 
# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - After all elements are sorted
 
def getColorArray(dataLen, head, tail, border, currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('Grey')
        else:
            colorArray.append('White')
        if i == tail:
            colorArray[i] = 'Blue'
        elif i == border:
            colorArray[i] = 'Red'
        elif i == currIdx:
            colorArray[i] = 'Yellow'
 
        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'Green'
 
    return colorArray