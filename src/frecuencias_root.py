import tkinter as tk
from tkinter import ttk
from frecuencias.analizador import Analizador
from frecuencias.categoria import Categoria
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import networkx as nx
import os

class Interfaz:
    def __init__(self, resultados_por_categoria):
        self.resultados = resultados_por_categoria

    def mostrar(self):
        root = tk.Tk()
        root.title("Frecuencia de Variables por Categoría")
        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True)

        for categoria, contador in self.resultados.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=categoria)
            texto = tk.Text(frame, wrap='none', height=25, width=80)
            texto.pack(fill='both', expand=True)
            for variable, frecuencia in contador.most_common():
                texto.insert(tk.END, f"{variable}: {frecuencia}\n")

        # Cuando se cierre la ventana tkinter se ejecutan los gráficos
        root.protocol("WM_DELETE_WINDOW", lambda: self._cerrar_interfaz(root))
        root.mainloop()

    def _cerrar_interfaz(self, root):
        root.destroy()
        self.mostrar_nube_palabras()
        self.mostrar_grafo_co_word()

    def mostrar_nube_palabras(self):
        # Combinar todas las frecuencias de todas las categorías para la nube general
        total_counter = Counter()
        for contador in self.resultados.values():
            total_counter.update(contador)

        if not total_counter:
            print("No hay datos para generar la nube de palabras.")
            return

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(total_counter)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title("Nube de Palabras - Análisis General")
        plt.show()

    def mostrar_grafo_co_word(self):
        # Construcción básica de un grafo co-word con variables que aparecen juntas en categorías
        G = nx.Graph()

        # Por simplicidad, crear aristas entre variables que aparecen en la misma categoría (puedes ajustar lógica)
        for contador in self.resultados.values():
            variables = list(contador.keys())
            for i in range(len(variables)):
                for j in range(i + 1, len(variables)):
                    # Incrementar peso por co-ocurrencia (podría ser 1 o frecuencia mínima)
                    if G.has_edge(variables[i], variables[j]):
                        G[variables[i]][variables[j]]['weight'] += 1
                    else:
                        G.add_edge(variables[i], variables[j], weight=1)

        if G.number_of_nodes() == 0:
            print("No hay datos para generar el grafo co-word.")
            return

        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(G, k=0.5)
        weights = [data['weight'] for _, _, data in G.edges(data=True)]
        nx.draw_networkx_nodes(G, pos, node_color='lightyellow', node_size=500)
        nx.draw_networkx_edges(G, pos, width=weights, edge_color='lightblue')
        nx.draw_networkx_labels(G, pos, font_size=8)
        plt.title("Grafo Co-word (Co-ocurrencia de Variables)")
        plt.axis('off')
        plt.show()

    def inicializar(self):
        ruta_bib = "archivo_unificado.bib"
        ruta_categorias = "frecuencias/archivos"
        archivos = os.listdir(ruta_categorias)

        categorias = []
        for archivo in archivos:
            if archivo.endswith('.csv'):
                nombre_categoria = archivo.replace('.csv', '').replace('_', ' ').title()
                ruta = os.path.join(ruta_categorias, archivo)
                categorias.append(Categoria(nombre_categoria, ruta))

        analizador = Analizador(ruta_bib)
        resultados = {}

        # Analizar categorías individuales
        for cat in categorias:
            resultados[cat.nombre] = analizador.contar_variables(cat)

        # Crear categoría temporal general con todas las variables juntas
        from frecuencias.categoria import CategoriaTemporal

        todas_variables = []
        for cat in categorias:
            todas_variables.extend(cat.variables)

        categoria_general = CategoriaTemporal("Análisis General", todas_variables)
        resultados[categoria_general.nombre] = analizador.contar_variables(categoria_general)

        interfaz = Interfaz(resultados)
        interfaz.mostrar()


