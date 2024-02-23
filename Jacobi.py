import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    """
    Método de Jacobi para resolver sistemas de ecuaciones lineales.
    
    Parámetros:
        A (array): Matriz de coeficientes del sistema.
        b (array): Vector de términos independientes.
        x0 (array): Estimación inicial.
        tol (float): Tolerancia para el criterio de parada.
        max_iter (int): Número máximo de iteraciones permitidas.
    
    Retorna:
        x (array): Vector solución.
        num_iter (int): Número de iteraciones realizadas.
    """
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)
    num_iter = 0
    while num_iter < max_iter:
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new.copy()
        num_iter += 1
    return x, num_iter

# Pedir los datos al usuario por consola
n = int(input("Ingrese el tamaño de la matriz cuadrada A (n): "))
print("Ingrese los elementos de la matriz A (fila por fila):")
A = np.zeros((n, n))
for i in range(n):
    A[i] = list(map(float, input().split()))
b = np.array(list(map(float, input("Ingrese los términos independientes b separados por espacios: ").split())))
x0 = np.array(list(map(float, input("Ingrese la estimación inicial x0 separada por espacios: ").split())))

# Resolver el sistema utilizando el método de Jacobi
solucion, num_iteraciones = jacobi(A, b, x0)

# Imprimir la solución y el número de iteraciones realizadas
print("Solución encontrada:", solucion)
print("Número de iteraciones:", num_iteraciones)
