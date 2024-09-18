import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear un Frame para la visualización de eventos
        self.frame_events = tk.Frame(root)
        self.frame_events.pack(pady=10, padx=10)

        # Crear el TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_events, columns=("Date", "Time", "Description"), show="headings")
        self.tree.heading("Date", text="Fecha")
        self.tree.heading("Time", text="Hora")
        self.tree.heading("Description", text="Descripción")
        self.tree.pack()

        # Crear un Frame para los campos de entrada
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(pady=10, padx=10)

        # Etiquetas y campos de entrada
        tk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0, padx=5, sticky="W")
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_input, text="Hora:").grid(row=1, column=0, padx=5, sticky="W")

        # Crear los widgets Spinbox para la hora y minutos
        self.hour_spinbox = tk.Spinbox(self.frame_input, from_=0, to=23, format="%02.0f", width=3, state='readonly')
        self.minute_spinbox = tk.Spinbox(self.frame_input, from_=0, to=59, format="%02.0f", width=3, state='readonly')

        # Alineación y espaciado de los widgets
        self.hour_spinbox.grid(row=1, column=1, padx=(5, 0), sticky="W")
        tk.Label(self.frame_input, text=":").grid(row=1, column=1, padx=(35, 0), sticky="W")
        self.minute_spinbox.grid(row=1, column=1, padx=(55, 5), sticky="W")

        tk.Label(self.frame_input, text="Descripción:").grid(row=2, column=0, padx=5, sticky="W")
        self.desc_entry = tk.Entry(self.frame_input)
        self.desc_entry.grid(row=2, column=1, padx=5, sticky="W")

        # Botones
        self.add_button = tk.Button(self.frame_input, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=3, column=0, pady=10)

        self.delete_button = tk.Button(self.frame_input, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.grid(row=3, column=1, pady=10)

        self.exit_button = tk.Button(self.frame_input, text="Salir", command=root.quit)
        self.exit_button.grid(row=4, columnspan=2, pady=10)

        # Inicializar hora y minutos
        self.initialize_time()

    def initialize_time(self):
        """ Inicializa los Spinbox para la hora y minutos en 00:00 """
        self.hour_spinbox.delete(0, tk.END)
        self.hour_spinbox.insert(0, '00')
        self.minute_spinbox.delete(0, tk.END)
        self.minute_spinbox.insert(0, '00')

    def add_event(self):
        date = self.date_entry.get_date()
        hour = self.hour_spinbox.get().zfill(2)
        minute = self.minute_spinbox.get().zfill(2)
        time = f"{hour}:{minute}"
        description = self.desc_entry.get()

        if not date or not time or not description:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return

        self.tree.insert("", "end", values=(date, time, description))
        self.clear_entries()

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
        if confirm:
            self.tree.delete(selected_item)

    def clear_entries(self):
        self.date_entry.set_date(self.date_entry.get_date())  # Reiniciar la fecha al valor actual
        self.initialize_time()  # Reiniciar la hora al valor predeterminado
        self.desc_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
