import pandas as pd
import time
from tkinter import *
from tkinter import ttk
import random
from colors import *

val = [1,4,5,7]
wt = [1,3,4,5]
W=7
n=4
K = [[0 for x in range(W + 1)] for x in range(n + 1)]

def visualise(target=0):
    if target < (W+1)*(len(val)+1) :
        i = target//(W+1)
        w = target%(W+1)
        if i == 0 or w == 0:
                K[i][w] = 0
                for ii in range(n+1):
                    for ww in range(W+1):
                        if ii==i and ww==w:
                            b = Entry(root,width=10,fg="Red",font=('Arial',20,'bold'))
                            b.grid(row=ii, column=ww,sticky='NSEW')
                            b.insert(END,K[ii][ww])
                        else:
                            b = Entry(root,width=10,fg="Blue",font=('Arial',20,'bold'))
                            b.grid(row=ii, column=ww,sticky='NSEW')
                            b.insert(END,K[ii][ww])
        elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
                for ii in range(n+1):
                    for ww in range(W+1):
                        if (ii==i and ww==w) or (ii==i-1 and ww==w) or (ii==i-1 and ww==w-wt[i-1]) :
                            b = Entry(root,width=10,fg="Red",font=('Arial',20,'bold'))
                            b.grid(row=ii, column=ww,sticky='NSEW')
                            b.insert(END,K[ii][ww])
                        else:
                            b = Entry(root,width=10,fg="Blue",font=('Arial',20,'bold'))
                            b.grid(row=ii, column=ww,sticky='NSEW')
                            b.insert(END,K[ii][ww])
        else:
                K[i][w] = K[i-1][w]
                for ii in range(n+1):
                    for ww in range(W+1):
                        if (ii==i and ww==w) :
                            b = Entry(root,width=10,fg="Red",font=('Arial',20,'bold'))
                            b.grid(row=ii, column=ww,sticky='NSEW')
                            b.insert(END,K[ii][ww])
                        else:
                            b = Entry(root,width=10,fg="Blue",font=('Arial',20,'bold'))
                            b.grid(row=ii, column=ww,sticky='NSEW')
                            b.insert(END,K[ii][ww])
        root.after(1000,visualise,target+1)
    return

print("The value array being used in this simulation is as follows:")
print(val)
print("The weight array being used in this simulation is as follows:")
print(wt)
print("The knapsack limit is: ")
print(W)
root = Tk()
root.title("Knapsack Visualization")

for i in range(len(val) + 1) :
    for j in range(W + 1) :
        b = Entry(root,width=10,fg="Blue",font=('Arial',20,'bold'))
        b.grid(row=i, column=j,sticky='NSEW')
        b.insert(END,K[i][j])

b1 = Button(root, text="Visualise", command=lambda: visualise(), bg=LIGHT_GRAY)
b1.grid(row=8, column=3, pady=50)

root.mainloop()