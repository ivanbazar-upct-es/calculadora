import tkinter as tk
import math
import sympy as sp

# Variable global para guardar los últimos resultados
ultimo_resultado = None
pre_ultimo_resultado = None
estado_factorizado = False

# Función para agregar números y operadores a la pantalla
def agregar_a_pantalla(valor):
    pantalla.insert(tk.END, valor)

def borrar_pantalla():
    pantalla.delete(0, tk.END)

# Función para borrar el último carácter escrito
def borrar_ultimo_caracter():
    pantalla.delete(len(pantalla.get()) - 1, tk.END)

# Función para calcular el resultado usando eval
def calcular():
    global ultimo_resultado, pre_ultimo_resultado, estado_factorizado
    try:
        expression = pantalla.get()

        if estado_factorizado:
            # Si la expresión es factorizada, la expandimos
            x = sp.symbols('x')
            expr = sp.sympify(expression)
            expanded_expr = sp.expand(expr)
            pantalla.delete(0, tk.END)
            pantalla.insert(tk.END, str(expanded_expr))
            estado_factorizado = False  # Ya no estamos en modo factorizado
            return

        if expression.count("(") != expression.count(")"):
            pantalla.delete(0, tk.END)
            pantalla.insert(tk.END, "Error: Paréntesis desequilibrados")
            return

        # Reemplazar funciones y operadores
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("^", "**")
        expression = expression.replace("!", "math.factorial")
        expression = expression.replace("√", "math.sqrt")
        expression = expression.replace("pi", "math.pi")
        expression = expression.replace("e", "math.e")
        expression = expression.replace("sin(", "math.sin(math.radians(")
        expression = expression.replace("cos(", "math.cos(math.radians(")
        expression = expression.replace("tan(", "math.tan(math.radians(")

        # Evaluar la expresión de forma segura
        result = eval(expression, {"math": math})
        result = round(result, 4)

        # Guardar el último resultado
        pre_ultimo_resultado = ultimo_resultado
        ultimo_resultado = result

        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(result))

    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para calcular la derivada
def derivada():
    try:
        expression = pantalla.get()
        x = sp.symbols('x')
        expr = sp.sympify(expression.replace("^", "**"))
        derivada = sp.diff(expr, x)
        resultado_derivada = derivada
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado_derivada))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para calcular la integral
def integral():
    try:
        expression = pantalla.get()
        x = sp.symbols('x')
        expr = sp.sympify(expression.replace("^", "**"))
        integral = sp.integrate(expr, x)
        resultado_integral = integral
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado_integral))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para calcular el valor absoluto
def valor_absoluto():
    try:
        expression = pantalla.get()
        x = sp.symbols('x')
        expr = sp.sympify(expression.replace("^", "**"))
        abs_expr = sp.Abs(expr)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(abs_expr))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para factorizar la expresión
def factorizar():
    global estado_factorizado
    try:
        expression = pantalla.get()
        x = sp.symbols('x')
        expr = sp.sympify(expression.replace("^", "**"))

        # Factorizar, incluyendo raíces complejas
        factorizada = sp.factor(expr, extension=sp.I)

        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(factorizada))

        estado_factorizado = True  # Activamos el modo factorizado
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para el botón ANS (último resultado)
def ans():
    global ultimo_resultado
    expression = pantalla.get()
    if ultimo_resultado is not None:
        # Si ya hay algo en la pantalla, concatenamos ANS al final
        if expression:
            pantalla.insert(tk.END, str(ultimo_resultado))
        else:
            pantalla.insert(tk.END, str(ultimo_resultado))

# Función para el botón preANS (resultado anterior)
def pre_ans():
    global pre_ultimo_resultado
    expression = pantalla.get()
    if pre_ultimo_resultado is not None:
        # Si ya hay algo en la pantalla, concatenamos preANS al final
        if expression:
            pantalla.insert(tk.END, str(pre_ultimo_resultado))
        else:
            pantalla.insert(tk.END, str(pre_ultimo_resultado))
# Convertir de binario a decimal
def binario_a_decimal():
    try:
        expression = pantalla.get().strip()
        if not all(c in "01" for c in expression):  # Verifica si es un número binario válido
            raise ValueError
        resultado = int(expression, 2)  # Convierte de binario a decimal
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error: binario inválido")

