import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphVisualizerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Depth-Limited Search")

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

        self.add_button = tk.Button(self.master, text="Add Connection", command=self.add_connection)
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

        self.depth_label = tk.Label(self.master, text="Depth Limit:")
        self.depth_label.pack()
        self.depth_var = tk.StringVar()
        self.depth_entry = tk.Entry(self.master, textvariable=self.depth_var)
        self.depth_entry.pack()

        self.visualize_button = tk.Button(self.master, text="Visualize", command=self.visualize_depth_limited_search)
        self.visualize_button.pack()

        # Create the canvas for the graph visualization
        self.figure = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack()

        # Create an empty graph
        self.graph = {}

    def add_connection(self):
        node = self.node_var.get()
        successor = self.successor_var.get()

        # Add the connection to the graph
        if node not in self.graph:
            self.graph[node] = {}
        self.graph[node][successor] = 1

        # Clear the input fields
        self.node_var.set('')
        self.successor_var.set('')

    def depth_limited_search(self, node, goal, depth_limit, path=[]):
        if node == goal:
            return path + [node]
        if depth_limit == 0:
            return None
        successors = self.graph.get(node, [])
        for successor in successors:
            if successor not in path:
                result = self.depth_limited_search(successor, goal, depth_limit - 1, path + [node])
                if result is not None:
                    return result
        return None

    def visualize_depth_limited_search(self):
        # Clear the previous visualization
        self.figure.clf()

        # Get the input values
        start = self.start_var.get()
        goal = self.goal_var.get()
        depth_limit = int(self.depth_var.get())

        # Run the depth-limited search
        path = self.depth_limited_search(start, goal, depth_limit)

        # Check if a path was found
        if path is None:
            print("No path found within the depth limit")
            return

        # Create a networkx graph
        G = nx.Graph()
        for node in self.graph:
            G.add_node(node)
            successors = self.graph[node]
            for successor in successors:
                G.add_edge(node, successor)

        # Highlight the path in the graph
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

        # Draw the graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=10)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        # Update the canvas
        self.canvas.draw()

        # Print the path
        if path is None:
            print("No path found within the depth limit")
        else:
            print("Path:", ' -> '.join(path))


if __name__ == '__main__':
    root = tk.Tk()
    app = GraphVisualizerGUI(root)
    root.mainloop()
