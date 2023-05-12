import tkinter as tk
from user_interface.search_algorithm_window import SearchAlgorithmWindow

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.search_algorithm_button = tk.Button(self, text="Search Algorithms", command=self.open_search_algorithm_window)
        self.search_algorithm_button.pack(side="top")

        # Add more buttons for other windows (Local Search, Adversarial Search, CSP Solver)

        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def open_search_algorithm_window(self):
        search_algorithm_window = tk.Toplevel(self.master)
        search_algorithm_app = SearchAlgorithmWindow(master=search_algorithm_window)
