#!/usr/bin/python3
from empleado import Empleado
class EmpleadoPermanente(Empleado):
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.antiguedad = antiguedad

    def calcular_comision(self):
        comision = self.salario * self.antiguedad / 100
        return comision

    def mostrar_datos(self):
        texto = super().mostrar_datos()
        texto += f"Antigüedad: {self.antiguedad}\n"
        return texto
