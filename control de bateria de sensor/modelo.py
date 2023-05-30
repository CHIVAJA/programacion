# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:05:18 2023

@author: pared
"""

import tkinter as tk
from tkinter import messagebox

class Modelo:
    def __init__(self):
        self.sensores = {}

    def registrar_sensor(self, sensor_id, nivel_bateria):
        if sensor_id in self.sensores:
            messagebox.showerror("Error", f"El sensor con ID {sensor_id} ya está registrado.")
        elif nivel_bateria < 0:
            messagebox.showerror("Error", "El nivel de batería debe ser mayor o igual a cero.")
        else:
            self.sensores[sensor_id] = nivel_bateria
            messagebox.showinfo("Registro exitoso", f"Sensor con ID {sensor_id} registrado correctamente.")

    def actualizar_bateria(self, sensor_id, nuevo_nivel_bateria):
        if sensor_id not in self.sensores:
            messagebox.showerror("Error", f"No se encontró un sensor con ID {sensor_id}.")
        elif nuevo_nivel_bateria < 0:
            messagebox.showerror("Error", "El nivel de batería debe ser mayor o igual a cero.")
        else:
            self.sensores[sensor_id] = nuevo_nivel_bateria
            messagebox.showinfo("Actualización exitosa", f"Nivel de batería del sensor {sensor_id} actualizado correctamente.")

    def obtener_estado(self, sensor_id):
        if sensor_id in self.sensores:
            return self.sensores[sensor_id]
        else:
            return None


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.root = tk.Tk()
        self.root.title("Control de Baterías")

        self.sensor_id_entry = tk.Entry(self.root)
        self.sensor_id_entry.pack()

        self.nivel_bateria_entry = tk.Entry(self.root)
        self.nivel_bateria_entry.pack()

        self.registrar_button = tk.Button(self.root, text="Registrar Sensor", command=self.registrar_sensor)
        self.registrar_button.pack()

        self.actualizar_button = tk.Button(self.root, text="Actualizar Batería", command=self.actualizar_bateria)
        self.actualizar_button.pack()

        self.estado_button = tk.Button(self.root, text="Mostrar Estado", command=self.mostrar_estado)
        self.estado_button.pack()

    def registrar_sensor(self):
        sensor_id = self.sensor_id_entry.get()
        nivel_bateria = float(self.nivel_bateria_entry.get())
        self.controlador.registrar_sensor(sensor_id, nivel_bateria)

    def actualizar_bateria(self):
        sensor_id = self.sensor_id_entry.get()
        nuevo_nivel_bateria = float(self.nivel_bateria_entry.get())
        self.controlador.actualizar_bateria(sensor_id, nuevo_nivel_bateria)

    def mostrar_estado(self):
        sensor_id = self.sensor_id_entry.get()
        estado = self.controlador.obtener_estado(sensor_id)
        if estado is not None:
            messagebox.showinfo("Estado del Sensor", f"El nivel de batería del sensor {sensor_id} es {estado}.")
        else:
            messagebox.showerror("Error", f"No se encontró un sensor con ID {sensor_id}.")

    def iniciar_aplicacion(self):
        self.root.mainloop()


class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def registrar_sensor(self, sensor_id, nivel_bateria):
        self.modelo.registrar_sensor(sensor_id, nivel_bateria)

    def actualizar_bateria(self, sensor_id, nuevo_nivel_bateria):
        self.modelo.actualizar_bateria(sensor_id, nuevo_nivel_bateria)

    def obtener_estado(self, sensor_id):
        return self.modelo.obtener_estado(sensor_id)


if __name__ == '__main__':
    modelo = Modelo()
    vista = Vista(Controlador(modelo, None))
    vista.iniciar_aplicacion()