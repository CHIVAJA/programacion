# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:33:37 2023

@author: pared
"""

import tkinter as tk

# Funciones para controlar los dispositivos
def encender_dispositivo(dispositivo):
    # Lógica para encender el dispositivo
    estado = "Encendido"
    actualizar_estado(dispositivo, estado)

def apagar_dispositivo(dispositivo):
    # Lógica para apagar el dispositivo
    estado = "Apagado"
    actualizar_estado(dispositivo, estado)

def mostrar_estado(dispositivo):
    # Lógica para obtener el estado actual del dispositivo
    # y mostrarlo en la etiqueta correspondiente
    estado = obtener_estado(dispositivo)
    actualizar_estado(dispositivo, estado)

def obtener_estado(dispositivo):
    # Lógica para obtener el estado actual del dispositivo
    # Esta función debe ser implementada según los dispositivos reales
    # y cómo se comunican con la aplicación
    # Aquí se retorna un estado aleatorio para demostración
    import random
    estados = ["Encendido", "Apagado"]
    return random.choice(estados)

def actualizar_estado(dispositivo, estado):
    # Actualizar la etiqueta correspondiente al dispositivo
    if dispositivo == "luz":
        estado_label_luz.config(text=estado)
    elif dispositivo == "cerradura":
        estado_label_cerradura.config(text=estado)
    elif dispositivo == "termostato":
        estado_label_termostato.config(text=estado)

# Crear la ventana principal
root = tk.Tk()
root.title("Control de Dispositivos IoT")

# Crear los botones y etiquetas para controlar la luz
luz_label = tk.Label(root, text="Luz:")
luz_label.grid(row=0, column=0, sticky=tk.W)

encender_button_luz = tk.Button(root, text="Encender", command=lambda: encender_dispositivo("luz"))
encender_button_luz.grid(row=0, column=1)

apagar_button_luz = tk.Button(root, text="Apagar", command=lambda: apagar_dispositivo("luz"))
apagar_button_luz.grid(row=0, column=2)

estado_label_luz = tk.Label(root, text="")
estado_label_luz.grid(row=0, column=3)

estado_button_luz = tk.Button(root, text="Mostrar Estado", command=lambda: mostrar_estado("luz"))
estado_button_luz.grid(row=0, column=4)

# Crear los botones y etiquetas para controlar la cerradura
cerradura_label = tk.Label(root, text="Cerradura:")
cerradura_label.grid(row=1, column=0, sticky=tk.W)

encender_button_cerradura = tk.Button(root, text="Encender", command=lambda: encender_dispositivo("cerradura"))
encender_button_cerradura.grid(row=1, column=1)

apagar_button_cerradura = tk.Button(root, text="Apagar", command=lambda: apagar_dispositivo("cerradura"))
apagar_button_cerradura.grid(row=1, column=2)

estado_label_cerradura = tk.Label(root, text="")
estado_label_cerradura.grid(row=1, column=3)

estado_button_cerradura = tk.Button(root, text="Mostrar Estado", command=lambda: mostrar_estado("cerradura"))
estado_button_cerradura.grid(row=1, column=4)

# Crear los botones y etiquetas para controlar el termostato
termostato_label = tk.Label(root, text="Termostato:")
termostato_label.grid(row=2, column=0, sticky=tk.W)

encender_button_termostato = tk.Button(root, text="Encender", command=lambda: encender_dispositivo("termostato"))
encender_button_termostato.grid(row=2, column=1)

apagar_button_termostato = tk.Button(root, text="Apagar", command=lambda: apagar_dispositivo("termostato"))
apagar_button_termostato.grid(row=2, column=2)

estado_label_termostato = tk.Label(root, text="")
estado_label_termostato.grid(row=2, column=3)

estado_button_termostato = tk.Button(root, text="Mostrar Estado", command=lambda: mostrar_estado("termostato"))
estado_button_termostato.grid(row=2, column=4)

# Iniciar el bucle principal de la aplicación
root.mainloop()