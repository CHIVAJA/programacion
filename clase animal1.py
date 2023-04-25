# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:22:18 2023

@author: lab
"""

class animal:
    def hablar(self):
        print("haciend ruido generico")
        
class gato(animal):
    def hablar(self):
        super().hablar()
        print("MIAU")

mi_perro=gato()
mi_perro.hablar()
mi_mascota01=gato()
mi_mascota01.hablar()