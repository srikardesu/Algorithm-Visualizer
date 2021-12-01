# Algorithm-Visualizer

This is an Algorithm-Visualizer that helps in understanding several algorithms using python.

It has multiple parts, starting off with the Sorting Visualizer.

### Sorting-Visualizer :

The algorithms that have been implemented are as follows :

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort (Divide and Conquer)
- Quick Sort (Divide and Conquer)
- Counting Sort

Pdfs for every algorithm has been attached, these provide the user with the ideas behind these sorting algorithms and also the helper/dummy codes to get started.

### DP_Algos-Visualizer :

The next section is the DP Algos visualizer, Here, I have taken 2 of the most famous algorithms, Longest increasing subsequence and knapsack problems.  The knapsack problem has been visualized by showing the dp table at every iteration, the indices involved in decision making at every step, have been marked in red and the other values are marked in blue. LIS problem has been visualized in a similar way. The pdfs for the algorithms have been attached as well, which helps the reader to understand the algorithm first and try coding it up on their own using the pseudo/helper code provided.

### Graph_Algos_Visualizer :

General Graph algorithms like BFS and DFS have been visited in this section, The BFS variant that I decided to show here is the shortest path between 2 nodes in an unweighted graph. It shows us the complete path from one node to another or displays if it could not find any path. the DFS on the other hand shows the sequence of nodes visited from the root node(entered by the user) as it happens during the DFS.

### Greedy_Algos_Visualizer :

The greedy algorithms I decided to show here are Dijkstra and Kruskals, I have decided to specifically show these as visualization of the shortest path in Dijkstra in graph form becomes easier and the spanning tree in Kruskals becomes easier as well. The pdfs for these have also been attached which have implementation details as well as explanation on the algorithms.

### How to run?

clone the repository 

> git clone [https://github.com/srikardesu/Algorithm-Visualizer](https://github.com/srikardesu/Algorithm-Visualizer)
> 

cd into the required directory :

> cd <directory>
> 

Run the required file <file.py> as:

> python3 file.py
> 

This project uses tkinter, This can be installed on ubuntu as follows :

> sudo apt-get update
sudo apt install python3-tk
>