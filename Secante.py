# Método de la secante
# Ejemplo 1 (Burden ejemplo 1 p.51/pdf.61)

import numpy as np

def secante_tabla(fx,xa,tolera):
    dx = 4*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return(tabla)

# PROGRAMA ---------------------
# INGRESO
fx = lambda x: x**3 + 4*x**2 - 10

a  = 1
b  = 2
xa = 1.5
tolera = 0.001
tramos = 100

# PROCEDIMIENTO
tabla = secante_tabla(fx,xa,tolera)
n = len(tabla)
raiz = tabla[n-1,2]

# SALIDA
np.set_printoptions(precision=4)
print('[xa ,\t xb , \t xc , \t tramo]')
for i in range(0,n,1):
    print(tabla[i])
print('raiz en: ', raiz)


# GRAFICA
import matplotlib.pyplot as plt

# Calcula los puntos a graficar
xi = np.linspace(a,b,tramos+1)
fi = fx(xi)
dx = (b-xa)/2
pendiente = (fx(xa+dx)-fx(xa))/(xa+dx-xa)
b0 = fx(xa) - pendiente*xa
tangentei = pendiente*xi+b0

fxa = fx(xa)
xb = xa + dx
fxb = fx(xb)

plt.plot(xi,fi, label='f(x)')

plt.plot(xi,tangentei, label='secante')
plt.plot(xa,fx(xa),'go', label='xa')
plt.plot(xa+dx,fx(xa+dx),'ro', label='xb')
plt.plot((-b0/pendiente),0,'yo', label='xc')

plt.plot([xa,xa],[0,fxa],'m')
plt.plot([xb,xb],[0,fxb],'m')

plt.axhline(0, color='k')
plt.title('Método de la Secante')
plt.legend()
plt.grid()
plt.show()