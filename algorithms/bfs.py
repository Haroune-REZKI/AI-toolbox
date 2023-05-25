import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BFSWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("BFS")

        # Create the input form
        self.node_label = tk.Label(self.master, text="Node:")
        self.node_label.pack()
        self.node_var = tk.StringVar()
        self.node_entry = tk.Entry(self.master, textvariable=self.node_var)
        self.node_entry.pack()

        self.successor_label = tk.Label(self.master, text="Successor:")
        self.successor_label.pack()
        self.successor_var = tk.StringVar()
        self.successor_entry = tk.Entry(self.master, textvariable=self.successor_var)
        self.successor_entry.pack()

        self.cost_label = tk.Label(self.master, text="Cost:")
        self.cost_label.pack()
        self.cost_var = tk.StringVar()
        self.cost_entry = tk.Entry(self.master, textvariable=self.cost_var)
        self.cost_entry.pack()

        self.add_button = tk.Button(self.master, text="Add", command=self.add_data)
        self.add_button.pack()

        self.start_label = tk.Label(self.master, text="Start Node:")
        self.start_label.pack()
        self.start_var = tk.StringVar()
        self.start_entry = tk.Entry(self.master, textvariable=self.start_var)
        self.start_entry.pack()

        self.goal_label = tk.Label(self.master, text="Goal Node:")
        self.goal_label.pack()
        self.goal_var = tk.StringVar()
        self.goal_entry = tk.Entry(self.master, textvariable=self.goal_var)
        self.goal_entry.pack()

        self.visualize_button = tk.Button(self.master, text="Visualize", command=self.visualize)
        self.visualize_button.pack()
        

        # Create the canvas for the graph visualization
        self.figure = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack()

        # Create the graph
        self.graph = {
	    'A': {'B': 2, 'C': 3},
	    'B': {'A': 2, 'D': 5, 'C': 4},
	    'C': {'A': 3, 'D': 3, 'F': 6},
	    'D': {'B': 5, 'C': 3, 'E': 2},
	    'E': {'D': 2, 'G': 5, 'F': 3},
	    'F': {'C' : 6, 'E': 3},
	    'G': {'E': 5}
	}
    def add_data(self):
        node = self.node_var.get()
        successor = self.successor_var.get()
        cost = int(self.cost_var.get())
        
        # Add the data to the graph dictionary
        if node not in self.graph:
            self.graph[node] = {}
        self.graph[node][successor] = cost
        
        # Clear the input fields
        self.node_var.set('')
        self.successor_var.set('')
        self.cost_var.set('')    

    def add_edge(self):
        node = self.node_var.get()
        successor = self.successor_var.get()
        cost = int(self.cost_var.get())
        if node not in self.graph:
            self.graph[node] = {}
        self.graph[node][successor] = cost

    def bfs(self, start, goal, graph):
        queue = [(start, [start])]
        visited = set()

        while queue:
            node, path = queue.pop(0)
            visited.add(node)

            if node == goal:
                return path

            for successor in graph.get(node, []):
                if successor not in visited:
                    new_path = path + [successor]
                    queue.append((successor, new_path))

        return None

    def visualize(self):
        # Clear the previous visualization
        self.figure.clf()

        # Run the BFS algorithm
        start = self.start_var.get()
        goal = self.goal_var.get()
        path = self.bfs(start, goal, self.graph)

        # Draw the graph
        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        if path is not None:
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2.0)
            self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    app = BFSWindow(root)
    root.mainloop()

