# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 05:35:58 2023

@author: Usuario
"""

import tkinter as tk
import random

class SensorError(Exception):
    def __init__(self, sensor_id, error_type):
        self.sensor_id = sensor_id
        self.error_type = error_type
        super().__init__()

class Sensor:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
    
    def leer_dato(self):
        # Simulación de lectura de dato del sensor
        # En este caso, generamos un número aleatorio entre 0 y 1
        dato = random.random()
        
        # Simulación de error en algunos casos
        if dato < 0.5:
            raise SensorError(self.id, "Error de lectura")

        return dato

class App(tk.Tk):
    def __init__(self, sensores):
        super().__init__()
        self.sensores = sensores
        self.title("Control de Sensores")
        self.config(bg="SteelBlue1")
        self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="PRESIONA EL BOTON PARA LEER LOS DATOS DE LOS SENSORES:",font=("Arial", 12), bg="SteelBlue1")
        self.label.pack(pady=10)

        self.button = tk.Button(self, text="LEER DATOS", bg="DarkOliveGreen1" ,command=self.leer_datos_sensores)
        self.button.pack(pady=10)

        self.output = tk.Text(self, height=8, width=40)
        self.output.pack()

    def leer_datos_sensores(self):
        self.output.delete("1.0", tk.END)
        
        for sensor in self.sensores:
            try:
                dato = sensor.leer_dato()
                mensaje = f"Dato leído del sensor {sensor.id} ({sensor.tipo}): {dato}"
                self.output.insert(tk.END, mensaje + "\n")
            except SensorError as e:
                mensaje_error = f"Error al leer el sensor {e.sensor_id} ({e.error_type})"
                self.output.insert(tk.END, mensaje_error + "\n")
            except Exception as e:
                mensaje_error = f"Error inesperado al leer el sensor {sensor.id}: {str(e)}"
                self.output.insert(tk.END, mensaje_error + "\n")
            else:
                self.output.insert(tk.END, "\n")

sensor1 = Sensor(1, "Temperatura")
sensor2 = Sensor(2, "Humedad")
sensor3 = Sensor(3, "Presión")

app = App([sensor1, sensor2, sensor3])
app.mainloop()