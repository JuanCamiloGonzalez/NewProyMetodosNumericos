import tkinter as tk
from math import sin, cos, tan, asin, acos, atan, e, pi
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import sympify, diff

def trapezoidal_rule():
    # Obtener los valores ingresados por el usuario
    function = function_entry.get()
    a = float(lower_limit_entry.get())
    b = float(upper_limit_entry.get())
    n = int(num_intervals_entry.get())

    # Crear una lista de los puntos x e y de la función

    message_label.config(text="")
    x = [a + (b - a) * i / n for i in range(n + 1)]
    try:
        window.geometry('650x800')
        y = [eval(function.replace('x', str(xi))) for xi in x]
        # Calcular el área usando el método del trapecio
        fig = Figure(figsize=(6, 6), dpi=100)
        plot = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=window)
        if n==1:
            area = 0.5 * (b - a) * sum(abs(y[i+1] - y[i]) for i in range(n))
        elif n>1:
            delta_x = (b - a) / n
            area = 0.5 * delta_x * (y[0] + 2 * sum(y[1:-1]) + y[-1])

        plot.plot(x, y)
        plot.fill_between(x, y, where=[(a <= xi <= b) for xi in x], alpha=0.2)
        plot.set_xlabel('x')
        plot.set_ylabel('y')
        plot.set_title(f'Área: {area:.4f}')
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0, columnspan=3)
    except Exception as e:
        print(e)
        window.geometry('650x150')
        error_label.config(text="")
        message_label.config(text="Lo sentimos, no podemos trabajar con esa ecuación")
    # Mostrar la gráfica de la función y el área calculada
    f = sympify(function)
    f2 = diff(diff(f))
    xi_values = [a + i * (b - a) / n for i in range(n + 1)]
    max_f2 = max([abs(f2.subs('x', xi)) for xi in xi_values])
    error = (b - a)**3 / (12 * n**2) * max_f2 * (b - a) / n
    error_label.config(text="Error: {}".format(error) )
def validate_inputs():
    try:
        # Obtener los valores de entrada
        lower_limit = float(lower_limit_entry.get())
        upper_limit = float(upper_limit_entry.get())

        # Verificar que el límite inferior sea menor o igual que el límite superior
        if lower_limit >= upper_limit:
            window.geometry('650x150')
            error_label.config(text="")
            message_label.config(text='El límite inferior debe ser menor que el límite superior.')
        else: 
            trapezoidal_rule()
    except:
        window.geometry('650x150')
        message_label.config(text="Llene los campos adecuadamente")
        error_label.config(text="")
def validate_float_input_positive(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def validate_float_input_negative(input):
    try:
        float(input)
        return True
    except ValueError:
        if input == "-" and lower_limit_entry.index("insert") == 0:
            return True
        return False
# Crear la ventana de la aplicación
window = tk.Tk()
validate_float_negative = window.register(validate_float_input_negative)
validate_float_positive = window.register(validate_float_input_positive)
window.geometry('650x150')
window.title('Método del Trapecio')
# Crear los campos de entrada para la función, el límite inferior, el límite superior y el número de intervalos
function_label = tk.Label(window, text='Función:')
function_label.grid(row=0, column=0)
function_entry = tk.Entry(window)
function_entry.grid(row=0, column=1)
function_entry.insert(0,"sin(x)")

lower_limit_label = tk.Label(window, text='Límite inferior:')
lower_limit_label.grid(row=1, column=0)
lower_limit_entry = tk.Entry(window, validate="key", validatecommand=(validate_float_negative, '%P'))
lower_limit_entry.grid(row=1, column=1)
lower_limit_entry.insert(0,"0")

upper_limit_label = tk.Label(window, text='Límite superior:')
upper_limit_label.grid(row=2, column=0)
upper_limit_entry = tk.Entry(window, validate="key", validatecommand=(validate_float_negative, '%P'))
upper_limit_entry.grid(row=2, column=1)
upper_limit_entry.insert(0,"4")

num_intervals_label = tk.Label(window, text='Número de intervalos:')
num_intervals_label.grid(row=3, column=0)
num_intervals_entry = tk.Entry(window, validate="key", validatecommand=(validate_float_positive, '%P'))
num_intervals_entry.grid(row=3, column=1)
num_intervals_entry.insert(0,"50")

message_label = tk.Label(window)
message_label.grid(row=4, column=0)
error_label = tk.Label(window)
error_label.grid(row=5, column=0)
# Crear el botón para calcular el área usando el método del trapecio
calculate_button = tk.Button(window, text='Calcular', command=validate_inputs)
calculate_button.grid(row=6, column=0)

# Mostrar la ventana de la aplicación
window.mainloop()
