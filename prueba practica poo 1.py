# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:52:24 2023

@author: lab
"""

import tkinter as tk

root=tk.Tk()
root.geometry("300x200")
root.title("ventana")
marco=tk.Frame(root)
marco.pack()

boton2=tk.Button(marco, text="dispositivo 3")
boton2.pack()
boton3=tk.Button(marco, text="dispositivo 2")
boton3.pack()

def ventana():
    ventana_emergente=tk.Toplevel(root)
    etiqueta=tk.Label(ventana_emergente,text="esta encendido")
    etiqueta.pack()
boton1=tk.Button(marco,text="dispositivo 1", command=ventana)
boton1.pack()

boton1.pack()
boton1.pack(side=tk.LEFT)
boton2.pack(side=tk.RIGHT)
root.mainloop()