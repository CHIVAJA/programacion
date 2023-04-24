# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:25:31 2023

@author: lab
"""

class animal:
    def __init__(self,nombre,raza,edad,estatura,color):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.estatura=estatura
        self.color=color
    def nombre(self):
        print("el nombre del animal es: ",self.name)
    def raza(self):
        print("la raza del animal es: ",self.raza)
    def edad(self):
        print("la edad del animal es: ",self.edad)
    def estatura(self):
        print("la estatura del animal es: ",self.estatura)
    def color(self):
        print("el color del animal es: ",self.color)
animal1=animal("xd", "pitbull", "4 años", "70 cm", "negro")
animal1.