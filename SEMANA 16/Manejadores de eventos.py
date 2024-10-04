import tkinter as tk
from tkinter import messagebox, Listbox, StringVar


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", self.add_task)
        self.root.bind("<c>", self.complete_task)
        self.root.bind("<Delete>", self.delete_task)
        self.root.bind("<Escape>", self.root.quit)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            self.tasks[selected_index] = f"[✓] {task}"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
