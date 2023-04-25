# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:27:16 2023

@author: lab
"""

class robot:
    def __init__(self, nombre, color):
        self.nombre=nombre
        self.color=color
    
    def saludar(self):
        print(f"hola, mi nombre es {self.nombre} y soy un robot {self.color}.")
        
class robotasistente(robot):
    def __init__(self, nombre, color, tareas):
        super().__init__(nombre, color)
        self.tareas=tareas
        
    def saludar(self):
        super().saludar()
        print("soy un robot asistente y estoy aqui para ayudarte. ")
        
    def realizar_tareas(self):
        super().saludar()
        print(f"realizando tareas: {self.tareas}")
        
robot1=robot("robot1", "rojo")
robot1.saludar()

robot2=robotasistente("robot2", "azul", ["limpiar", "cocinar", "organizar"])
robot2.saludar()
robot2.realizar_tareas()