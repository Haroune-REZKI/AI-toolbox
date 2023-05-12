from user_interface.main_menu import MainMenu
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(master=root)
    app.mainloop()