import tkinter as tk
from tkinter import ttk
from cal import run_calendar_app  # Importa la función para abrir el calendario

class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Formulario Principal")
        self.root.configure(bg="#F0F0F0")
        
        # Fuente y estilo general
        label_font = ("Arial", 10, "bold")
        entry_font = ("Arial", 10)
        
        # Estilo de entrada de texto
        style = ttk.Style()
        style.configure("TEntry", padding=5)
        
        # Marco principal
        main_frame = tk.Frame(self, bg="#F0F0F0", padx=20, pady=20)
        main_frame.pack()
        
        # Campo para "Placa"
        tk.Label(main_frame, text="Placa:", font=label_font, bg="#F0F0F0").grid(row=0, column=0, sticky="w", pady=5)
        self.placa_entry = ttk.Entry(main_frame, font=entry_font)
        self.placa_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Campo para "Confirmar Placa"
        tk.Label(main_frame, text="Confirmar Placa:", font=label_font, bg="#F0F0F0").grid(row=1, column=0, sticky="w", pady=5)
        self.confirm_placa_entry = ttk.Entry(main_frame, font=entry_font)
        self.confirm_placa_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Campo para "Serie"
        tk.Label(main_frame, text="Serie:", font=label_font, bg="#F0F0F0").grid(row=2, column=0, sticky="w", pady=5)
        self.serie_entry = ttk.Entry(main_frame, font=entry_font)
        self.serie_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Campo para "Confirmar Serie"
        tk.Label(main_frame, text="Confirmar Serie:", font=label_font, bg="#F0F0F0").grid(row=3, column=0, sticky="w", pady=5)
        self.confirm_serie_entry = ttk.Entry(main_frame, font=entry_font)
        self.confirm_serie_entry.grid(row=3, column=1, pady=5, padx=10)
        
        # Menú desplegable para "Modelo"
        tk.Label(main_frame, text="Modelo:", font=label_font, bg="#F0F0F0").grid(row=4, column=0, sticky="w", pady=5)
        self.model_combo = ttk.Combobox(main_frame, values=["Modelo A", "Modelo B", "Modelo C"], font=entry_font)
        self.model_combo.grid(row=4, column=1, pady=5, padx=10)
        
        # Campo para "Correo Electrónico"
        tk.Label(main_frame, text="Correo electrónico:", font=label_font, bg="#F0F0F0").grid(row=5, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(main_frame, font=entry_font)
        self.email_entry.grid(row=5, column=1, pady=5, padx=10)
        
        # Botón de confirmación
        self.confirm_button = tk.Button(main_frame, text="Confirmar", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=run_calendar_app)
        self.confirm_button.grid(row=6, column=0, columnspan=2, pady=15)
        
# --- Configuración de la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    app.pack(pady=20)
    root.mainloop()


