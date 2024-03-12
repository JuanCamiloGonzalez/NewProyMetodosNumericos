import tkinter as tk
import threading
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Proyecto Final Métodos Numéricos")
        self.master.geometry("400x400") # Establece el tamaño de la ventana
        self.create_widgets()

    def create_widgets(self):
        # Crea un título centrado en la ventana
        self.title_label = tk.Label(self.master, text="Menú de Metodos Numericos", font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        options = ["Punto Fijo", "Bisección", "Secante", "Trapezoidal", "Simpson", "Gauss Seidel","Newton","Jacobi"]
        for i in range(len(options)):
            option_button = tk.Button(self.menu_frame, text=options[i], width=20, command=lambda index=i: self.execute_file(index))
            option_button.pack(pady=5)

    def execute_file(self, index):
        file_names = ["punto_fijo.py", "biseccion.py", "secante.py", "trapecio.py", "simpson.py", "gaussseidelmenu.py", "Newton.py","Jacobi.py"]
        file_name = file_names[index]
        thread = threading.Thread(target=lambda: os.system("python " + file_name))
        thread.start()
root = tk.Tk()
app = Application(master=root)
app.mainloop()