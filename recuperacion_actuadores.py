# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 05:25:18 2023

@author: Usuario
"""

import tkinter as tk
from tkinter import font

class ActuadorError(Exception):
    def __init__(self, actuador_id, error_type):
        self.actuador_id = actuador_id
        self.error_type = error_type

class Actuador:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def encender(self):
        # Simulación de encendido del actuador
        if self.id == 2 or self.id == 8:
            raise ActuadorError(self.id, "Error de encendido")
        else:
            print(f"Se ha encendido el actuador {self.id} ({self.tipo}).")

class Application(tk.Tk):
    def __init__(self, actuadores):
        super().__init__()
        self.actuadores = actuadores
        self.title("Control de Actuadores")
        self.geometry("300x200")
        self.config(bg="SteelBlue1")

        self.status_label = tk.Label(self, text="ESTADO DE LOS ACTUADORES:",bg="SteelBlue1")
        self.status_label.pack()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.buttons = []
        for actuador in self.actuadores:
            button = tk.Button(self.button_frame, text=f"Encender Actuador {actuador.id}",bg="DarkOliveGreen1",command=lambda a=actuador: self.encender_actuador(a))
            button.pack()
            self.buttons.append(button)

    def encender_actuador(self, actuador):
        try:
            actuador.encender()
            self.status_label["text"] += f"\nSe ha encendido el actuador {actuador.id} ({actuador.tipo})."
        except ActuadorError as e:
            self.status_label["text"] += f"\nError al encender el actuador {e.actuador_id} ({e.error_type})."

actuador1 = Actuador(1, "Luz")
actuador2 = Actuador(2, "Persiana")
actuador3 = Actuador(3, "Electrodoméstico")
actuador4 = Actuador(8, "Error de Encendido")

app = Application([actuador1, actuador2, actuador3, actuador4])
app.mainloop()