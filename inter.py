import tkinter as tk
from tkinter import ttk, messagebox
from cal import run_calendar_app
class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Formulario Principal")
        self.root.configure(bg="#F0F0F0")
        label_font = ("Arial", 10, "bold")
        entry_font = ("Arial", 10)
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
        self.confirm_button = tk.Button(main_frame, text="Confirmar", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=self.confirm)
        self.confirm_button.grid(row=6, column=0, columnspan=2, pady=15)
    def confirm(self):
        if not self.placa_entry.get() or not self.confirm_placa_entry.get() or not self.serie_entry.get() or not self.confirm_serie_entry.get() or not self.model_combo.get() or not self.email_entry.get():
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
            return
        self.root.withdraw()
        run_calendar_app()
        self.root.deiconify()
if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    app.pack(pady=20)
    root.mainloop()