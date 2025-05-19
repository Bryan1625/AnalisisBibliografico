import tkinter as tk
from tkinter import ttk
from src.bib import Biblioteca

class VentanaCitas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Extracción de citas")
        self.geometry("400x250")
        self.centrar_ventana(400, 250)

        self.biblioteca = Biblioteca()
        self.biblioteca.cargar_credenciales()

        # Widgets
        label_busqueda = ttk.Label(self, text="Búsqueda:")
        label_busqueda.pack(pady=(20, 0))
        self.entry_busqueda = ttk.Entry(self, width=40)
        self.entry_busqueda.pack()

        label_cantidad = ttk.Label(self, text="Cantidad:")
        label_cantidad.pack(pady=(10, 0))
        self.entry_cantidad = ttk.Entry(self, width=40)
        self.entry_cantidad.pack()

        frame_botones = ttk.Frame(self)
        frame_botones.pack(pady=20)

        btn_ieee = ttk.Button(frame_botones, text="IEEE", command=lambda: self.on_click("IEEE"))
        btn_ieee.grid(row=0, column=0, padx=10)

        btn_sciencedirect = ttk.Button(frame_botones, text="Science Direct", command=lambda: self.on_click("Science Direct"))
        btn_sciencedirect.grid(row=0, column=1, padx=10)

        btn_sage = ttk.Button(frame_botones, text="SAGE", command=lambda: self.on_click("SAGE"))
        btn_sage.grid(row=0, column=2, padx=10)

    def on_click(self, fuente):
        busqueda = self.entry_busqueda.get()
        cantidad = self.entry_cantidad.get()
        print(f"Búsqueda: {busqueda}, Cantidad: {cantidad}, Fuente: {fuente}")

        if fuente == "IEEE":
            self.biblioteca.buscar_ieee(busqueda, int(cantidad))
        elif fuente == "Science Direct":
            self.biblioteca.buscar_sciencedirect(busqueda, int(cantidad))
        elif fuente == "SAGE":
            print("SAGE")
            self.biblioteca.buscar_sage(busqueda, int(cantidad))

    def centrar_ventana(self, ancho, alto):
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")