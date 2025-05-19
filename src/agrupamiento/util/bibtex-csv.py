import os
import bibtexparser
import csv

# Rutas
ruta_bibtex = r'C:\Users\Bryan\Documents\btw\code\Programacion\AlgoritmosProyecto\src\main\resources'
ruta_csv = r'C:\Users\Bryan\Documents\btw\code\Programacion\AlgoritmosProyecto\src\main\java\bibl\agrupamiento\data\abstracts.csv'

# Crear lista de entradas
entradas = []

# Leer cada archivo .bib
for nombre_archivo in os.listdir(ruta_bibtex):
    if nombre_archivo.endswith('.bib'):
        with open(os.path.join(ruta_bibtex, nombre_archivo), encoding='utf-8') as archivo:
            parser = bibtexparser.load(archivo)
            for entrada in parser.entries:
                titulo = entrada.get('title', '').replace('\n', ' ').strip()
                resumen = entrada.get('abstract', '').replace('\n', ' ').strip()
                categoria = entrada.get('keywords', 'SinCategoría').split(',')[0].strip()
                if titulo and resumen:
                    entradas.append([titulo, resumen, categoria])

# Guardar en CSV
with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['titulo', 'contenido', 'categoria'])
    escritor.writerows(entradas)

print(f'{len(entradas)} abstracts exportados a {ruta_csv}')
