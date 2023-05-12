import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter as tk

class CustomProblem:
    def __init__(self, initial_state, graph, edges):
        self.initial = initial_state
        self.graph = graph
        self.edges = edges

    def initial_state(self):
        return self.initial

    def neighbors(self, state):
        return self.edges[state]

    def evaluate(self, state):
        return self.graph[state]

def hill_climbing(problem, iterations):
    current = problem.initial_state()
    path = [current]
    for _ in range(iterations):
        neighbors = problem.neighbors(current)
        if not neighbors:
            break

        next_state = max(neighbors, key=problem.evaluate)
        if problem.evaluate(next_state) <= problem.evaluate(current):
            break

        current = next_state
        path.append(current)

    return current, path

def visualize_graph(graph, edges, path):
    print("Visualizing graph...")
    G = nx.Graph()
    for state, value in graph.items():
        G.add_node(state, value=value)

    for state1, neighbors in edges.items():
        for state2 in neighbors:
            G.add_edge(state1, state2)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{u}-{v}" for u, v in G.edges()}
    node_labels = {node: f"{node}\n{data['value']}" for node, data in G.nodes(data=True)}

    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_weight="bold")

    edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color="r", width=2)

    plt.ion()
    plt.show(block=True)  # Updated this line # added this line bcs the visu window closes immediately

def get_input():
    root = tk.Tk()

    num_states_label = tk.Label(root, text="Enter the number of states:")
    num_states_label.pack()
    num_states_entry = tk.Entry(root)
    num_states_entry.pack()

    states_frame = tk.Frame(root)
    states_frame.pack()

    def add_state():
        state_frame = tk.Frame(states_frame)
        state_frame.pack(side=tk.TOP)

        state_label = tk.Label(state_frame, text=f"State {len(states_frame.winfo_children())}:")
        state_label.pack(side=tk.LEFT)

        state_entry = tk.Entry(state_frame)
        state_entry.pack(side=tk.LEFT)

        value_label = tk.Label(state_frame, text="Objective value:")
        value_label.pack(side=tk.LEFT)

        value_entry = tk.Entry(state_frame)
        value_entry.pack(side=tk.LEFT)

        state_entries.append({"state": state_entry, "value": value_entry})

    num_states_button = tk.Button(root, text="Add states", command=add_state)
    num_states_button.pack()

    initial_state_label = tk.Label(root, text="Enter the initial state:")
    initial_state_label.pack()
    initial_state_entry = tk.Entry(root)
    initial_state_entry.pack()

    num_edges_label = tk.Label(root, text="Enter the number of edges:")
    num_edges_label.pack()
    num_edges_entry = tk.Entry(root)
    num_edges_entry.pack()

    edges_frame = tk.Frame(root)
    edges_frame.pack()

    def add_edge():
        edge_label = tk.Label(edges_frame, text=f"Edge {len(edges_frame.winfo_children()) + 1}:")
        edge_label.pack(side=tk.LEFT)
        state1_entry = tk.Entry(edges_frame)
        state1_entry.pack(side=tk.LEFT)
        state2_entry = tk.Entry(edges_frame)
        state2_entry.pack(side=tk.LEFT)
        edge_entries.append({"state1": state1_entry, "state2": state2_entry})

    num_edges_button = tk.Button(root, text="Add edges", command=add_edge)
    num_edges_button.pack()

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_input(root))
    submit_button.pack()

    def submit_input(root):
        input_data["num_states"] = int(num_states_entry.get())
        input_data["states"] = [{"state": entry["state"].get(), "value": float(entry["value"].get())} for entry in state_entries]
        input_data["initial_state"] = initial_state_entry.get()
        input_data["num_edges"] = int(num_edges_entry.get())
        input_data["edges"] = [(entry["state1"].get(), entry["state2"].get()) for entry in edge_entries]

        num_states = int(num_states_entry.get())
        graph = {}
        for entry in state_entries:
            state = entry["state"].get()
            value = float(entry["value"].get())
            graph[state] = value

        initial_state = initial_state_entry.get()

        num_edges = int(num_edges_entry.get())
        edges = {}
        for entry in edge_entries:
            state1 = entry["state1"].get()
            state2 = entry["state2"].get()
            if state1 not in edges:
                edges[state1] = []
            if state2 not in edges:
                edges[state2] = []
            edges[state1].append(state2)
            edges[state2].append(state1)

        problem = CustomProblem(initial_state, graph, edges)
        input_data["problem"] = problem

        root.destroy()
    state_entries = []
    edge_entries = []
    input_data = {}

    root.mainloop()

    return input_data["problem"]

def main():
    problem = get_input()
    solution, path = hill_climbing(problem, 1000)
    print("Solution found:", solution)
    print("Path taken:", path)

    visualize_graph(problem.graph, problem.edges, path)

if __name__ == "__main__":
    main()