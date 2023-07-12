#Controlador *******************************************************************************************************************************
class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def verificar_dispositivo_controller(self, codigo):
        return self.modelo.verificar_dispositivo(codigo)

    def registrar_dispositivo_controller(self, codigo):
        return self.modelo.registrar_dispositivo(codigo)


#Vista *************************************************************************************************************************************
import tkinter as tk
from tkinter import messagebox
from tkinter import font

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tk.Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Verificación de Dispositivos")
        self.ventana.configure(bg="SteelBlue1")

        titulo_font = font.Font(family="Arial", size=16, weight="bold")
        titulo = tk.Label(self.ventana, text="CONTROLADOR DE SENSORES", font=titulo_font, bg="SteelBlue1")
        titulo.pack()

        titulo_font = font.Font(family="Arial", size=11, weight="bold")
        titulo = tk.Label(self.ventana, text="________________________", font=titulo_font, bg="SteelBlue1")
        titulo.pack()

        self.label_codigo = tk.Label(self.ventana, text="Código del dispositivo:", font=("Arial", 12), bg="SteelBlue1")
        self.label_codigo.pack()

        self.entry_codigo = tk.Entry(self.ventana, font=("Arial", 12))
        self.entry_codigo.pack()

        self.btn_registrar = tk.Button(self.ventana, text="Registrar", font=("Arial", 12), bg="DarkOliveGreen1", command=self.registrar_dispositivo_handler)
        self.btn_registrar.pack(pady=10)

        self.btn_verificar = tk.Button(self.ventana, text="Verificar", font=("Arial", 12), bg="DarkOliveGreen1", command=self.verificar_dispositivo_handler)
        self.btn_verificar.pack(pady=10)

    def registrar_dispositivo_handler(self):
        codigo = self.entry_codigo.get()
        try:
            self.controlador.registrar_dispositivo_controller(codigo)
            messagebox.showinfo("Registro Exitoso", "El dispositivo se ha registrado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def verificar_dispositivo_handler(self):
        codigo = self.entry_codigo.get()
        try:
            mensaje = self.controlador.verificar_dispositivo_controller(codigo)
            messagebox.showinfo("Resultado de la verificación", mensaje)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def iniciar(self):
        self.ventana.mainloop()


#Modelo *************************************************************************************************************************************
class Modelo:
    def __init__(self):
        self.dispositivos_registrados = []

    def verificar_dispositivo(self, codigo):
        if codigo in self.dispositivos_registrados:
            if codigo.startswith("ACT"):
                return "¡Alerta! El dispositivo no está conectado"
            else:
                return "Verificación exitosa. Funcionamiento normal"
        else:
            raise Exception("Error: código de dispositivo inválido")

    def registrar_dispositivo(self, codigo):
        if codigo not in self.dispositivos_registrados:
            self.dispositivos_registrados.append(codigo)
        else:
            raise Exception("Error: el dispositivo ya está registrado")


#Main **************************************************************************************************************************************
modelo = Modelo()
controlador = Controlador(modelo, None)  # La vista se asignará en el main

vista = Vista(controlador)
controlador.vista = vista  # Asignar la vista al controlador

vista.iniciar()
