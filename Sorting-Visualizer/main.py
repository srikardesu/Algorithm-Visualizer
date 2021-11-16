from tkinter import *
from tkinter import ttk
import random
from colors import *

from sorting_algorithms.bubbleSort import bubblesort

#Testing bubblesort

# n = int(input("Enter the number of elements in array: "))
# print("Enter the array: ")
# lst=[]
# for i in range(0,n):
#     ele = int(input())
#     lst.append(ele)

# print("Sorted array is as follows: ")
# bubblesort(lst)
# print(lst)

def generate():
    global data
    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 300)
        data.append(random_value)
    print(data)

window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg=WHITE)

algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']

UI_frame = Frame(window)
UI_frame.grid(row=0, column=0, padx=100, pady=100)

l1 = Label(UI_frame, text="Sorting Algorithm: ")
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ")
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=bubblesort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

window.mainloop()

