# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:20:33 2023

@author: lab
"""

def crealista(numero):
    lista=[]
    for item in range(1,numero+1,1):
        lista.append(item)
    return lista
print(crealista(10))