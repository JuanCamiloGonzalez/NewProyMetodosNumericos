import tkinter as tk
import matplotlib.pyplot as plt
import argparse

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = [0] * n
    iter_count = 0
    errors = []
    for k in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]
        r = [b[i] - sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
        err = max(abs(r[i]) for i in range(n))
        errors.append(err)
        if err < tol:
            return x, iter_count, errors
        iter_count += 1
    raise ValueError('El método no converge después de %d iteraciones.' % max_iter)
         
def solve():
    warning_label.config(text="")
    error_label.config(text="")
    iter_label.config(text="")
    for i in range(n):
        result[i].configure(text="")
    try:
        # Obtener los datos ingresados por el usuario
        A = [[float(entry_A[i][j].get()) for j in range(n)] for i in range(n)]
        b = [float(entry_b[i].get()) for i in range(n)]
        x0 = [float(entry_x0[i].get()) for i in range(n)]
        tol = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        # Resolver el sistema de ecuaciones lineales
        try:
            x, iter_count, errors = gauss_seidel(A, b, x0, tol, max_iter)
            for i in range(n):
                result[i].configure(text='%.4f' % x[i])
            iter_label.config(text='Iteraciones: %d' % iter_count)
            error_label.config(text='Error: %.4e' % errors[-1])
            print(errors)
            # Graficar la evolución del error
            plt.plot(range(iter_count), errors)
            plt.xlabel('Iteración')
            plt.ylabel('Error')
            plt.show()
        except ValueError as e:
            warning_label.config("")
    except ValueError:
        warning_label.config(text="Todos los campos deben ser numéricos.")

# Crear la interfaz gráfica de usuario
root = tk.Tk()
root.title('Método de Gauss-Seidel')
# Crear los widgets de entrada y salida
# n = 2


parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=4, help='Valor por defecto es 5')
args = parser.parse_args()

# Utilizar el valor proporcionado por el usuario o el valor por defecto
n = args.n

entry_A = [[None]*n for i in range(n)]
entry_b = [None]*n
entry_x0 = [None]*n
for i in range(n):
    for j in range(n):
        label = tk.Label(root, text='A[%d][%d] =' % (i+1, j+1))
        label.grid(row=i, column=2*j)
        entry_A[i][j] = tk.Entry(root, width=8)
        entry_A[i][j].grid(row=i, column=2*j+1)
    label = tk.Label(root, text='b[%d] =' % (i+1))
    label.grid(row=i, column=2*n)
    entry_b[i] = tk.Entry(root, width=8)
    entry_b[i].grid(row=i, column=2*n+1)
    label = tk.Label(root, text='x0[%d] =' % (i+1))
    label.grid(row=n+i, column=0)
    entry_x0[i] = tk.Entry(root, width=8)
    entry_x0[i].grid(row=n+i, column=1)
    entry_x0[i].insert(0, '0')

tol_label = tk.Label(root, text='Tolerancia:')
tol_label.grid(row=2*n+1, column=0)
entry_tol = tk.Entry(root, width=8)
entry_tol.insert(0,'0.0001')
entry_tol.grid(row=2*n+1, column=1)
max_iter_label = tk.Label(root, text='Iteraciones máximas:')
max_iter_label.grid(row=2*n+2, column=0)
entry_max_iter = tk.Entry(root, width=8)
entry_max_iter.insert(0, '50')
entry_max_iter.grid(row=2*n+2, column=1)
solve_button = tk.Button(root, text='Resolver', command=solve)
solve_button.grid(row=2*n+3, column=0)
warning_label = tk.Label(root, text="")
warning_label.grid(row=11, column=0)
iter_label = tk.Label(root, text="")
iter_label.grid(row=12, column=0)
error_label = tk.Label(root, text="")
error_label.grid(row=13, column=0)
result = [None]*n
for i in range(n):
    label = tk.Label(root, text='x[%d] =' % (i+1))
    label.grid(row=n+i, column=2*n+2)
    result[i] = tk.Label(root, width=8, bg='white')
    result[i].grid(row=n+i, column=2*n+3)

root.mainloop()