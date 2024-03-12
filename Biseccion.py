import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import matplotlib.pyplot as plt

class Biseccion(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Método de bisección')

        # Etiqueta y campo de texto para la función
        func_label = QLabel(self)
        func_label.setText('Función:')
        func_label.move(20, 20)
        self.func_edit = QLineEdit(self)
        self.func_edit.move(80, 20)
        self.func_edit.resize(200, 20)
        self.func_edit.setText('x**3+2*x+10*x-20')

        # Etiqueta y campo de texto para el límite inferior
        a_label = QLabel(self)
        a_label.setText('Límite inferior:')
        a_label.move(20, 60)
        self.a_edit = QLineEdit(self)
        self.a_edit.move(120, 60)
        self.a_edit.resize(160, 20)
        self.a_edit.setText('0')

        # Etiqueta y campo de texto para el límite superior
        b_label = QLabel(self)
        b_label.setText('Límite superior:')
        b_label.move(20, 100)
        self.b_edit = QLineEdit(self)
        self.b_edit.move(120, 100)
        self.b_edit.resize(160, 20)
        self.b_edit.setText('4')

        # Botón para calcular la raíz
        calc_button = QPushButton('Calcular', self)
        calc_button.move(100, 140)
        calc_button.resize(120, 30)
        calc_button.clicked.connect(self.calcular_raiz)
        self.error_label = QLabel(self)
        self.error_label.move(20, 220)
        self.setGeometry(100, 100, 300, 220)
        self.show()

    def calcular_raiz(self):
        try:
            # Obtener los datos ingresados por el usuario
            funcion = self.func_edit.text()
            a = float(self.a_edit.text())
            b = float(self.b_edit.text())

            # Crear la función y graficarla
            x = np.linspace(a, b, 1000)
            y = eval(funcion)
            plt.plot(x, y)
            plt.axhline(y=0, color='k')
            plt.axvline(x=a, color='r')
            plt.axvline(x=b, color='r')

            # Aplicar el método de bisección
            fa = eval(funcion.replace('x', str(a)))
            fb = eval(funcion.replace('x', str(b)))
            if fa * fb > 0:
                QMessageBox.warning(self, "Error", "La función no cambia de signo en el intervalo dado.")
                return
            for i in range(100):
                c = (a + b) / 2
                fc = eval(funcion.replace('x', str(c)))
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
                if abs(b - a) < 1e-6:
                    break
            # Calcular el error relativo
            x_true = abs(b - a)  # Supongamos que la raíz verdadera es 1.0
            error_rel = abs(c - x_true) / abs(c)
            # Mostrar la raíz encontrada
            root_label = QLabel(self)
            root_label.setText(f"La raíz encontrada es: {c:.6f}")
            root_label.move(20, 180)
            root_label.show()
            error_label = QLabel(self)
            error_label.setText(f"El error relativo es: {x_true:.6f}")
            error_label.move(20, 200)
            error_label.show()
            
            # Mostrar la gráfica
            plt.plot(c, 0, 'ro')
            plt.show()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ocurrió un error al calcular la raíz: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bisec = Biseccion()
    sys.exit(app.exec_())
