import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from calendario_hn import ejecutar_hoy_no_circula
from inter import MainView
def hoy_no_circula():
    ejecutar_hoy_no_circula()
def abrir_formulario():
    nueva_ventana = tk.Toplevel(ventana)
    app = MainView(nueva_ventana)
    app.pack(pady=20)
def cerrar_ventana():
    ventana.destroy()
ventana = tk.Tk()
ventana.title("Interfaz de Opciones")
ventana.geometry("600x500")
ventana.configure(bg="#E7DCD5")
ruta_imagen = "carro_-ai-brush-removebg-t00ggb6.png"
imagen = Image.open(ruta_imagen).convert("RGBA")
imagen = imagen.resize((500, 300))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=imagen_tk, bd=0, highlightthickness=0)
label_imagen.image = imagen_tk
label_imagen.place(x=-250, y=200)
button_style = {
    'font': ("Georgia", 14, "bold"),
    'width': 5,
    'height': 1,
}
btn_hoy_no_circula = tk.Button(
    ventana,
    text="Ir",
    command=hoy_no_circula,
    bg="#bdffae",
    fg="black",
    **button_style
)
btn_hoy_no_circula.place(x=250, y=200)
btn_registrar_cita = tk.Button(
    ventana,
    text="Ir",
    bg="#bdffae",
    fg="black",
    command=abrir_formulario,
    **button_style
)
btn_registrar_cita.place(x=450, y=200)
btn_cerrar = tk.Button(
    ventana,
    text="Cerrar",
    command=cerrar_ventana,
    bg="red",
    fg="white",
    width=5,
    height=1,
    font=("Georgia", 14, "bold")
)
btn_cerrar.place(x=500, y=430)
header_label1 = tk.Label(ventana, text="Bienvenido a la Interfaz", font=("Georgia", 18, "bold"), bg="#E7DCD5")
header_label1.pack(pady=(20, 0))
header_label2 = tk.Label(ventana, text="Registro de citas", font=("Georgia", 18, "bold"), bg="#E7DCD5")
header_label2.pack(pady=(5, 20))
header_label3 = tk.Label(ventana, text="Hoy no circula", font=("Georgia", 18, "bold"), bg="#E7DCD5")
header_label3.place(x=200, y=150)
header_label4 = tk.Label(ventana, text="Registrar cita", font=("Georgia", 18, "bold"), bg="#E7DCD5")
header_label4.place(x=410, y=150)
ventana.mainloop()