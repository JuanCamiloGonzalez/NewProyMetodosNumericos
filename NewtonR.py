import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson():
    # INGRESO
    fx  = lambda x: x**3 + 2*(x**2) + 10*x - 20
    dfx = lambda x: 3*(x**2) + 4*x +10
    x = np.linspace(-10,10,1000)
    x0 = float(entry.get())
    error = 0.001

    # PROCEDIMIENTO
    tabla = []
    deltax = 0.002
    xi = x0
    while (error<deltax):
        xnuevo = xi - fx(xi)/dfx(xi)
        deltax = abs(xnuevo-xi)
        p1=dfx(xi)**2-fx(xi)*((6*xi)+4)
        gx= abs((p1/dfx(xi)**2)-1)
        tabla.append([xi,xnuevo, deltax ,gx])
        xi = xnuevo

    # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    n = len(tabla)
    fi = fx(x)

    # SALIDA
    result_label = tk.Label(window, text=f"Raíz encontrada: {xi:.4f}\nError: {deltax:.4e}")
    result_label.grid(row=n+3, column=0, columnspan=4)

# Crear la ventana
window = tk.Tk()
window.title("Método de Newton-Raphson")

# Crear los widgets
entry_label = tk.Label(window, text="Valor inicial:")
entry_label.grid(row=0, column=0)
entry = tk.Entry(window, width=10)
entry.insert(0, "1")
entry.grid(row=0, column=1)

plot_button = tk.Button(window, text="Plotar", command=lambda: [newton_raphson(), plt.show()])
plot_button.grid(row=n+2, column=0, columnspan=4)

# Iniciar el bucle de eventos
window.mainloop()

# Mostrar la gráfica
plt.plot(x,fi,'b')
plt.plot(xi,0,'ro')
plt.axvline(x=0, ymin=-10, ymax=10)
plt.axhline(y=0, xmin=-10, xmax=10)
plt.grid()
plt.show()