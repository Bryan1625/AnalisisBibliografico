import tkinter as tk
from tkinter import ttk
from src.agrupamiento import main
from citas_root import VentanaCitas
from estadisticas import unificar
from estadisticas.stats import ResumenEstadisticas
from frecuencias_root import Interfaz

# Funciones que se ejecutarán al presionar los botones
def extraer_citas():
    print("Extrayendo citas...")
    citas = VentanaCitas()
    citas.mainloop()

def mostrar_estadisticas():
    print("Mostrando estadísticas...")
    unificador = unificar.Unificador()
    unificador.unificar()
    stats = ResumenEstadisticas('estadisticas/archivo_unificado.bib')
    stats.mostrar()


def frecuencia_variables():
    print("Calculando frecuencia de variables...")
    interfaz = Interfaz({})
    interfaz.inicializar()


def analisis_similitud():
    print("Analizando similitud...")
    main.main()

def centrar_ventana(self, ancho, alto):
    pantalla_ancho = self.winfo_screenwidth()
    pantalla_alto = self.winfo_screenheight()
    x = (pantalla_ancho - ancho) // 2
    y = (pantalla_alto - alto) // 2
    self.geometry(f"{ancho}x{alto}+{x}+{y}")



if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Análisis bibliográfico de artículos científicos")
    ventana.geometry("400x300")
    centrar_ventana(ventana,400, 300)
    ventana.resizable(False, False)

    # Crear y posicionar el título
    titulo = ttk.Label(ventana, text="Análisis bibliográfico de artículos científicos", font=("Helvetica", 14, "bold"), wraplength=380, justify="center")
    titulo.pack(pady=20)

    # Crear los botones
    boton1 = ttk.Button(ventana, text="Extraer citas", command=extraer_citas)
    boton1.pack(pady=5)

    boton2 = ttk.Button(ventana, text="Estadísticas", command=mostrar_estadisticas)
    boton2.pack(pady=5)

    boton3 = ttk.Button(ventana, text="Frecuencia de variables", command=frecuencia_variables)
    boton3.pack(pady=5)

    boton4 = ttk.Button(ventana, text="Análisis de Similitud", command=analisis_similitud)
    boton4.pack(pady=5)

    # Ejecutar la interfaz
    ventana.mainloop()