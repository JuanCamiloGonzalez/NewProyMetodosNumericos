import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NewtonApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Crear los widgets de entrada
        self.func_label = tk.Label(self, text="Función:")
        self.func_label.pack()
        self.func_entry = tk.Entry(self)
        self.func_entry.pack()

        self.deriv_label = tk.Label(self, text="Derivada:")
        self.deriv_label.pack()
        self.deriv_entry = tk.Entry(self)
        self.deriv_entry.pack()

        self.x0_label = tk.Label(self, text="Estimación inicial:")
        self.x0_label.pack()
        self.x0_entry = tk.Entry(self)
        self.x0_entry.pack()

        # Crear el lienzo de Matplotlib en Tkinter
        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Botón para iniciar el método de Newton
        self.calcular_button = tk.Button(self, text="Calcular", command=self.iniciar_newton)
        self.calcular_button.pack()

    def iniciar_newton(self):
        # Obtener las entradas del usuario
        func_str = self.func_entry.get()
        deriv_str = self.deriv_entry.get()
        x0_str = self.x0_entry.get()

        # Convertir la estimación inicial a un número flotante
        try:
            x0 = float(x0_str)
        except ValueError:
            print("La estimación inicial debe ser un número válido.")
            return

        # Calcular la raíz utilizando el método de Newton
        raiz = self.metodo_newton(func_str, deriv_str, x0)
        print(f"La raíz es {raiz:.8f}")

        # Graficar la función y la línea tangente
        self.graficar_newton(func_str, deriv_str, x0, raiz, self.fig)

    def metodo_newton(self, func_str, deriv_str, x0, tol=1e-8, max_iter=100):
        def func(x):
            return eval(func_str)

        def deriv(x):
            return eval(deriv_str)

        for i in range(max_iter):
            h = func(x0) / deriv(x0)
            if abs(h) < tol:
                return x0 - h
            x0 -= h
        return x0

    def graficar_newton(self, func_str, deriv_str, x0, raiz, fig):
        x_min = raiz - 5
        x_max = raiz + 5
        x = np.linspace(x_min, x_max, 1000)
        func = lambda x: eval(func_str)
        deriv = lambda x: eval(deriv_str)

        fig.clf()
        ax = fig.add_subplot(111)
        ax.plot(x, func(x), label="f(x)")
        ax.plot(x, func(x0) + deriv(x0) * (x - x0), label="línea tangente")
        ax.axvline(raiz, color='red', linestyle='--', label='raíz')
        ax.set_xlim(x_min, x_max)
        ax.legend()
        fig.canvas.draw()

if __name__ == "__main__":
    app = NewtonApp()
    app.title("Método de Newton")
    app.mainloop()
