import tkinter as tk
from tkinter import PhotoImage, messagebox

class PowerFitApp(tk.Tk):

    # --------- VENTANAS CONFIGURACION GENERAL ------------ 

    def __init__(self):
        super().__init__()
        self.title("PowerFit - Tu App de ejercicios")
        
        # Imagen de fondo para la pantalla de inicio
        self.imagen_inicio = PhotoImage(file='imagenes/power_fit.png')
 
        # Configuración de la ventana principal
        self.geometry(f"{self.imagen_inicio.width()}x{self.imagen_inicio.height()}")
        self.resizable(False, False)
        self.configure(bg='white')

        # Tamaño de los frames
        self.frame_width = self.imagen_inicio.width()
        self.frame_height = self.imagen_inicio.height()

        # Frames para la pantalla de inicio, inputs y resultados
        self.frame_inicio = tk.Frame(self, bg='white', width=self.frame_width, height=self.frame_height)
        self.frame_inputs = tk.Frame(self, bg='white', width=self.frame_width, height=self.frame_height)
        self.frame_resultados = tk.Frame(self, bg='white', width=self.frame_width, height=self.frame_height)

        # Crear las pantallas
        self.crear_pantalla_inicio()
        self.crear_pantalla_inputs()
        self.crear_pantalla_resultados()

        self.mostrar_pantalla_inicio()


    # --------- VENTANA DE INICIO ------------ 

    def crear_pantalla_inicio(self):
        tk.Label(self.frame_inicio, image=self.imagen_inicio).place(relx=0.5, rely=0.5, anchor='center')

        # Botón para ir a la pantalla de inputs
        tk.Button(self.frame_inicio, text="Comenzar", command=self.mostrar_pantalla_inputs, font=("Roboto", 14, "bold"), fg='white', bg='#00FFB4').place(relx=0.5, rely=0.8, anchor='center')


    # --------- VENTANA INPUTS ------------ 

    def crear_pantalla_inputs(self):
        # Titulo principal
        tk.Label(self.frame_inputs, text="Ready?", bg='white', font=("Roboto", 20, "bold")).place(relx=0.1, rely=0.05, anchor='w')
        tk.Label(self.frame_inputs, text="Empecemos", bg='white', font=("Roboto", 20, "bold")).place(relx=0.1, rely=0.12, anchor='w')

        # Inputs
        self.crear_campo_entrada("Nombre completo", 0.25, "nombre")
        self.crear_campo_entrada("Edad (años)", 0.35, "edad")
        self.crear_campo_entrada("Peso (kg)", 0.45, "peso")
        self.crear_campo_entrada("Estatura (m)", 0.55, "estatura")

        # Boton enviar
        tk.Button(self.frame_inputs, text="Enviar", command=self.enviar_datos, font=("Roboto", 14, "bold"), fg='white', bg='#00FFB4').place(relx=0.5, rely=0.85, anchor='center', relwidth=0.3)

    def crear_campo_entrada(self, texto, posicion_y, atributo):
        tk.Label(self.frame_inputs, text=texto, bg='white', font=("Roboto", 12)).place(relx=0.5, rely=posicion_y, anchor='center')
        setattr(self, f"entry_{atributo}", tk.Entry(self.frame_inputs, font=("Roboto", 12), fg='black', bg='white'))
        getattr(self, f"entry_{atributo}").place(relx=0.5, rely=posicion_y + 0.05, anchor='center', relwidth=0.6)

    def mostrar_pantalla_inicio(self):
        self.frame_inicio.pack(expand=True, fill='both')

    def mostrar_pantalla_inputs(self):
        self.frame_inicio.pack_forget()
        self.frame_inputs.pack(expand=True, fill='both')

    def mostrar_pantalla_resultados(self):
        self.frame_inputs.pack_forget()
        self.frame_resultados.pack(expand=True, fill='both')

    # --------- Calculo de IMC con inputs ------------     

    def calcular_imc(self, peso, estatura):
        return peso / (estatura ** 2)
    
    # --------- Asignación de rutinas ------------ 

    def determinar_rutina(self, imc):
        if imc < 18.5:
            return "Ganar masa muscular"
        elif 18.5 <= imc < 25:
            return "Mantenimiento"
        elif imc > 25:
            return "Perder peso"

    # --------- Manejo de errores / inputs ------------ 

    def enviar_datos(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        peso = self.entry_peso.get()
        estatura = self.entry_estatura.get()

        if not nombre or not edad or not peso or not estatura:
            messagebox.showerror("Error", "Complete todos los campos por favor")
            return
        
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese una edad válida por favor")
            return

        try:
            peso = float(peso.replace(',', '.'))
            if peso <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese un peso válido por favor")
            return

        try:
            estatura = float(estatura.replace(',', '.'))
            if estatura <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese una estatura válida por favor")
            return

        imc = self.calcular_imc(peso, estatura)
        rutina = self.determinar_rutina(imc)
        self.mostrar_resultado(nombre, imc, rutina)



        # --------- VENTANA RESULTADO ------------ 

    def crear_pantalla_resultados(self):
        # Titulo principal
        tk.Label(self.frame_resultados, text="Resultados", bg='white', font=("Roboto", 20, "bold")).pack(pady=20)

        resultados_frame = tk.Frame(self.frame_resultados, bg='white', width=self.frame_width)
        resultados_frame.pack(pady=20, padx=20, fill='both', expand=True)

        # Titulos resultados
        self.resultado_nombre = tk.Label(resultados_frame, text="", font=("Roboto", 12), bg='white')
        self.resultado_nombre.pack(pady=5, anchor='w')
        self.resultado_imc = tk.Label(resultados_frame, text="", font=("Roboto", 12), bg='white')
        self.resultado_imc.pack(pady=5, anchor='w')
        self.resultado_rutina = tk.Label(resultados_frame, text="", font=("Roboto", 12), bg='white', wraplength=self.frame_width*0.8)
        self.resultado_rutina.pack(pady=5, anchor='w')

        # Boton ver rutina
        tk.Button(self.frame_resultados, text="Ver rutina", command=self.ver_rutina, font=("Roboto", 14, "bold"), fg='white', bg='#00FFB4').pack(pady=20)

    def mostrar_resultado(self, nombre_completo, imc, rutina):
        self.resultado_nombre.config(text=f"Nombre: {nombre_completo}")
        self.resultado_imc.config(text=f"IMC: {imc:.2f}")
        self.resultado_rutina.config(text=f"Tu objetivo es: {rutina}")

        self.mostrar_pantalla_resultados()


    # --------- VENTANA RUTINA ------------ 

    def ver_rutina(self):
        # Acá ira código para mostrar rutinas proximamente
        messagebox.showinfo("")





if __name__ == "__main__":
    app = PowerFitApp()
    app.mainloop()
