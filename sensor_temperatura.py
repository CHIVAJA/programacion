# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:13:23 2023

@author: pared
"""

class LecturaSensorError(Exception):
    pass

class SensorTemperatura:
    def leer_temperatura(self):
        temp=int(input("ingrese la temperatura: "))
        try:
            temp=int(temp)
        except:
            raise LecturaSensorError("la temperatura no es valida")
        return temp
    def verificar_rango(self, temp):  
        if temp<-50 or temp>100:
            raise LecturaSensorError("la temperatura es invalida")
sensor=SensorTemperatura()
while True:
    try:
        temp=sensor.leer_temperatura()
        sensor.verificar_rango(temp)
        print("temperatura valida", temp)
    except LecturaSensorError as e:
        print("error: ", e)
    opcion=input("¿desea leer nuevamente la temperatura? (s/n): ")
    if opcion!='s':
        break