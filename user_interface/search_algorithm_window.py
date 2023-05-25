import tkinter as tk
from algorithms.DFS import DFSWindow
from algorithms.bfs import BFSWindow
from algorithms.hillClimbing import hill_climbing, visualize_graph, get_input, hillClimbingWindow
from algorithms.UCS import UCSWindow

graph = {...}
start = ...
goal = ...

class SearchAlgorithmWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Search Algorithm")
        self.configure(bg="#F5F5F5")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Choose a search algorithm:", bg="#F5F5F5")
        self.label.pack(side="top")

        dfs_button = tk.Button(self, text="DFS", command=self.open_dfs_window, bg="#3FBBFF", fg="white", font=("Arial", 12), padx=5, pady=1, bd=0)
        dfs_button.pack(side="top", pady=10)
        dfs_button = tk.Button(self, text="BFS", command=self.open_bfs_window, bg="#3FBBFF", fg="white", font=("Arial", 12), padx=5, pady=1, bd=0)
        dfs_button.pack(side="top", pady=10)
        dfs_button = tk.Button(self, text="UCS", command=self.open_ucs_window, bg="#3FBBFF", fg="white", font=("Arial", 12), padx=5, pady=1, bd=0)
        dfs_button.pack(side="top", pady=10)
        dfs_button = tk.Button(self, text="Hill Climbing", command=self.open_hill_climbing_window, bg="#3FBBFF", fg="white", font=("Arial", 12), padx=5, pady=1, bd=0)
        dfs_button.pack(side="top", pady=10)
        dfs_button = tk.Button(self, text="Constraint Satisfaction", command=self.open_dfs_window, bg="#3FBBFF", fg="white", font=("Arial", 12), padx=10, pady=5, bd=0)
        dfs_button.pack(side="top", pady=10)
        self.close_button = tk.Button(self, text="Close", command=self.destroy)
        self.close_button.pack(side="bottom")
        

    def open_dfs_window(self):
        dfs_window = DFSWindow(self)
        dfs_window.mainloop()

    def open_hill_climbing_window(self):
        problem = get_input()  # Get input for the hill climbing problem
        solution, path = hill_climbing(problem, 1000)  # Perform hill climbing
        visualize_graph(problem.graph, problem.edges, path)  # Visualize the graph

    def open_ucs_window(self):
        ucs_window = tk.Toplevel(self)
        ucs_app = UCSWindow(ucs_window)
    
    def open_bfs_window(self):
        ucs_window = tk.Toplevel(self)
        ucs_app = BFSWindow(ucs_window)


def main():
    app = SearchAlgorithmWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
    



#app = SearchAlgorithmWindow()
#app.mainloop()
