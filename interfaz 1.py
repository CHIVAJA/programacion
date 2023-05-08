# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:22:41 2023

@author: lab
"""

import tkinter as tk

root=tk.Tk()
root.geometry("300x200")

label=tk.Label(root, text="selecciona tu opcion:")
label.pack()

var=tk.StringVar()
var.set("opcion 1")

def seleccionado():
    label.config(text=f"selecionaste {var.get()}")
    
rb1=tk.Radiobutton(root, text="opcion 1", variable=var, value="opcion 1", command=seleccionado)
rb1.pack()

rb2=tk.Radiobutton(root, text="opcion 2", variable=var, value="opcion 2", command=seleccionado)
rb2.pack()

root.mainloop()