import tkinter as tk
from tkinter import PhotoImage, messagebox

class PowerFitApp(tk.Tk):

    # --------- VENTANAS CONFIGURACION GENERAL ------------

    def __init__(self):
        super().__init__()
        self.title("PowerFit - Tu App de ejercicios")

        # Imagen de fondo para la pantalla de inicio
        self.imagen_inicio = PhotoImage(file='power_fit.png')

        # Configuración de la ventana principal
        self.geometry(f"{self.imagen_inicio.width()}x{self.imagen_inicio.height()}")
        self.resizable(False, False)
        self.configure(bg='white')

        # Tamaño de los frames según img
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
        elif imc >= 25:
            return "Perder peso"

    # Rutinas de ejercicios para cada objetivo
    rutinas_ej = {
        "Ganar masa muscular": {
            "Día 1": "\n- Press militar c/man: 3x8\n- Remo c/man: 3x8\n- Curl bíceps c/man: 3x10\n- Extensiones tríceps en polea: 3x10",
            "\n"
            "Día 2": "\n- Sentadilla peso corporal: 3x10\n- Peso muerto c/man: 3x8\n- Zancadas: 3x8/pierna\n- Elevaciones talón: 3x15",
            "\n"
            "Día 3": "\n- Burpees: 3x10\n- Kettlebell Swings: 3x15\n- Flexiones: 3x10\n- Mountain Climbers: 3x20 seg",
            "\n"
            "Día 4": "\n- Crunches: 3x15\n- Plancha: 3x30 seg\n- Elevaciones de piernas: 3x10\n- Bicicleta abdominal: 3x15/lado",
            "\n"
            "Día 5 ": "- Circuito:\n- Flexiones: 3x12-15\n- Sentadillas: 3x12-15\n- Remo c/man: 3x12-15\n- Cardio: 20-30 min caminata/bicicleta"
        },

        "Mantenimiento": {
            "Día 1": "\n- Press militar c/man: 4x8-10\n- Remo con barra: 4x8-10\n- Curl bíceps c/barra: 4x10-12\n- Extensiones tríceps en polea: 4x10-12",
            "\n"
            "Día 2": "\n- Sentadilla c/barra: 4x8-10\n- Peso muerto rumano: 4x8-10\n- Prensa de pierna: 4x10-12\n- Elevaciones talón en máquina: 4x12-15",
            "\n"
            "Día 3": "\n- Burpees: 4x10-12\n- Kettlebell Swings: 4x15-20\n- Flexiones: 4x12-15\n- Mountain Climbers: 4x30 seg",
            "\n"
            "Día 4": "\n- Crunches: 4x20\n- Plancha: 4x45 seg\n- Elevaciones de piernas en banco: 4x15\n- Bicicleta abdominal: 4x20/lado",
            "\n"
            "Día 5 ": "- Circuito:\n- Burpees: 4x15-20\n- Sentadilla c/salto: 4x15-20\n- Kettlebell Swings: 4x15-20\n- Cardio: 30-40 min carrera/bicicleta"
        },

        "Perder peso": {
            "Día 1": "\n- Press militar c/barra: 4x10-12\n- Dominadas: 4x10-12\n- Curl bíceps c/barra Z: 4x12-14\n- Fondos en paralelas: 4x12-14",
            "\n"
            "Día 2": "\n- Sentadilla frontal c/barra: 5x5\n- Peso muerto sumo: 4x10-12\n- Prensa de pierna: 4x12-14\n- Elevaciones talón c/barra: 4x15-20",
            "\n"
            "Día 3": "\n- Burpees con salto: 5x12-15\n- Clean and Press c/barra: 4x8-10\n- Flexiones c/palmada: 4x15-20\n- Mountain Climbers avanzados: 4x45 seg",
            "\n"
            "Día 4": "\n- Crunches c/peso: 4x25\n- Plancha con elevación de pierna: 4x60 seg\n- Elevaciones de piernas colgado: 4x15-20\n- Bicicleta abdominal rápida: 4x25/lado",
            "\n"
            "Día 5 ": "- Circuito:\n- Burpees con salto: 5x20-25\n- Sentadillas con salto: 5x20-25\n- Kettlebell Swings: 5x20-25\n- Cardio: 40-50 min carrera/bicicleta"
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

        # Área para mostrar la rutina
        self.rutina_frame = tk.Frame(self.frame_resultados, bg='white')
        self.rutina_frame.pack(pady=20, padx=20, fill='both', expand=True)

        # Boton ver rutina
        tk.Button(self.frame_resultados, text="Ver rutina", command=self.mostrar_rutina, font=("Roboto", 14, "bold"), fg='white', bg='#00FFB4').pack(pady=20)

    def mostrar_resultado(self, nombre_completo, imc, rutina):
        self.resultado_nombre.config(text=f"Nombre: {nombre_completo}")
        self.resultado_imc.config(text=f"IMC: {imc:.2f}")
        self.resultado_rutina.config(text=f"Tu objetivo es: {rutina}")

        self.mostrar_pantalla_resultados()

    # --------- MUESTRA RUTINA Y TEMPORIZADOR ------------
    def mostrar_rutina(self):
        rutina = self.resultado_rutina.cget("text").split(": ")[1]  # objetivo de la rutina
        if rutina in self.rutinas_ej:
            rutina_texto = "\n".join([f"{dia}: {ejercicios}" for dia, ejercicios in self.rutinas_ej[rutina].items()])
            
            # Crear una nueva ventana con el mismo tamaño que la ventana principal
            ventana_rutina = tk.Toplevel(self)
            ventana_rutina.title("Tu Rutina de Ejercicios")
            ventana_rutina.geometry(f"{self.frame_width}x{self.frame_height}")
            ventana_rutina.configure(bg='white')

            # Crear un frame para el widget Text y la barra de desplazamiento
            frame_texto = tk.Frame(ventana_rutina, bg='white')
            frame_texto.pack(pady=20, padx=20, fill='both', expand=True)
     
            texto_rutina = tk.Text(frame_texto, wrap=tk.WORD, font=("Roboto", 10), bg='white', width=80, height=20)
            texto_rutina.pack(side=tk.LEFT, fill='both', expand=True)

            # barra de desplazamiento 
            scrollbar = tk.Scrollbar(frame_texto, orient=tk.VERTICAL, command=texto_rutina.yview)
            scrollbar.pack(side=tk.RIGHT, fill='y')

            texto_rutina.config(yscrollcommand=scrollbar.set)
            
            # Insertar la rutina y resaltar Día 1
            for dia, ejercicios in self.rutinas_ej[rutina].items():
                if dia == "Día 1":
                    texto_rutina.insert(tk.END, f"{dia}{ejercicios}\n", ("resaltado"))
                else:
                    texto_rutina.insert(tk.END, f"{dia}{ejercicios}\n")
            
            texto_rutina.tag_config("resaltado", background="#00FFB4")

            # Agregar el temporizador a la ventana de rutina
            self.temporizador = tk.Label(ventana_rutina, font=('Roboto', 22), bg='white', fg='black')
            self.temporizador.pack(pady=20)

            frame_botones = tk.Frame(ventana_rutina, bg='white')
            frame_botones.pack(pady=20)

            # Botones del temporizador
            tk.Button(frame_botones, text="Iniciar", command=lambda: self.iniciar_temporizador(ventana_rutina), font=("Roboto", 11), fg='white', bg='#00FFB4').pack(side=tk.LEFT, padx=10)
            tk.Button(frame_botones, text="Parar", command=self.parar_temporizador, font=("Roboto", 11), fg='white', bg='#FF0000').pack(side=tk.LEFT, padx=10)
            tk.Button(frame_botones, text="Reiniciar", command=lambda: self.reiniciar_temporizador(ventana_rutina), font=("Roboto", 11), fg='white', bg='#00FFB4').pack(side=tk.LEFT, padx=10)

            # Configurar y comenzar el temporizador
            self.tiempo_restante = 60
            self.temporizador_activado = False
            self.temporizador_id = None
            
            self.iniciar_temporizador(ventana_rutina)

            tk.Button(ventana_rutina, text="Cerrar", command=ventana_rutina.destroy, font=("Roboto", 14, "bold"), fg='white', bg='#00FFB4').pack(pady=20)

        else:
            messagebox.showerror("Error", "Rutina no disponible")

    #funcionamiento del temporizador
    def iniciar_temporizador(self, ventana_rutina):
        def actualizar_tiempo():
            if self.tiempo_restante > 0 and self.temporizador_activado:
                minutos, segundos = divmod(self.tiempo_restante, 60)
                tiempo_formateado = f'{minutos:02}:{segundos:02}'
                self.temporizador.config(text=tiempo_formateado)
                self.tiempo_restante -= 1
                self.temporizador_id = ventana_rutina.after(1000, actualizar_tiempo)
            else:
                if self.tiempo_restante == 0:
                    self.temporizador.config(text='Finalizado!', font=("Roboto", 22, "bold"))
                self.temporizador_activado = False
        
        if not self.temporizador_activado:
            self.temporizador_activado = True
            actualizar_tiempo()

    def parar_temporizador(self):
        if self.temporizador_id:
            self.after_cancel(self.temporizador_id)
            self.temporizador_activado = False

    def reiniciar_temporizador(self, ventana_rutina):
        self.parar_temporizador()
        self.tiempo_restante = 60
        minutos, segundos = divmod(self.tiempo_restante, 60)
        self.temporizador.config(text=f'{minutos:02}:{segundos:02}')
        self.temporizador_activado = False


if __name__ == "__main__":
    app = PowerFitApp()
    app.mainloop()
