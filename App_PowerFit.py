import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox

class PowerFitApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("PowerFit - Tu App de ejercicios")

        # Imágenes de fondo
        self.imagen_inicio = PhotoImage(file='assets\power_fit.png')
        self.imagen_rutinas = PhotoImage(file='assets\power_fit_2.png')
        

        # Configuración de la ventana principal
        self.geometry(f"{self.imagen_inicio.width()}x{self.imagen_inicio.height()}")
        self.resizable(False, False)
        self.configure(bg='white')

        # Tamaño de los frames según la imagen
        self.frame_width = self.imagen_inicio.width()
        self.frame_height = self.imagen_inicio.height()

        # Frames para la pantalla de inicio, inputs y resultados
        self.frame_inicio = tk.Frame(self, bg='white', width=self.frame_width, height=self.frame_height)
        self.frame_inputs = tk.Frame(self, bg='white', width=self.frame_width, height=self.frame_height)
        self.frame_resultados = tk.Frame(self, bg='white', width=self.frame_width, height=self.frame_height)
        self.frame_rutinas = tk.Frame(self, bg='white', width=self.frame_width, height=self.frame_height)

        # Crear las pantallas
        self.crear_pantalla_inicio()
        self.crear_pantalla_inputs()
        self.crear_pantalla_resultados()
        self.crear_pantalla_rutinas()

        self.mostrar_pantalla_inicio()

    # --------- VENTANA DE INICIO ------------

    def crear_pantalla_inicio(self):
        tk.Label(self.frame_inicio, image=self.imagen_inicio).place(relx=0.5, rely=0.5, anchor='center')
        tk.Button(self.frame_inicio, text="Comenzar", command=self.mostrar_pantalla_inputs, font=("Roboto", 14, "bold"), fg='black', bg='#1ad69e', cursor='hand2', relief=tk.FLAT).place(relx=0.5, rely=0.8, anchor='center')

    # --------- VENTANA INPUTS ------------

    def crear_pantalla_inputs(self):
        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        # Título principal
        tk.Label(self.frame_inputs, text="Ready?", bg='white', font=("Roboto", 20, "bold")).place(relx=0.1, rely=0.05, anchor='w')
        tk.Label(self.frame_inputs, text="Empecemos", bg='white', font=("Roboto", 20, "bold")).place(relx=0.1, rely=0.12, anchor='w')

        # Inputs
        self.crear_campo_entrada("Nombre completo", 0.25, "nombre")
        self.crear_campo_entrada("Edad (años)", 0.35, "edad")
        self.crear_campo_entrada("Peso (kg)", 0.45, "peso")
        self.crear_campo_entrada("Estatura (m)", 0.55, "estatura")

        # Botón volver
        tk.Button(self.frame_inputs, text="Volver", command=self.mostrar_pantalla_inicio, font=("Roboto", 14, "bold"), fg='black', bg='#1ad69e', cursor='hand2', relief=tk.FLAT).place(relx=0.3, rely=0.85, anchor='center', relwidth=0.3)

        # Botón enviar
        tk.Button(self.frame_inputs, text="Enviar", command=self.enviar_datos, font=("Roboto", 14, "bold"), fg='black', bg='#1ad69e', cursor='hand2', relief=tk.FLAT).place(relx=0.7, rely=0.85, anchor='center', relwidth=0.3)

    def crear_campo_entrada(self, texto, posicion_y, atributo):
        tk.Label(self.frame_inputs, text=texto, bg='white', font=("Roboto", 12)).place(relx=0.5, rely=posicion_y, anchor='center')
        setattr(self, f"entry_{atributo}", tk.Entry(self.frame_inputs, font=("Roboto", 12), fg='black', bg='white'))
        getattr(self, f"entry_{atributo}").place(relx=0.5, rely=posicion_y + 0.05, anchor='center', relwidth=0.6)

    def mostrar_pantalla_inicio(self):
        self.frame_inputs.pack_forget()
        self.frame_resultados.pack_forget()
        self.frame_rutinas.pack_forget()
        self.frame_inicio.pack(expand=True, fill='both')

    def mostrar_pantalla_inputs(self):
        self.frame_inicio.pack_forget()
        self.frame_resultados.pack_forget()
        self.frame_rutinas.pack_forget()
        self.frame_inputs.pack(expand=True, fill='both')

    def mostrar_pantalla_resultados(self):
        self.frame_inicio.pack_forget()
        self.frame_inputs.pack_forget()
        self.frame_rutinas.pack_forget()
        self.frame_resultados.pack(expand=True, fill='both')

    def mostrar_pantalla_rutinas(self):
        self.frame_inicio.pack_forget()
        self.frame_inputs.pack_forget()
        self.frame_resultados.pack_forget()
        self.frame_rutinas.pack(expand=True, fill='both')

    # --------- Calculo de IMC con inputs ------------

    def calcular_imc(self, peso, estatura):
        return peso / (estatura ** 2)

    # --------- Asignación de rutinas ------------

    def determinar_rutina(self, imc):
        if imc < 18.5:
            return "Ganar masa muscular"
        elif 18.5 <= imc < 25:
            return "Mantenimiento"
        elif imc >= 25:
            return "Perder peso"

    # Rutinas de ejercicios para cada objetivo
    rutinas_ej = {
        "Ganar masa muscular": {
            "Día 1": "\n- Press militar c/man: 3x8\n- Remo c/man: 3x8\n- Curl bíceps c/man: 3x10\n- Extensiones tríceps en polea: 3x10",
            "Día 2": "\n- Sentadilla peso corporal: 3x10\n- Peso muerto c/man: 3x8\n- Zancadas: 3x8/pierna\n- Elevaciones talón: 3x15",
            "Día 3": "\n- Burpees: 3x10\n- Kettlebell Swings: 3x15\n- Flexiones: 3x10\n- Mountain Climbers: 3x20 seg",
            "Día 4": "\n- Crunches: 3x15\n- Plancha: 3x30 seg\n- Elevaciones de piernas: 3x10\n- Bicicleta abdominal: 3x15/lado",
            "Día 5": "\nCircuito:\n- Flexiones: 3x12-15\n- Sentadillas: 3x12-15\n- Remo c/man: 3x12-15\n- Cardio: 20-30 min caminata/bicicleta"
        },
        "Mantenimiento": {
            "Día 1": "\n- Press militar c/man: 4x8-10\n- Remo con barra: 4x8-10\n- Curl bíceps c/barra: 4x10-12\n- Extensiones tríceps en polea: 4x10-12",
            "Día 2": "\n- Sentadilla con barra: 4x8-10\n- Peso muerto con barra: 4x8-10\n- Zancadas con mancuernas: 4x10/pierna\n- Elevaciones talón: 4x15",
            "Día 3": "\n- Burpees: 4x20\n- Kettlebell Swings: 4x20\n- Flexiones: 4x15\n- Mountain Climbers: 4x45 seg",
            "Día 4": "\n- Crunches en fitball: 4x20-25\n- Plancha: 4x45 seg\n- Elevaciones de piernas en barra: 4x15\n- Bicicleta abdominal: 4x25/lado",
            "Día 5": "\nCircuito HIIT:\n- Burpees: 5x20\n- Sentadilla con salto: 5x20\n- Kettlebell Swings: 5x20\n- Cardio: 30 min intermitente"
        },
        "Perder peso": {
            "Día 1": "\n- Sentadillas con mancuernas: 3x15\n- Flexiones: 3x12\n- Remo con mancuernas: 3x15\n- Crunches: 3x20",
            "Día 2": "\n- Zancadas: 3x15/pierna\n- Elevaciones talón: 3x20\n- Plancha: 3x45 seg\n- Crunches invertidos: 3x15",
            "Día 3": "\n- Burpees: 4x15\n- Kettlebell Swings: 4x20\n- Mountain Climbers: 4x30 seg\n- Bicicleta abdominal: 4x15/lado",
            "Día 4": "\n- Sentadilla con salto: 3x15\n- Flexiones: 3x10\n- Remo con mancuernas: 3x15\n- Plancha: 3x1 min",
            "Día 5": "\nCircuito:\n- Burpees: 5x10\n- Flexiones: 5x12\n- Sentadilla con salto: 5x15\n- Cardio: 40 min intermitente"
        }
    }
    
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
            estatura = estatura.replace(',', '.')
            estatura_float = float(estatura)

    #Si la estatura tiene 3 dígitos y no contiene punto decimal, se asume que está en centímetros
            if 100 <= estatura_float < 1000:
              estatura_float /= 100  

            if estatura_float <= 0:
               raise ValueError

            estatura = estatura_float
        except ValueError:
          messagebox.showerror("Error", "Ingrese una estatura válida por favor")
          return

        imc = self.calcular_imc(peso, estatura)
        rutina = self.determinar_rutina(imc)
        self.mostrar_resultado(nombre, imc, rutina)
        
        

    # --------- VENTANA RESULTADO IMC ------------

    def crear_pantalla_resultados(self):
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        self.label_resultados_titulo = tk.Label(self.frame_resultados, text="Resultado", bg='white', font=("Roboto", 12))
        self.label_resultados_titulo.pack(pady=10, padx=20, fill='both', expand=True)
        
    def mostrar_resultado(self, nombre, imc, rutina_asignada):
        self.label_resultados_titulo.config(
            text=f"Hola {nombre}\nTu IMC es: {imc:.2f}\nTu objetivo es: {rutina_asignada}")
        self.combobox_rutinas['values'] = list(self.rutinas_ej[rutina_asignada].keys())
        self.combobox_rutinas.current(0)  
        self.mostrar_rutina()  
        self.mostrar_pantalla_resultados()

        # Botón para cerrar la ventana de resultados
        tk.Button(self.frame_resultados, text="Volver", command=self.mostrar_pantalla_inputs, font=("Roboto", 14, "bold"), fg='black', bg='#1ad69e', cursor='hand2', relief=tk.FLAT).place(relx=0.3, rely=0.85, anchor='center', relwidth=0.3)

        # Botón para ver la rutina
        tk.Button(self.frame_resultados, text="Ver rutina", command=self.mostrar_pantalla_rutinas, font=("Roboto", 14, "bold"), fg='black', bg='#1ad69e', cursor='hand2', relief=tk.FLAT).place(relx=0.7, rely=0.85, anchor='center', relwidth=0.3)



    # --------- VENTANA RUTINAS ------------

    def crear_pantalla_rutinas(self):
        for widget in self.frame_rutinas.winfo_children():
            widget.destroy()

        # Imagen de fondo en la ventana de rutinas
        self.background_image = tk.Label(self.frame_rutinas, image=self.imagen_rutinas)
        self.background_image.place(relx=0.5, rely=0.5, anchor='center')

        # Desplegable de rutinas
        self.rutina_opcion = tk.StringVar(self.frame_rutinas)
        self.combobox_rutinas = ttk.Combobox(self.frame_rutinas, textvariable=self.rutina_opcion, state="readonly", font=("Roboto", 11))
        self.combobox_rutinas.place(relx=0.5, rely=0.16, anchor='center', relwidth=0.6)
        self.combobox_rutinas.bind("<<ComboboxSelected>>", self.mostrar_rutina)

        # Texto de la rutina
        self.texto_rutina = tk.Label(self.frame_rutinas, font=("Roboto", 11), bg='white', fg='black', wraplength=300, justify='left')
        self.texto_rutina.place(relx=0.5, rely=0.48, anchor='center', relwidth=0.8)
        
        # Botón para volver
        tk.Button(self.frame_rutinas, text="Volver", command=self.mostrar_pantalla_resultados, font=("Roboto", 14, "bold"), fg='black', bg='#1ad69e', cursor='hand2', relief=tk.FLAT).place(relx=0.3, rely=0.85, anchor='center', relwidth=0.3)

        # Botón para cerrar
        tk.Button(self.frame_rutinas, text="Cerrar", command=self.cerrar_aplicacion, font=("Roboto", 14, "bold"), fg='black', bg='#1ad69e', cursor='hand2', relief=tk.FLAT).place(relx=0.7, rely=0.85, anchor='center', relwidth=0.3)

    def mostrar_rutina(self, *args):
        rutina_dia = self.rutina_opcion.get()
        if rutina_dia:
            rutina = self.rutinas_ej[self.determinar_rutina(self.calcular_imc(float(self.entry_peso.get().replace(',', '.')), float(self.entry_estatura.get().replace(',', '.'))))][rutina_dia]
            self.texto_rutina.config(text=rutina)
    
    # Botón Cerrar App completa
    def cerrar_aplicacion(self):
        self.quit()         


if __name__ == "__main__":
    app = PowerFitApp()
    app.mainloop()