import tkinter as tk
import numpy as np

def gauss(A, b):
    """
    Aplica el método de eliminación de Gauss para resolver un sistema de ecuaciones lineales.
    
    Parámetros:
        A (array): Matriz de coeficientes del sistema.
        b (array): Vector de términos independientes.
    
    Retorna:
        x (array): Vector solución.
    """
    n = len(b)
    
    # Concatenar matriz A y vector b en una matriz aumentada
    Ab = np.column_stack((A, b))
    
    # Eliminación hacia adelante
    for i in range(n):
        pivot_row = Ab[i]  # fila pivot
        for j in range(i + 1, n):
            factor = Ab[j, i] / pivot_row[i]
            Ab[j] -= factor * pivot_row
            
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] / Ab[i, i]
        for j in range(i - 1, -1, -1):
            Ab[j, -1] -= Ab[j, i] * x[i]
    
    return x

# Pedir los datos al usuario por consola
n = int(input("Ingrese el tamaño de la matriz cuadrada A (n): "))
print("Ingrese los elementos de la matriz A (fila por fila separados por espacios):")
A = np.zeros((n, n))
for i in range(n):
    A[i] = list(map(float, input().split()))
b = np.array(list(map(float, input("Ingrese los términos independientes b separados por espacios: ").split())))

# Crear la ventana y el widget para mostrar la solución
window = tk.Tk()
solution_label = tk.Label(window, text="Solución del sistema:")
solution_label.grid(row=0, column=0)
solution_entry = tk.Entry(window, width=50)
solution_entry.grid(row=0, column=1)

# Resolver el sistema utilizando el método de eliminación de Gauss
solucion = gauss(A, b)

# Mostrar la solución en el widget
solution_entry.insert(0, str(solucion))

# Iniciar el bucle de eventos de la ventana
window.mainloop()