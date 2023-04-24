# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:52:30 2023

@author: lab
"""

class employee:
    
    empcount=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount+=1
        
    def displaycount(self):
        print("total employee %d",employee.empcount)
        
    def displayemployee(self):
        print("name:",self.name, ",salary:", self.salary)
        
empleado1=employee("juan dpmingez",800)
empleado2=employee("sandra",900)
empleado3=employee("carlos",750)
empleado4=employee("lucas",1200)
empleado5=employee("sara",4000)
empleado6=employee("pepito",2500)
empleado1.displayemployee()
empleado2.displayemployee()
empleado3.displayemployee()
empleado4.displayemployee()
empleado5.displayemployee()
empleado6.displayemployee()
print("total employee %d",employee.empcount)