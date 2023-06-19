# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:41:55 2023

@author: lab
"""

class EntradaInvalida(Exception):
    pass


def validar_edad(edad):
    if edad < 0 or edad > 120:
        raise EntradaInvalida("la edad porporsionada es invalida")
        
        
try:
    edad=int(input("ingrese su edad: "))
    validar_edad(edad)
    print("la edad es valida")
except EntradaInvalida as e:
    print("error:",e)