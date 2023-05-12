import tkinter as tk

graph = {...}
start = ...
goal = ...

class SearchAlgorithmWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Choose a search algorithm:")
        self.label.pack(side="top")

        # Add buttons and input fields for search algorithms (BFS, DFS, UCS, A*, Greedy Best-First Search)

        self.close_button = tk.Button(self, text="Close", command=self.master.destroy)
        self.close_button.pack(side="bottom")

from algorithms.uninformed_search import bfs, dfs

# ...

class SearchAlgorithmWindow(tk.Frame):
    # ...

    def create_widgets(self):
        # ...

        self.bfs_button = tk.Button(self, text="BFS", command=self.run_bfs)
        self.bfs_button.pack(side="top")

        # Add more buttons for other search algorithms

    def run_bfs(self):
        # Get input values and call the BFS function
        result = bfs(graph, start, goal)
        # Display the result
