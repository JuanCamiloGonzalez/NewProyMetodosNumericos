import os
import sys
from PyQt5 import QtGui
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sympy as sym
class Simpson(QWidget):
    def __init__(self):
        super().__init__()

        # Crear los widgets para la interfaz
        self.funcion_label = QLabel('Función:')
        self.funcion_edit = QLineEdit()
        self.lim_inf_label = QLabel('Límite inferior:')
        self.lim_inf_edit = QLineEdit()
        self.lim_sup_label = QLabel('Límite superior:')
        self.lim_sup_edit = QLineEdit()
        self.intervalos_label = QLabel('Número de intervalos:')
        self.intervalos_edit = QLineEdit()
        self.calcular_button = QPushButton('Calcular')
        self.resultado_label = QLabel()
        self.grafica = QLabel()

        # Crear el layout de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.funcion_label)
        layout.addWidget(self.funcion_edit)
        layout.addWidget(self.lim_inf_label)
        layout.addWidget(self.lim_inf_edit)
        layout.addWidget(self.lim_sup_label)
        layout.addWidget(self.lim_sup_edit)
        layout.addWidget(self.intervalos_label)
        layout.addWidget(self.intervalos_edit)
        layout.addWidget(self.calcular_button)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.grafica)
        self.setLayout(layout)

        # Conectar la señal del botón con el slot correspondiente
        self.calcular_button.clicked.connect(self.calcular)

    def calcular(self):
        # Obtener los datos ingresados por el usuario
        try:
            funcion = self.funcion_edit.text()
            lim_inf = float(self.lim_inf_edit.text())
            lim_sup = float(self.lim_sup_edit.text())
            intervalos = int(self.intervalos_edit.text())

            # Validar que el número de intervalos sea par
            if intervalos % 2 != 0:
                raise ValueError('El número de intervalos debe ser par.')

            # Calcular el ancho de los intervalos
            h = (lim_sup - lim_inf) / intervalos

            # Calcular la suma de los términos impares de la fórmula de Simpson
            suma_impares = 0
            for i in range(1, intervalos, 2):
                x = lim_inf + i * h
                suma_impares += eval(funcion.replace('x', str(x)))

            # Calcular la suma de los términos pares de la fórmula de Simpson
            suma_pares = 0
            for i in range(2, intervalos, 2):
                x = lim_inf + i * h
                suma_pares += eval(funcion.replace('x', str(x)))

            # Calcular el área
            area = h / 3 * (eval(funcion.replace('x', str(lim_inf))) + 4 * suma_impares + 2 * suma_pares + eval(funcion.replace('x', str(lim_sup))))

            # Mostrar el resultado en la interfaz
            x = sym.Symbol('x')
            funcion_sym = sym.sympify(funcion)
            valor_exacto = float(sym.integrate(funcion_sym, (x, lim_inf, lim_sup)))
            error_porcentual = abs((valor_exacto - area) / valor_exacto) * 100
            self.resultado_label.setText(f'Área encontrada: {area} \nError porcentual: {error_porcentual:.8f}%')

            # Crear la gráfica

            x = np.linspace(lim_inf, lim_sup, 100)
            y = eval(funcion.replace('x', 'x'))
            plt.plot(x, y)
            plt.fill_between(x, y, where=(x >= lim_inf) & (x <= lim_sup), alpha=0.5)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title(f'Área = {area}')
            plt.savefig('grafica.png')

            # Mostrar la gráfica en la interfaz
            pixmap = QtGui.QPixmap('grafica.png')
            self.grafica.setPixmap(pixmap)
            plt.cla()

        except ValueError as error:
            QMessageBox.critical(self, 'Error', str(error))
        except ZeroDivisionError as error:
            QMessageBox.critical(self, 'Error', 'El límite inferior y el límite superior no pueden ser iguales.')
        except Exception as error:
            QMessageBox.critical(self, 'Error', f'Ha ocurrido un error: {str(error)}')

if __name__ == '__main__':
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear la ventana de la interfaz
    ventana = Simpson()
    ventana.setWindowTitle('Método de Simpson')

    # Mostrar la ventana
    ventana.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())