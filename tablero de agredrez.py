# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:32:47 2023

@author: pared
"""

import tkinter as tk

def create_chessboard(root):
    # Crear el grid
    for i in range(8):
        for j in range(8):
            # Determinar el color de la casilla
            if (i + j) % 2 == 0:
                color = 'white'
            else:
                color = 'black'
            
            # Crear el botón/casilla
            button = tk.Button(root, width=2, height=1, bg=color)
            button.grid(row=i, column=j)

# Crear la ventana principal
root = tk.Tk()
root.title("Tablero de Ajedrez")

# Crear el tablero de ajedrez
create_chessboard(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()