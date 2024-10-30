import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

# --- Modelo ---
class CalendarModel:
    def __init__(self):
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

    def get_calendar(self, year, month):
        return calendar.monthcalendar(year, month)

# --- Vista ---
class CalendarView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Calendario MVC")
        
        # Componentes para el año y el mes
        self.year_var = tk.IntVar(value=datetime.now().year)
        self.month_var = tk.IntVar(value=datetime.now().month)

        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        # Entrada para el año
        tk.Label(top_frame, text="Año: ").grid(row=0, column=0)
        self.year_entry = tk.Entry(top_frame, textvariable=self.year_var, width=5)
        self.year_entry.grid(row=0, column=1)
        
        # Selección de mes
        tk.Label(top_frame, text="Mes: ").grid(row=0, column=2)
        self.month_combo = ttk.Combobox(top_frame, textvariable=self.month_var, values=list(range(1, 13)), width=3)
        self.month_combo.grid(row=0, column=3)
        
        # Botón para mostrar el calendario
        self.show_button = tk.Button(top_frame, text="Mostrar Calendario")
        self.show_button.grid(row=0, column=4, padx=10)
        
        # Frame para mostrar el calendario
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack()

    def set_controller(self, controller):
        # Asociar el controlador al botón
        self.show_button.config(command=controller.show_calendar)

    def update_calendar(self, calendar_data, year, month):
        # Limpiar el calendario actual
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        # Título con mes y año
        title = f"{calendar.month_name[month]} {year}"
        tk.Label(self.calendar_frame, text=title, font=("Arial", 16)).grid(row=0, column=0, columnspan=7)
        
        # Encabezados de los días de la semana
        days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for idx, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold")).grid(row=1, column=idx)

        # Mostrar los días del mes
        for row_idx, week in enumerate(calendar_data, start=2):
            for col_idx, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text="").grid(row=row_idx, column=col_idx)
                else:
                    tk.Label(self.calendar_frame, text=str(day)).grid(row=row_idx, column=col_idx)

# --- Controlador ---
class CalendarController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def show_calendar(self):
        # Obtener año y mes de la vista
        year = self.view.year_var.get()
        month = self.view.month_var.get()
        
        # Obtener datos del modelo
        calendar_data = self.model.get_calendar(year, month)
        
        # Actualizar la vista
        self.view.update_calendar(calendar_data, year, month)

# --- Configuración de la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    model = CalendarModel()
    view = CalendarView(root)
    controller = CalendarController(model, view)
    view.pack()
    root.mainloop()
