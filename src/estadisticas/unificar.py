import os
import bibtexparser

class Unificador():
    def unificar(self):
        ruta_carpeta = 'C:\\Users\\Bryan\\Documents\\btw\\code\\Programacion\\ProyectoAlgoritmos\\src\\resources'
        entradas_totales = []

        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith('.bib'):
                with open(os.path.join(ruta_carpeta, archivo), 'r', encoding='utf-8') as f:
                    bib_db = bibtexparser.load(f)
                    entradas_totales.extend(bib_db.entries)

        # Ahora creas un objeto BibDatabase con todas las entradas
        bib_unificado = bibtexparser.bibdatabase.BibDatabase()
        bib_unificado.entries = entradas_totales

        # Opcional: guardar en un archivo unificado
        with open('C:\\Users\\Bryan\\Documents\\btw\\code\\Programacion\\ProyectoAlgoritmos\\src\\estadisticas\\archivo_unificado.bib', 'w', encoding='utf-8') as f:
            writer = bibtexparser.bwriter.BibTexWriter()
            f.write(writer.write(bib_unificado))


