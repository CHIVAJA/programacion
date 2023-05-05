# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:02:38 2023

@author: lab
"""
import tkinter as tk
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.title("ventana")
marco=tk.Frame(ventana)
marco.pack()
boton=tk.Button(marco,text="haz clic aqui")
boton1=tk.Button(marco,text="Boton 1")
ventana.configure(bg="black")

def clic():
    print("haz hecho clic en el boton")
boton=tk.Button(ventana,text="haz clic aqui",
command=clic)
boton1=tk.Button(ventana,text="Boton 1",
command=clic)

cuadro_text=tk.Entry(ventana)
cuadro_text.pack()

text_ingresado=cuadro_text.get()
etiqueta=tk.Label(ventana,text="!hola, mundo!")
etiqueta.pack()

elementos=["elemento 1", "elemento 2", "elemento 3"]
lista=tk.Listbox(ventana)
for elementos in elementos:
    lista.insert(tk.END, elementos)
lista.pack()

def abrir_ventana():
    ventana_emergente=tk.Toplevel(ventana)
    etiqueta=tk.Label(ventana_emergente,text="!es una ventana emergente!")
    etiqueta.pack()
boton=tk.Button(ventana,text="abrir ventana emergente", command=abrir_ventana)
boton.pack()

boton.pack()
boton.pack(side=tk.LEFT)
boton1.pack(side=tk.RIGHT)
ventana.mainloop()