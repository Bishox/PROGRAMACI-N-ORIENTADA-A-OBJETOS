import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Label para el campo de tarea
        self.task_label = tk.Label(root, text="Nombre de la Tarea:")
        self.task_label.grid(row=0, column=0, pady=5)

        # Campo de entrada para la tarea
        self.task_entry = tk.Entry(root, width=40, justify="center")
        self.task_entry.grid(row=1, column=0, pady=10)

        # Selector de fecha
        self.date_picker = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_picker.grid(row=2, column=0, pady=10)

        # Campo de entrada para la hora
        self.time_entry = tk.Entry(root, width=10)
        self.time_entry.grid(row=3, column=0, pady=10)
        self.time_entry.insert(0, "HH:MM")  # Placeholder

        # Botones
        self.add_button = tk.Button(root, text="AÃ±adir Tarea", command=self.add_task)
        self.add_button.grid(row=4, column=0, pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=5, column=0, pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=6, column=0, pady=5)

        # TÃ­tulos para tareas
        self.label = tk.Label(root, text="Tareas Pendientes", font=("Arial", 14))
        self.label.grid(row=7, column=0, pady=5)

        # Frame para tareas pendientes
        self.pending_frame = tk.Frame(root)
        self.pending_frame.grid(row=8, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.pending_tree = ttk.Treeview(self.pending_frame, columns=("Tarea", "Fecha", "Hora", "Estado"), show='headings')
        self.pending_tree.heading("Tarea", text="Tarea")
        self.pending_tree.heading("Fecha", text="Fecha")
        self.pending_tree.heading("Hora", text="Hora")
        self.pending_tree.heading("Estado", text="Estado")

        self.pending_scroll = ttk.Scrollbar(self.pending_frame, orient="vertical", command=self.pending_tree.yview)
        self.pending_tree.configure(yscrollcommand=self.pending_scroll.set)

        self.pending_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.pending_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # TÃ­tulo para tareas completadas
        self.completed_label = tk.Label(root, text="Tareas Completadas", font=("Arial", 14))
        self.completed_label.grid(row=9, column=0, pady=5)

        # Frame para tareas completadas
        self.completed_frame = tk.Frame(root)
        self.completed_frame.grid(row=10, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.completed_tree = ttk.Treeview(self.completed_frame, columns=("Tarea", "Fecha", "Hora", "Estado"), show='headings')
        self.completed_tree.heading("Tarea", text="Tarea")
        self.completed_tree.heading("Fecha", text="Fecha")
        self.completed_tree.heading("Hora", text="Hora")
        self.completed_tree.heading("Estado", text="Estado")

        self.completed_scroll = ttk.Scrollbar(self.completed_frame, orient="vertical", command=self.completed_tree.yview)
        self.completed_tree.configure(yscrollcommand=self.completed_scroll.set)

        self.completed_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.completed_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Hacer que los frames ocupen el mismo espacio
        self.root.grid_rowconfigure(8, weight=1)  # Pendientes
        self.root.grid_rowconfigure(10, weight=1)  # Completadas
        self.root.grid_columnconfigure(0, weight=1)

        # Vincular la tecla Enter para aÃ±adir tareas
        self.task_entry.bind("<Return>", self.add_task)  # Ajustado para usar el mÃ©todo directamente

    def add_task(self, event=None):  # event=None para manejar el caso de Enter
        task = self.task_entry.get()
        date_str = self.date_picker.get()
        time_str = self.time_entry.get()

        if task and time_str:
            try:
                # Validar formato de hora
                hour, minute = map(int, time_str.split(':'))
                if not (0 <= hour < 24) or not (0 <= minute < 60):
                    raise ValueError("Hora no vÃ¡lida")

                self.pending_tree.insert("", tk.END, values=(task, date_str, time_str, "Pendiente"))
                self.task_entry.delete(0, tk.END)
                self.time_entry.delete(0, tk.END)
                self.time_entry.insert(0, "HH:MM")  # Resetear placeholder
            except ValueError:
                messagebox.showwarning("Advertencia", "Formato de hora no vÃ¡lido. Usa 'HH:MM'.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea y la hora.")

    def complete_task(self):
        selected_item = self.pending_tree.selection()
        if selected_item:
            task = self.pending_tree.item(selected_item, "values")[0]
            date = self.pending_tree.item(selected_item, "values")[1]
            time = self.pending_tree.item(selected_item, "values")[2]
            self.pending_tree.item(selected_item, values=(task, date, time, "Completada"))
            
            # Mover la tarea a las completadas
            self.completed_tree.insert("", tk.END, values=(task, date, time, "Completada"))
            self.pending_tree.delete(selected_item)  # Eliminar de pendientes
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def delete_task(self):
        selected_item = self.pending_tree.selection()
        if selected_item:
            self.pending_tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x900")  # Ajusta el tamaÃ±o de la ventana
    app = TaskManager(root)
    root.mainloop()