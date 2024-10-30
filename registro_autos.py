import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from calendario_hn import ejecutar_hoy_no_circula
from cal import run_calendar_app
def hoy_no_circula():
    ejecutar_hoy_no_circula()
class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Formulario de Registro de Cita")
        self.root.configure(bg="#F0F0F0")
        label_font = ("Arial", 10, "bold")
        entry_font = ("Arial", 10)
        style = ttk.Style()
        style.configure("TEntry", padding=5)
        main_frame = tk.Frame(self, bg="#F0F0F0", padx=20, pady=20)
        main_frame.pack()
        tk.Label(main_frame, text="Placa:", font=label_font, bg="#F0F0F0").grid(row=0, column=0, sticky="w", pady=5)
        self.placa_entry = ttk.Entry(main_frame, font=entry_font)
        self.placa_entry.grid(row=0, column=1, pady=5, padx=10)
        tk.Label(main_frame, text="Confirmar Placa:", font=label_font, bg="#F0F0F0").grid(row=1, column=0, sticky="w", pady=5)
        self.confirm_placa_entry = ttk.Entry(main_frame, font=entry_font)
        self.confirm_placa_entry.grid(row=1, column=1, pady=5, padx=10)
        tk.Label(main_frame, text="Serie:", font=label_font, bg="#F0F0F0").grid(row=2, column=0, sticky="w", pady=5)
        self.serie_entry = ttk.Entry(main_frame, font=entry_font)
        self.serie_entry.grid(row=2, column=1, pady=5, padx=10)
        tk.Label(main_frame, text="Confirmar Serie:", font=label_font, bg="#F0F0F0").grid(row=3, column=0, sticky="w", pady=5)
        self.confirm_serie_entry = ttk.Entry(main_frame, font=entry_font)
        self.confirm_serie_entry.grid(row=3, column=1, pady=5, padx=10)
        tk.Label(main_frame, text="Modelo:", font=label_font, bg="#F0F0F0").grid(row=4, column=0, sticky="w", pady=5)
        self.model_combo = ttk.Combobox(main_frame, values=["Modelo A", "Modelo B", "Modelo C"], font=entry_font)
        self.model_combo.grid(row=4, column=1, pady=5, padx=10)
        tk.Label(main_frame, text="Correo electrónico:", font=label_font, bg="#F0F0F0").grid(row=5, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(main_frame, font=entry_font)
        self.email_entry.grid(row=5, column=1, pady=5, padx=10)
        self.confirm_button = tk.Button(main_frame, text="Confirmar", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=run_calendar_app)
        self.confirm_button.grid(row=6, column=0, columnspan=2, pady=15)
def registrar_cita():
    ventana_cita = tk.Toplevel()
    ventana_cita.title("Registrar Cita")
    ventana_cita.geometry("400x400")
    app = MainView(ventana_cita)
    app.pack()
ventana = tk.Tk()
ventana.title("Interfaz de Opciones")
ventana.geometry("600x800")
ruta_imagen = "carro_-ai-brush-removebg-t00ggb6.png"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((700, 500))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.place(x=-250, y=200)
btn_hoy_no_circula = tk.Button(
    ventana,
    text="Hoy No Circula",
    command=hoy_no_circula,
    font=("Helvetica", 14),
    bg="lightblue",
    fg="black",
    width=15,
    height=2
)
btn_hoy_no_circula.place(x=100, y=100)
btn_registrar_cita = tk.Button(
    ventana,
    text="Registrar Cita",
    command=registrar_cita,
    font=("Helvetica", 14),
    bg="lightgreen",
    fg="black",
    width=15,
    height=2
)
btn_registrar_cita.place(x=300, y=100)
ventana.mainloop()