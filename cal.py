import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import datetime
class CalendarModel:
    def __init__(self):
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
    def get_calendar(self, year, month):
        return calendar.monthcalendar(year, month)
class CalendarView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Calendario MVC")
        self.year_var = tk.IntVar(value=datetime.now().year)
        self.month_var = tk.IntVar(value=datetime.now().month)
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)
        self.prev_button = tk.Button(top_frame, text="◀", command=self.prev_month)
        self.prev_button.grid(row=0, column=0)
        self.month_label = tk.Label(top_frame, text="", font=("Arial", 16))
        self.month_label.grid(row=0, column=1, padx=10)
        self.next_button = tk.Button(top_frame, text="▶", command=self.next_month)
        self.next_button.grid(row=0, column=2)
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack()
        self.selected_day_label = None
        self.selected_day = None
    def set_controller(self, controller):
        """Establece el controlador para la vista."""
        self.controller = controller
        self.show_calendar()  # Muestra el calendario después de establecer el controlador
    def update_calendar(self, calendar_data, year, month):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        title = f"{calendar.month_name[month]} {year}"
        self.month_label.config(text=title)  # Actualizar el título del mes
        days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for idx, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold")).grid(row=1, column=idx)
        for row_idx, week in enumerate(calendar_data, start=2):
            for col_idx, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text="").grid(row=row_idx, column=col_idx)
                else:
                    day_label = tk.Label(self.calendar_frame, text=str(day), relief="raised", width=5)
                    day_label.grid(row=row_idx, column=col_idx)
                    day_label.bind("<Button-1>", lambda e, d=day, label=day_label: self.select_day(d, label))
        self.confirm_button = tk.Button(self.calendar_frame, text="Confirmar Cita", command=self.confirm_appointment)
        self.confirm_button.grid(row=row_idx + 1, column=0, columnspan=7, pady=10)
    def show_calendar(self):
        year = self.year_var.get()
        month = self.month_var.get()
        calendar_data = self.controller.model.get_calendar(year, month)  # Usar el modelo del controlador
        self.update_calendar(calendar_data, year, month)
    def prev_month(self):
        """Cambia al mes anterior y actualiza el calendario."""
        month = self.month_var.get()
        year = self.year_var.get()
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
        self.year_var.set(year)
        self.month_var.set(month)
        self.show_calendar()
    def next_month(self):
        """Cambia al siguiente mes y actualiza el calendario."""
        month = self.month_var.get()
        year = self.year_var.get()
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        self.year_var.set(year)
        self.month_var.set(month)
        self.show_calendar()
    def select_day(self, day, label):
        if self.selected_day_label:
            self.selected_day_label.config(bg=self.calendar_frame.cget("bg"))
        self.selected_day = day
        self.selected_day_label = label
        label.config(bg="lightblue")
    def confirm_appointment(self):
        if self.selected_day:
            year = self.year_var.get()
            month = self.month_var.get()
            messagebox.showinfo("Cita Registrada", f"Cita registrada para el {self.selected_day}/{month}/{year}.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un día primero.")
class CalendarController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
def run_calendar_app():
    root = tk.Tk()
    model = CalendarModel()
    view = CalendarView(root)
    controller = CalendarController(model, view)
    view.pack()
    root.mainloop()
if __name__ == "__main__":
    run_calendar_app()