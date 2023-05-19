import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphVisualizerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bidirectional Search")

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

        self.visualize_button = tk.Button(self.master, text="Visualize", command=self.visualize)
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

    def bidirectional_search(self):
        start = self.start_var.get()
        goal = self.goal_var.get()

        # Perform BFS from both directions
        forward_visited = {start}
        backward_visited = {goal}
        forward_queue = [(start, [start])]
        backward_queue = [(goal, [goal])]

        while forward_queue and backward_queue:
            # Forward BFS
            node, path = forward_queue.pop(0)
            successors = self.graph.get(node, [])
            for successor in successors:
                if successor not in forward_visited:
                    forward_visited.add(successor)
                    forward_queue.append((successor, path + [successor]))
                    if successor in backward_visited:
                        backward_visited_list = list(backward_visited)
                        return path + [successor] + backward_queue[backward_visited_list.index(successor)][1][::-1]

            # Backward BFS
            node, path = backward_queue.pop(0)
            successors = self.graph.get(node, [])
            for successor in successors:
                if successor not in backward_visited:
                    backward_visited.add(successor)
                    backward_queue.append((successor, path + [successor]))
                    if successor in forward_visited:
                        forward_visited_list = list(forward_visited)
                        return forward_queue[forward_visited_list.index(successor)][1] + [successor] + path[::-1]

        return None

    def visualize(self):
        # Clear the previous visualization
        self.figure.clf()

        # Run the bidirectional search
        path = self.bidirectional_search()

        # Check if a path was found
        if path is None:
            print("No path found")
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
            print("No path found")
        else:
            print("Path:", ' -> '.join(path))


if __name__ == '__main__':
    root = tk.Tk()
    app = GraphVisualizerGUI(root)
    root.mainloop()

