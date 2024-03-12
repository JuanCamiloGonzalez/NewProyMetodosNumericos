import tkinter as tk
import threading
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("gausseidelmenu")
        self.master.geometry("400x300") # Establece el tamaño de la ventana
        self.create_widgets()

    def create_widgets(self):
        # Crea un título centrado en la ventana
        self.title_label = tk.Label(self.master, text="Tamaño de la matriz", font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        options = ["Matriz 2*2", "Matriz 3*3", "Matriz 4*4"]
        for i in range(len(options)):
            option_button = tk.Button(self.menu_frame, text=options[i], width=20, command=lambda index=i: self.execute_file(index))
            option_button.pack(pady=5)

    def execute_file(self, index):
        file_names = ["gaussseidel.py --n 2", "gaussseidel.py --n 3", "gaussseidel.py --n 4"]
        file_name = file_names[index]
        thread = threading.Thread(target=lambda: os.system("python " + file_name))
        thread.start()
root = tk.Tk()
app = Application(master=root)
app.mainloop()