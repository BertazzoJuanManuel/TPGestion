#!/usr/bin/python3

class EmpleadoEventual(Empleado):
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.ventas = ventas

    def calcular_comision(self):
        total_ventas = 0
        for una_venta in self.ventas:
            total_ventas = total_ventas + una_venta

        # O bien:
        # total_ventas = sum(self.ventas)
        
        porcentaje_comision = 0.05
        comision = total_ventas * porcentaje_comision
        return comision

    def calcular_ingreso_total(self):
        ingreso_total = self.salario + self.calcular_comision()
        return ingreso_total

    def coincide(self, texto_a_buscar):
        if texto_a_buscar in self.nombre or texto_a_buscar in self.apellido:
            return True
        else:
            return False

    def mostrar_datos(self):
        texto = super().mostrar_datos()
        texto += f"Ventas: {self.ventas}\n"
        return texto
