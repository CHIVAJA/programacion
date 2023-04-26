# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:15:35 2023

@author: lab
"""

class redessociales:
    def __init__(self, nombre_platf, usuario, amigos, correo):
        self.nombre_platf=nombre_platf
        self.usuario=usuario
        self.amigos=amigos
        self.correo=correo
    def inicioS(self):
        print(self.usuario, ",bienvenido, ha iniciado secion")
    def cerrar(self):
        print("has cerrado secion, adios: ", self.usuario)
    def amigo(self):
        print("el numero de amigos que tienes: ", self.amigos)
        
u1=redessociales("facebook", "xd012", "23", "xdxd@")
u1.inicioS()
u1.cerrar()