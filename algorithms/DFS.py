import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DFSWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("DFS")
        self.geometry("400x400")
        self.create_widgets()

        # Create the graph
        self.graph = {}

    def create_widgets(self):
        # Create the input form
        self.node_label = tk.Label(self, text="Node:")
        self.node_label.pack()
        self.node_var = tk.StringVar()
        self.node_entry = tk.Entry(self, textvariable=self.node_var)
        self.node_entry.pack()

        self.successor_label = tk.Label(self, text="Successor:")
        self.successor_label.pack()
        self.successor_var = tk.StringVar()
        self.successor_entry = tk.Entry(self, textvariable=self.successor_var)
        self.successor_entry.pack()

        self.cost_label = tk.Label(self, text="Cost:")
        self.cost_label.pack()
        self.cost_var = tk.StringVar()
        self.cost_entry = tk.Entry(self, textvariable=self.cost_var)
        self.cost_entry.pack()

        self.add_button = tk.Button(self, text="Add", command=self.add_data)
        self.add_button.pack()

        self.start_label = tk.Label(self, text="Start Node:")
        self.start_label.pack()
        self.start_var = tk.StringVar()
        self.start_entry = tk.Entry(self, textvariable=self.start_var)
        self.start_entry.pack()

        self.goal_label = tk.Label(self, text="Goal Node:")
        self.goal_label.pack()
        self.goal_var = tk.StringVar()
        self.goal_entry = tk.Entry(self, textvariable=self.goal_var)
        self.goal_entry.pack()

        self.visualize_button = tk.Button(self, text="Visualize", command=self.visualize)
        self.visualize_button.pack()

        # Create the canvas for the graph visualization
        self.figure = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack()

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

    def dfs(self, start, goal, graph):
        stack = [(start, [start])]
        visited = set()

        while stack:
            node, path = stack.pop()
            visited.add(node)

            if node == goal:
                return path

            for successor in reversed(graph.get(node, [])):
                if successor not in visited:
                    new_path = path + [successor]
                    stack.append((successor, new_path))

        return None

    def visualize(self):
        # Clear the previous visualization
        self.figure.clf()

        # Run the DFS algorithm
        start = self.start_var.get()
        goal = self.goal_var.get()
        path = self.dfs(start, goal, self.graph)

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
