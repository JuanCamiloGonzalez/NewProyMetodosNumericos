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

# Resolver el sistema utilizando el método de eliminación de Gauss
solucion = gauss(A, b)

# Imprimir la solución
print("La solución del sistema es:", solucion)
