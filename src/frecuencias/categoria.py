import csv
import os

class Categoria:
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.variables = self._cargar_variables(ruta_archivo)

    def _cargar_variables(self, ruta):
        variables = []
        with open(ruta, encoding='utf-8') as f:
            reader = csv.reader(f)
            for fila in reader:
                if fila:
                    sinonimos = [v.strip().lower() for v in fila[0].split('-')]
                    variables.append(sinonimos)
        return variables

class CategoriaTemporal:
    def __init__(self, nombre, grupos_variables):
        self.nombre = nombre
        self.variables = grupos_variables