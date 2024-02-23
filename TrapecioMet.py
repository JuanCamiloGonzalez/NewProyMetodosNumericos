# Integración: Regla de los trapecios
# Usando una función fx()
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 10
tramos = 5

# PROCEDIMIENTO
# Regla del Trapecio
# Usando tramos equidistantes en intervalo
h = (b-a)/tramos
xi = a
suma = fx(xi)
for i in range(0,tramos-1,1):
    xi = xi + h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area = h*(suma/2)

# SALIDA
print('tramos: ', tramos)
print('Integral: ', area)



# GRAFICA
# Puntos de muestra
muestras = tramos + 1
xi = np.linspace(a,b,muestras)
fi = fx(xi)
# Linea suave
muestraslinea = tramos*10 + 1
xk = np.linspace(a,b,muestraslinea)
fk = fx(xk)

# Graficando
plt.plot(xk,fk, label ='f(x)')
plt.plot(xi,fi, marker='o',
         color='orange', label ='muestras')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Integral: Regla de Trapecios')
plt.legend()

# Trapecios
plt.fill_between(xi,0,fi, color='g')
for i in range(0,muestras,1):
    plt.axvline(xi[i], color='w')

plt.show()