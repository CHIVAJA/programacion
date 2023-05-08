# -*- coding: utf-8 -*-
"""
Created on Mon May  8 10:29:41 2023

@author: lab
"""

import tkinter as tk

root=tk.Tk()
root.geometry("300x200")

label=tk.Label(root, text="Ingresa tu nombre:")
label.pack()

entry=tk.Entry(root, width=30)
entry.pack()

root.mainloop()