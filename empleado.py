#clase empleado que abstraiga la funcionalidad de las clases EmpleadoEventual y EmpleadoPermanente.
class Empleado:
     def __init__(self, nombre, apellido, dni, salario, antiguedad,ventas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.antiguedad = antiguedad
        self.ventas = ventas

    def calcular_comision(self):
        comision = self.salario * self.antiguedad / 100
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
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni} - Salario: {self.salario}\n"
        texto += f"Antigüedad: {self.antiguedad}\n"
        return texto