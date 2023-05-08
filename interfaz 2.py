# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:35:12 2023

@author: lab
"""

import tkinter as tk

root=tk.Tk()
root.geometry("300x200")

label=tk.Label(root, text="selecciona tu opcion:")
label.pack()

var1=tk.BooleanVar()
var1.set(False)

var2=tk.BooleanVar()
var2.set(False)

def seleccionado():
    opciones=[]
    if var1.get():
        opciones.append("opcion 1")
    if var1.get():
        opciones.append("opcion 2")
    label.config(text=f"seleccionaste {', '.join(opciones)}")
    
cb1=tk.Checkbutton(root, text="opcion 1", variable=var1, onvalue=True, offvalue=False,command=seleccionado())
cb1.pack()

cb2=tk.Checkbutton(root, text="opcion 2", variable=var2, onvalue=True, offvalue=False,command=seleccionado())
cb2.pack()

root.mainloop()