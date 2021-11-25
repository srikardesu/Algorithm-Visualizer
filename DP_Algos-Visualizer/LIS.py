import pandas as pd
import time
from tkinter import *
from tkinter import ttk
import random
from colors import *

arr = [9,6,5,4,10,8,10,10,8,0]
length = 10
lis = [1,1,1,1,1,1,1,1,1,1]
mappedtargetcol = [0,1,3,6,10,15,21,28,36,45]

def visualise(target=0):
    if target < 46:
        pos=9
        for i in range(10) :
            if mappedtargetcol[i]>=target:
                pos=i
                break
        posl=-1
        if target==0:
            posl=0
        else :
            posl=target-mappedtargetcol[pos-1]-1

        if target == 0 :
            for i in range(10):
                if i == 0:
                    b = Entry(root,width=10,fg="Red",font=('Arial',20,'bold'))
                    b.grid(row=1, column=i,sticky='NSEW')
                    b.insert(END,arr[i])
                else :
                    b = Entry(root,width=10,fg="Blue",font=('Arial',20,'bold'))
                    b.grid(row=1, column=i,sticky='NSEW')
                    b.insert(END,arr[i])
        else :
            for i in range(10):
                if i==pos or i==posl:
                    b = Entry(root,width=10,fg="Red",font=('Arial',20,'bold'))
                    b.grid(row=1, column=i,sticky='NSEW')
                    b.insert(END,arr[i])
                else :
                    b = Entry(root,width=10,fg="Blue",font=('Arial',20,'bold'))
                    b.grid(row=1, column=i,sticky='NSEW')
                    b.insert(END,arr[i])
        if posl==0 :
            print(f"LIS[{pos}] is :")
            print(lis[pos])
        if arr[posl] < arr[pos] and lis[posl] + 1 > lis[pos] :
            lis[pos]=lis[posl] + 1 
            print(f"LIS[{pos}] is :")
            print(lis[pos])
        root.after(1000,visualise,target+1)

root = Tk()
root.title("Longest increasing Subsequence Visualization")

print("Array that is being visualised is as follows:")
print(arr)

for i in range(10):
    b = Entry(root,width=10,fg="Blue",font=('Arial',20,'bold'))
    b.grid(row=1, column=i,sticky='NSEW')
    b.insert(END,arr[i])


b1 = Button(root, text="Visualise", command=lambda: visualise(), bg=LIGHT_GRAY)
b1.grid(row=8, column=4, pady=50)

root.mainloop()
print("max of all LIS values (LIS length) is as follows:")
maximum = lis[0]
for i in range(10):
    if lis[i] > maximum :
        maximum = lis[i]

print(maximum)