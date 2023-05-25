from tkinter import Tk, Label, Button
from user_interface.search_algorithm_window import SearchAlgorithmWindow

class MainMenu(Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.configure(bg="#F5F5F5")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        label = Label(self, text="Choose what is appropriate for you:", bg="#F5F5F5", font=("Arial", 16))
        label.pack(side="top", pady=20)

        search_algorithm_button = Button(self, text="Search Algorithms", command=self.open_search_algorithm_window, bg="#03A9F4", fg="white", font=("Helvetica", 12), padx=10, pady=5, bd=0)
        search_algorithm_button.pack(side="top", pady=20)
        search_algorithm_button = Button(self, text="Play a game", command=self.open_search_algorithm_window, bg="#03A9F4", fg="white", font=("Helvetica", 12), padx=10, pady=5, bd=0)
        search_algorithm_button.pack(side="top", pady=20)


        quit_button = Button(self, text="QUIT", command=self.destroy, bg="#F44336", fg="white", font=("Helvetica", 12), padx=10, pady=5, bd=0)
        quit_button.pack(side="bottom", pady=20)

    def open_search_algorithm_window(self):
        search_algorithm_window = SearchAlgorithmWindow(self)

app = MainMenu()
app.mainloop()