# Convertir de decimal a binario
def decimal_a_binario():
    try:
        expression = pantalla.get().strip()
        if not expression.isdigit():  # Verifica si es un número decimal válido
            raise ValueError
        resultado = bin(int(expression))[2:]  # Convierte de decimal a binario
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error: decimal inválido")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("350x500")
ventana.config(bg="#f0f0f0")  # Fondo suave de color gris claro

# Pantalla
pantalla = tk.Entry(ventana, font=("Arial", 20), bd=10, relief="solid", justify="right", bg="#eaeaea", fg="#333333")
pantalla.pack(fill=tk.BOTH, padx=20, pady=20)

# Crear botones numéricos y operaciones
botones_frame = tk.Frame(ventana, bg="#f0f0f0")
botones_frame.pack(fill=tk.BOTH, expand=True)

# Lista de botones
botones = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2), ("+", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("!", 3, 0), ("0", 3, 1), ("/", 3, 2), ("^", 3, 3),
    ("pi", 4, 0), ("e", 4, 1), ("log", 4, 2), ("ln", 4, 3),
    ("(", 5, 0), (")", 5, 1), ("sin", 5, 2), ("cos", 5, 3),
    ("tan", 6, 0), ("√", 6, 1), ("x", 6, 2), ("Derivada", 6, 3),
    ("Integral", 7, 0), ("ANS", 7, 1), ("preANS", 7, 2),
    ("C", 8, 0), ("Borrar", 8, 1), ("=", 8, 2),
    ("|x|", 9, 0), ("Factorizar", 9, 1),
    ("Bin → Dec", 10, 0), ("Dec → Bin", 10, 1) 
]


# Crear los botones y asignarles funciones
for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(botones_frame, text=texto, command=calcular, bg="white", fg="black")
    elif texto == "C":  # Limpiar la pantalla
        boton = tk.Button(botones_frame, text=texto, command=borrar_pantalla, bg="white", fg="black")
    elif texto == "Borrar":  # Borrar último carácter
        boton = tk.Button(botones_frame, text=texto, command=borrar_ultimo_caracter, bg="white", fg="black")
    elif texto == "ANS":
        boton = tk.Button(botones_frame, text=texto, command=ans, bg="white", fg="black")
    elif texto == "preANS":
        boton = tk.Button(botones_frame, text=texto, command=pre_ans, bg="white", fg="black")
    elif texto == "Derivada":
        boton = tk.Button(botones_frame, text=texto, command=derivada, bg="white", fg="black")
    elif texto == "Integral":
        boton = tk.Button(botones_frame, text=texto, command=integral, bg="white", fg="black")
    elif texto == "|x|":
        boton = tk.Button(botones_frame, text=texto, command=valor_absoluto, bg="white", fg="black")
    elif texto == "Factorizar":
        boton = tk.Button(botones_frame, text=texto, command=factorizar, bg="white", fg="black")
    elif texto == "x":
        boton = tk.Button(botones_frame, text=texto, command=lambda: agregar_a_pantalla('x'))
    elif texto == "Bin → Dec":
        boton = tk.Button(botones_frame, text=texto, command=binario_a_decimal, bg="white", fg="black")
    elif texto == "Dec → Bin":
        boton = tk.Button(botones_frame, text=texto, command=decimal_a_binario, bg="white", fg="black")

    else:
        boton = tk.Button(botones_frame, text=texto, command=lambda t=texto: agregar_a_pantalla(t))
    
    boton.grid(row=fila, column=columna, sticky="nsew")

# Botón para cerrar
boton_cerrar = tk.Button(ventana, text="Cerrar", font=("Arial", 14), bg="#FF5722", fg="white", command=ventana.destroy)
boton_cerrar.pack(pady=20)

# Etiqueta 
etiqueta = tk.Label(ventana, text="Made por Iván, su pijica, sus huevicos", font=("Arial", 12), fg="#555555", bg="#f0f0f0")
etiqueta.pack(side=tk.BOTTOM, pady=10)

# Asociar la tecla Enter con la función de cálculo (igual)
ventana.bind("<Return>", lambda event: calcular())

# Configurar el grid para que los botones se ajusten bien
for i in range(5):
    botones_frame.grid_columnconfigure(i, weight=1)
    botones_frame.grid_rowconfigure(i, weight=1)

ventana.mainloop()
