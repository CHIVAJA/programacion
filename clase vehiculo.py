# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:22:47 2023

@author: lab
"""

class vehiculo:
    def __init__(self, velocidad, posicion, direccion):
        self.velocidad=velocidad
        self.posicion=posicion
        self.direccion=direccion
        
class coche(vehiculo):
    def __init__(self, marca, velocidad, direccion, posicion):
        super().__init__(velocidad, posicion, direccion)
        self.marca=marca
    def saludar(self):
        print("el auto",self.marca, "va auna velocidad de",self.velocidad)
    
    def conducir(self):
        print("el auto esta siendo conducido")
    def acelerar(self):
        print("el auto esta acelerando a: ",self.velocidad)

class moto(vehiculo):
    def __init__(self, marca, velocidad, direccion, posicion):
        super(). 
        
coche1=coche("toyota", "80 km/h", "4", "derecha", "adelante")
coche1.saludar()
coche1.conducir()
coche1.acelerar()