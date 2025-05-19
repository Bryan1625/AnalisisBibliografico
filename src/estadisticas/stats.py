import tkinter as tk
from tkinter import ttk
import bibtexparser
from collections import Counter, defaultdict

class ResumenEstadisticas:
    def __init__(self, ruta_bibtex):
        self.ruta_bibtex = ruta_bibtex
        self.autor_contador = Counter()
        self.journal_contador = Counter()
        self.publisher_contador = Counter()
        self.tipo_producto_contador = Counter()
        self.anio_por_tipo = defaultdict(Counter)
        self.top_15_autores = []
        self.top_15_journals = []
        self.top_15_publishers = []
        self._procesar_archivo()

    def _procesar_archivo(self):
        with open(self.ruta_bibtex, encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)

        for entry in bib_database.entries:
            tipo = entry.get('ENTRYTYPE', '').lower()
            self.tipo_producto_contador[tipo] += 1

            year = entry.get('year', 'Unknown')

            autores = entry.get('author', '')
            primer_autor = autores.split(' and ')[0].strip() if autores else 'Unknown'
            self.autor_contador[primer_autor] += 1

            journal = entry.get('journal')
            if journal:
                self.journal_contador[journal] += 1

            publisher = entry.get('publisher')
            if publisher:
                self.publisher_contador[publisher] += 1

            self.anio_por_tipo[tipo][year] += 1

        self.top_15_autores = self.autor_contador.most_common(15)
        self.top_15_journals = self.journal_contador.most_common(15)
        self.top_15_publishers = self.publisher_contador.most_common(15)

    def _agregar_tab(self, notebook, titulo, datos):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=titulo)
        text = tk.Text(frame, wrap='none', height=25, width=100)
        text.pack(fill='both', expand=True)
        for linea in datos:
            text.insert(tk.END, linea + '\n')

    def mostrar(self):
        root = tk.Tk()
        root.title("Resumen BibTeX")

        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True)

        self._agregar_tab(notebook, "Top 15 Autores", [f"{a}: {c}" for a, c in self.top_15_autores])
        self._agregar_tab(notebook, "Top 15 Journals", [f"{j}: {c}" for j, c in self.top_15_journals])
        self._agregar_tab(notebook, "Top 15 Publishers", [f"{p}: {c}" for p, c in self.top_15_publishers])
        self._agregar_tab(notebook, "Tipos de Producto", [f"{t}: {c}" for t, c in self.tipo_producto_contador.items()])

        anio_tabla = []
        for tipo, anios in self.anio_por_tipo.items():
            anio_tabla.append(f"{tipo}:")
            for anio, c in sorted(anios.items()):
                anio_tabla.append(f"  {anio}: {c}")
        self._agregar_tab(notebook, "Año por Tipo", anio_tabla)

        root.mainloop()