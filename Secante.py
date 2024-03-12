# INGRESO
fx  = lambda x: x**3 + 2*(x**2) + 10*x - 20
dfx = lambda x: 3*(x**2) + 4*x +10
x0 = float(input("Ingrese el valor inicial: "))
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
fi = fx(np.linspace(-10,10,1000))

# SALIDA
print(f"Raíz encontrada: {xi:.4f}\nError: {deltax:.4e}")

# Mostrar la gráfica
plt.plot(np.linspace(-10,10,1000),fi,'b')
plt.plot(xi,0,'ro')
plt.axvline(x=0, ymin=-10, ymax=10)
plt.axhline(y=0, xmin=-10, xmax=10)
plt.grid()
plt.show()