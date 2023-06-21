# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:16:38 2023

@author: lab
"""

import time
print("ATAQUE DE ORCOS")
escudo = int(input("ingrese el numero de escudos que desea: "))
soldado = int(input("ingrese el numero de soldados que desea: "))
dragon = int(input("ingrese el numero de dragones que desea: "))
granada = int(input("ingrese el numero de grandas que desea: "))
sanador = int(input("ingrese el numero de sanadores que desea: "))
hechicero = int(input("ingrese el numero de hechiceros que desea: "))
arco = int(input("ingrese el numero de arcos con sus respectivas flechas que desea: "))
oro = (escudo*1)+(soldado*5)+(granada*500)+(arco*300)
plata = (dragon*1000)+(sanador*1)+(hechicero*500)
print("el numero de monedas de oro que necesita es: ", oro)
print("el numero de monedas de plata que necesita es:", plata)

####################################
### Fecha y hora para el reporte ###
####################################

print(time.strftime("%H:%M:%S"))
print(time.strftime("%d/%m/%y"))
    
    
for i in range (5):
    print("hola, valor de i", i)