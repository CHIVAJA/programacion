# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:27:20 2023

@author: lab
"""

class LecturaSensorError(Exception):
    pass

class SensorTemperatura:
    def leer_temperatura(temp):
        int(input("ingrese la temperatura: "))
    def verificar_rango(temp):
        if temp<-50 or temp>100:
            raise LecturaSensorError("la temperatura es invalida")
        return temp