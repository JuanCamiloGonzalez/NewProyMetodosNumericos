import tkinter as tk
import numpy as np

def jacobi_iteration(a, b, x_0, num_iterations, tolerance):
    n = len(a)
    x = x_0.copy()
    x_new = np.zeros(n)
    converged = False
    num_iterations_done = 0
    
    while not converged and num_iterations_done < num_iterations:
        for i in range(n):
            x_new[i] = (b[i] - sum(a[i,j]*x[j] for j in range(n) if j != i)) / a[i,i]
        if np.linalg.norm(x_new - x) < tolerance:
            converged = True
        x = x_new.copy()  # Se debe copiar x_new en x en cada iteración
        num_iterations_done += 1
    return x, num_iterations_done

def start_iteration():
    # Obtener los valores de los campos de entrada
    entries = [a11_entry, a12_entry, a13_entry, a21_entry, a22_entry, a23_entry,
               a31_entry, a32_entry, a33_entry, b1_entry, b2_entry, b3_entry]

    values = [entry.get() for entry in entries]

    # Verificar si algún campo de entrada está vacío
    if any(value == '' for value in values):
        result_entry.delete('1.0', tk.END)  # Limpiar el campo de resultados
        result_entry.insert(tk.END, "¡Por favor, llene todos los campos!")
        return

    # Convertir los valores de cadena a números flotantes
    a_values = [float(value) for value in values[:9]]
    b_values = [float(value) for value in values[9:12]]

    # Crear la matriz 'a' y el vector 'b'
    a = np.array(a_values).reshape(3, 3)
    b = np.array(b_values)

    # Obtener la estimación inicial, el número de iteraciones y la tolerancia
    x_0 = np.zeros(3)
    num_iterations = int(iterations_entry.get())
    tolerance = float(tolerance_entry.get())

    # Realizar la iteración de Jacobi
    x, num_iterations_done = jacobi_iteration(a, b, x_0, num_iterations, tolerance)

    # Mostrar la solución y el número de iteraciones realizadas
    result_entry.delete('1.0', tk.END)  # Limpiar el campo de resultados
    result_entry.insert(tk.END, f"Solución: {x}\nNúmero de iteraciones: {num_iterations_done}")

root = tk.Tk()
root.title("Interfaz gráfica del Método de Jacobi")

tk.Label(root, text="Matriz A:").grid(row=0, column=0)
tk.Label(root, text="Vector b del lado derecho:").grid(row=1, column=0)
tk.Label(root, text="Estimación inicial x_0:").grid(row=2, column=0)
tk.Label(root, text="Número de iteraciones:").grid(row=3, column=0)
tk.Label(root, text="Tolerancia:").grid(row=4, column=0)

a11_entry = tk.Entry(root, width=10)
a12_entry = tk.Entry(root, width=10)
a13_entry = tk.Entry(root, width=10)
a21_entry = tk.Entry(root, width=10)
a22_entry = tk.Entry(root, width=10)
a23_entry = tk.Entry(root, width=10)
a31_entry = tk.Entry(root, width=10)
a32_entry = tk.Entry(root, width=10)
a33_entry = tk.Entry(root, width=10)
b1_entry = tk.Entry(root, width=10)
b2_entry = tk.Entry(root, width=10)
b3_entry = tk.Entry(root, width=10)
iterations_entry = tk.Entry(root, width=10)
tolerance_entry = tk.Entry(root, width=10)

a11_entry.grid(row=0, column=1)
a12_entry.grid(row=0, column=2)
a13_entry.grid(row=0, column=3)
a21_entry.grid(row=1, column=1)
a22_entry.grid(row=1, column=2)
a23_entry.grid(row=1, column=3)
a31_entry.grid(row=2, column=1)
a32_entry.grid(row=2, column=2)
a33_entry.grid(row=2, column=3)
b1_entry.grid(row=3, column=1)
b2_entry.grid(row=3, column=2)
b3_entry.grid(row=3, column=3)
iterations_entry.grid(row=4, column=1)
tolerance_entry.grid(row=4, column=2)

tk.Button(root, text="Comenzar Iteración", command=start_iteration).grid(row=5, column=0)

result_entry = tk.Text(root, width=40, height=10)
result_entry.grid(row=6, column=0, columnspan=4)

root.mainloop()