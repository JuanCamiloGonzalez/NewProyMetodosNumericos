import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import sin, cos, tan, asin, acos, atan, pi

def secant_method(f, x0, x1, tol, max_iter):
    """
    Implementación del método de la secante para encontrar una raíz de una función.

    Parámetros:
    f: función de la cual se desea encontrar una raíz.
    x0: valor inicial para la iteración.
    x1: valor inicial para la iteración.
    tol: tolerancia para la precisión de la solución.
    max_iter: número máximo de iteraciones permitidas.

    Retorna:
    x: aproximación de la raíz encontrada.
    """

    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        try:
            x = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
            
        except ZeroDivisionError:
            root.geometry('650x180')
            root_label.config(text="No se puede analizar la ecuacion")
        else:
            if abs(x - x1) < tol:
                error_label.config(text="El error porcentual es: {}".format(x-x1))
                return x
            x0 = x1
            x1 = x
            print(f"Iteración {i+1}: x={x}, f(x)={f(x)}")

    raise ValueError(f"No se encontró una raíz después de {max_iter} iteraciones")


def find_root():
    error_label.config(text="")
    try:
        # Obtenemos los valores ingresados por el usuario
        f = lambda x: eval(f_str)
        f_str = f_entry.get()
        x0 = float(x0_entry.get())
        x1 = float(x1_entry.get())
        tol = float(tol_entry.get())
        max_iter = int(max_iter_entry.get())
        # Llamamos al método de la secante para encontrar la raíz
        x_root = secant_method(f, x0, x1, tol, max_iter)
        if x1 < x0:
            root.geometry('650x180')
            root_label.config(text="Error: x1 debe ser mayor o igual que x0.")
            return
        else:
            root_label.config(text=f"La raíz encontrada es x={x_root}")
            # Graficamos la función y mostramos la raíz encontrada y la línea horizontal en y=0
            if x_root > x1:
                x_vals = np.linspace(x0, x_root, 1000)
            elif x_root<x0:
                x_vals = np.linspace(x_root, x1, 1000) 
            else:
                x_vals = np.linspace(x0, x1, 1000)
            y_vals = f(x_vals)
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals)
            ax.plot(x_root, f(x_root), 'ro')
            ax.axhline(y=0, color='black', linestyle='--')
            ax.set_title("Gráfica de f(x)")
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=10, column=0, columnspan=3)
            root.geometry('650x650')
    except Exception as e:
        root.geometry('650x180')
        root_label.config(text="No se puede analizar la ecuacion, Verifique que los datos sean válidos")

def validate_float_input_positive(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

def validate_float_input_negative(input):
    try:
        float(input)
        return True
    except ValueError:
        if input == "-" and x0_entry.index("insert") == 0 or x1_entry.index("insert") == 0:
            return True
        return False

# Creamos la ventana principal y los elementos de la interfaz gráfica
root = tk.Tk()
validate_float_negative = root.register(validate_float_input_negative)
validate_float_positive = root.register(validate_float_input_positive)
root.title("Método de la secante")
root.geometry('650x180')
f_label = tk.Label(root, text="Ingresa la función f(x):")
f_label.grid(row=0, column=0)
f_entry = tk.Entry(root)
f_entry.grid(row=0, column=1)
f_entry.insert(0,("np.sin(x)"))

x0_label = tk.Label(root, text="Ingresa el valor inicial x0:")
x0_label.grid(row=1, column=0)
x0_entry = tk.Entry(root, validate="key", validatecommand=(validate_float_negative, '%P'))
x0_entry.grid(row=1, column=1)
x0_entry.insert(0,"-1")

x1_label = tk.Label(root, text="Ingresa el valor inicial x1:")
x1_label.grid(row=2, column=0)
x1_entry = tk.Entry(root, validate="key", validatecommand=(validate_float_negative, '%P'))
x1_entry.grid(row=2, column=1)
x1_entry.insert(0,"1")

tol_label = tk.Label(root, text="Ingresa la tolerancia:")
tol_label.grid(row=3, column=0)
tol_entry = tk.Entry(root, validate="key", validatecommand=(validate_float_positive, '%P'))
tol_entry.grid(row=3, column=1)
tol_entry.insert(0,"0.0001")

max_iter_label = tk.Label(root, text="Ingresa el número máximo de iteraciones:")
max_iter_label.grid(row=4, column=0)
max_iter_entry = tk.Entry(root, validate="key", validatecommand=(validate_float_positive, '%P'))
max_iter_entry.insert(0, "50")
max_iter_entry.grid(row=4, column=1)

find_button = tk.Button(root, text="Encontrar raíz", command=find_root)
find_button.grid(row=7, column=0)

root_label = tk.Label(root, text="")
root_label.grid(row=8)
error_label = tk.Label(root, text="")
error_label.grid(row=9)

root.mainloop()
