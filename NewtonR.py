# Método de Newton-Raphson

import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx  = lambda x: x**3 + 2*(x**2) + 10*x - 20
dfx = lambda x: 3*(x**2) + 4*x +10
x = np.linspace(-10,10,1000)
x0 = 1
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
    print('g(x)', gx)
    tabla.append([xi,xnuevo, deltax ,gx])
    xi = xnuevo
    print('Deltax',deltax)

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)
fi = fx(x)
# SALIDA
print(['xi', 'xnuevo', 'deltax','g(x)'])
np.set_printoptions(precision = 4)
np.set_printoptions(suppress=True)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',deltax)
plt.plot(x,fi,'b')
plt.plot(xi,0,'ro')
plt.axvline(x=0, ymin=-10, ymax=10)
plt.axhline(y=0, xmin=-10, xmax=10)
plt.grid()
plt.show()