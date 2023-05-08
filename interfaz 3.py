# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:50:43 2023

@author: lab
"""

import tkinter as tk

root=tk.Tk()
root.geometry("300x200")

label=tk.Label(root, text="selecciona tu opcion:")
label.pack()

opciones=["opcion 1","opcion 2","opcion 3",]

combo = tk.Combobox(root, values=opciones)
combo.pack()

def seleccionado(event):
    label.config(text=f"seleccionaste {combo.get()}")
    
combo.bind