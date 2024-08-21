import tkinter as tk

# Calculadora basica
# 1. Crear menu con opciones de suma, resta, multiplicacion y division
# 2. Crear las funciones para cada una de las operaciones

# def guardar_operandos():
#     print("Ingrese operando 1: ")
#     a = int(input())
#     print("Ingrese operando 2: ")
#     b = int(input())
#     return a, b

def sumar():
    a = float(numero_1.get())
    b = float(numero_2.get())
    resultado = a + b
    etiqueta_1.config(text=f"{a} + {b} = {resultado}")

def restar():
    a = float(numero_1.get())
    b = float(numero_2.get())
    resultado = a - b
    etiqueta_1.config(text=f"{a} - {b} = {resultado}")

def multiplicar():
    a = float(numero_1.get())
    b = float(numero_2.get())
    resultado = a * b
    etiqueta_1.config(text=f"{a} x {b} = {resultado}")

def dividir():
    a = float(numero_1.get())
    b = float(numero_2.get())
    if b == 0:
        etiqueta_1.config(text=f"ERROR: No se puede dividir por 0.")
    else:
        resultado = a / b
        etiqueta_1.config(text=f"{a} / {b} = {resultado}")

def limpiar():
    etiqueta_1.config(text="")
    numero_1.delete(0, tk.END)
    numero_2.delete(0, tk.END)

# paso 1
# print("Ingrese la operacion a realizar: ")
# print("1. Suma\n2. Resta\n3. Multiplicar\n4. Dividir\n0. Salir")
# opcion = int(input())

# while opcion != 0:
#     a, b = guardar_operandos()
#     if opcion == 1:
#         resultado = sumar(a, b)
#         print(f"{a} + {b} = {resultado}")
#     elif opcion == 2:
#         resultado = restar(a, b)
#         print(f"{a} - {b} = {resultado}")
#     elif opcion == 3:
#         resultado = multiplicar(a, b)
#         print(f"{a} x {b} = {resultado}")
#     elif opcion == 4:
#         resultado = dividir(a, b)
#         if(resultado != None):
#             print(f"{a} \ {b} = {resultado}")
#     elif opcion == 0:
#         break
#     else:
#         print("Ingrese una opcion valida... ")

#     print("Ingrese la operacion a realizar: ")
#     print("1. Suma\n2. Resta\n3. Multiplicar\n4. Dividir\n0. Salir")
#     opcion = int(input())



ventana = tk.Tk()
ventana.title("Calculadora basica")
ventana.geometry("300x300")

numero_1 = tk.Entry(ventana, width=30)
numero_1.pack(pady=10)
numero_1.pack(padx=10)

numero_2 = tk.Entry(ventana, width=30)
numero_2.pack(pady=10)
numero_2.pack(padx=10)

cuadro = tk.Frame(ventana)
cuadro.pack(pady=10)

btn_suma = tk.Button(cuadro, text="+", command=sumar)
btn_suma.pack(side=tk.LEFT, padx=3, pady=3)
btn_resta = tk.Button(cuadro, text="-", command=restar)
btn_resta.pack(side=tk.LEFT, padx=3, pady=3)
btn_multiplicar = tk.Button(cuadro, text="x", command=multiplicar)
btn_multiplicar.pack(side=tk.LEFT, padx=3, pady=3)
btn_dividir = tk.Button(cuadro, text="/", command=dividir)
btn_dividir.pack(side=tk.LEFT, padx=3, pady=3)
btn_clear = tk.Button(cuadro, text="C", command=limpiar)
btn_clear.pack(side=tk.LEFT, padx=3, pady=3)

cuadro.pack(anchor=tk.CENTER)

etiqueta_1 = tk.Label(ventana)
etiqueta_1.pack(pady=20)

ventana.mainloop()