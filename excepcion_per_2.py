# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:17:56 2023

@author: lab
"""

class DivisionPorCeroError(Exception):
    pass

class Calculadora:
    def dividir(self, num1, num2):
        if num2==0:
            raise DivisionPorCeroError("Division por cero no permitida")
        return num1/num2
    
try:
    calc=Calculadora()
    resultado=calc.dividir(10, 0)
    print("El resultado es:", resultado)
except DivisionPorCeroError as e:
    print("Error:", e)