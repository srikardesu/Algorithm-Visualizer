from tkinter import *
from tkinter import ttk
import random
from colors import *

from sorting_algorithms.bubbleSort import bubblesort
from sorting_algorithms.insertionSort import insertionsort
from sorting_algorithms.selectionSort import selectionsort
from sorting_algorithms.countingSort import countingsort
from sorting_algorithms.mergeSort import mergesort

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

def draw(data, color):
    canvas.delete("all")
    canvas_width = 1800
    canvas_height = 1200
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 600
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    window.update_idletasks()

def generate():
    global data
    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 300)
        data.append(random_value)
    #got the random array, time to plot it now
    print(data)
    color = [LIGHT_GREEN for x in range(0,100)]
    draw(data,color)

def speed():
    if speed_menu.get() == 'Slow':
        return 0.05
    elif speed_menu.get() == 'Medium':
        return 0.01
    else:
        return 0.0005

def sort():
    global data
    Tick = speed()
    if algo_menu.get() == 'Bubble Sort':
        bubblesort(data, draw, Tick)
    elif algo_menu.get() == 'Insertion Sort':
        insertionsort(data, draw, Tick)
    elif algo_menu.get() == 'Selection Sort':
        selectionsort(data, draw, Tick)
    elif algo_menu.get() == 'Counting Sort':
        countingsort(data, draw, Tick)
    elif algo_menu.get() == 'Merge Sort':
        mergesort(data, 0, len(data)-1, draw, Tick)

window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(2400, 1600)
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

canvas = Canvas(window, width=1800, height=1200, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

window.mainloop()

