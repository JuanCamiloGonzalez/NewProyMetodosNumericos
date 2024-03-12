from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import *

class VentanaPuntoFijo:
    def __init__(self):
        self.root = Tk()
        self.root.title("Método de Punto Fijo")

        self.frame_funcion = Frame(self.root)
        self.frame_funcion.pack(pady=5)

        self.label_funcion = Label(self.frame_funcion, text="Ingrese la función g(x):")
        self.label_funcion.pack(side=LEFT)

        self.entry_funcion = Entry(self.frame_funcion, width=30)
        self.entry_funcion.pack(side=LEFT)

        self.frame_valor_inicial = Frame(self.root)
        self.frame_valor_inicial.pack(pady=5)

        self.label_valor_inicial = Label(self.frame_valor_inicial, text="Ingrese el valor inicial x0:")
        self.label_valor_inicial.pack(side=LEFT)

        self.entry_valor_inicial = Entry(self.frame_valor_inicial, width=10)
        self.entry_valor_inicial.pack(side=LEFT)

        self.frame_botones = Frame(self.root)
        self.frame_botones.pack(pady=5)

        self.boton_calcular_raiz = Button(self.frame_botones, text="Calcular raíz", command=self.calcular_raiz)
        self.boton_calcular_raiz.pack(side=LEFT)

        self.boton_salir = Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.boton_salir.pack(side=LEFT)

        self.frame_resultados = Frame(self.root)
        self.frame_resultados.pack(pady=5)

        self.label_valor_raiz = Label(self.frame_resultados, text="")
        self.label_valor_raiz.pack()

        self.label_valor_error = Label(self.frame_resultados, text="")
        self.label_valor_error.pack()

        self.frame_grafica = Frame(self.root)
        self.frame_grafica.pack(pady=5)

        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("g(x)")
        self.ax.grid()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_grafica)
        self.canvas.get_tk_widget().pack()

    def calcular_puntos(self, g, x0, n):
        puntos = []
        x = x0
        for i in range(n):
            puntos.append((x, g(x)))
            x = g(x)
        return puntos

    def calcular_raiz(self):
 
        try:
            g = lambda x: eval(self.entry_funcion.get().replace('sqrt', 'np.sqrt').replace('pow', 'np.power'))
            x0 = float(self.entry_valor_inicial.get())
            tolerancia = 1e-6
            error = 1

            x_ant = x0
            x_sig = g(x_ant)
            i = 0

            while error > tolerancia and i < 1000:
                x_ant = x_sig
                x_sig = g(x_ant)
                error = abs(x_sig - x_ant)
                i += 1

            if i == 1000:
                raise Exception("Se alcanzó el máximo número de iteraciones sin convergencia")

            self.label_valor_raiz.config(text=f"La raíz encontrada es: {x_sig:.6f}")
            self.label_valor_error.config(text=f"El error relativo es: {error:.6f}")

            x = np.linspace(x0 - 1, x0 + 1, 1000)
            y = g(x)

            self.ax.clear()
            self.ax.plot(x, x, color="gray", linestyle="--")
            self.ax.plot(x, y, color="red", linewidth=2)
            self.ax.plot(x_sig, x_sig, marker="o", color="blue")
            self.ax.set_xlim([x0 - 1, x0 + 1])
            self.ax.set_ylim([x0 - 1, x0 + 1])
            self.ax.legend(["y = x", "g(x)", "Raíz"])
            self.canvas.draw()

        except Exception as e:
            self.label_valor_raiz.config(text=str(e))
            self.label_valor_error.config(text="")
            self.ax.clear()
            self.canvas.draw()
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    ventana_punto_fijo = VentanaPuntoFijo()
    ventana_punto_fijo.run()