import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import random
import os
from tkcalendar import Calendar

# Egyéni osztály a feladatok kezeléséhez


class TaskManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                task_id INTEGER PRIMARY KEY,
                                task_name TEXT NOT NULL,
                                priority TEXT NOT NULL
                              )''')
        self.conn.commit()

    def add_task(self, task_name, priority):
        self.cursor.execute("INSERT INTO tasks (task_name, priority) VALUES (?, ?)",
                            (task_name, priority))
        self.conn.commit()

    def remove_task(self, task_name):
        self.cursor.execute("DELETE FROM tasks WHERE task_name=?", (task_name,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# GUI létrehozása a tkinter segítségével


root = tk.Tk()
root.title("Feladatlista")

# A TaskManager osztály példányosítása
task_manager = TaskManager("tasks.db")

# GUI elemek létrehozása


def add_task():
    task = task_entry.get()
    priority = priority_combobox.get()
    date = cal.get_date()
    if task:
        task_manager.add_task(task, priority)
        task_list.insert(tk.END, f"{date} - {priority}: {task}")
        task_entry.delete(0, tk.END)


def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task = task_list.get(selected_task_index)
        task_name = task.split(": ")[1]
        task_manager.remove_task(task_name)
        task_list.delete(selected_task_index)


def save_tasks_to_file():
    tasks = task_list.get(0, tk.END)
    if not os.path.exists('tasks'):
        os.makedirs('tasks')
    with open('tasks/tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    messagebox.showinfo("Info", "Feladatok elmentve fájlba!")


def load_tasks_from_file():
    if os.path.exists('tasks/tasks.txt'):
        with open('tasks/tasks.txt', 'r') as file:
            tasks = file.readlines()

        current_tasks = task_list.get(0, tk.END)
        for task in tasks:
            task = task.strip()
            if task and task not in current_tasks:
                task_list.insert(tk.END, task)
    else:
        messagebox.showwarning("Figyelem", "A feladatok fájlja nem található!")


def select_random_task():
    tasks = task_list.get(0, tk.END)
    if tasks:
        random_task = random.choice(tasks)
        messagebox.showinfo("Véletlenszerű feladat", random_task)
    else:
        messagebox.showwarning("Figyelem", "Nincsenek elérhető feladatok!")


def befejezve():

    kivalasztott_feladat_index = task_list.curselection()
    if kivalasztott_feladat_index:
        feladat = task_list.get(kivalasztott_feladat_index)
        task_list.delete(kivalasztott_feladat_index)
        task_list.insert(kivalasztott_feladat_index, feladat + " - Befejezve")
    else:
        messagebox.showwarning("Figyelem", "Nincs kiválasztva feladat!")

# GUI elemek hozzáadása és konfigurálása


cal_label = tk.Label(root, text="Válasszon dátumot:", font=("Arial", 12))
cal_label.pack(padx=20, pady=5, anchor=tk.W)
cal = Calendar(root, selectmode="day", year=2023, month=9, day=27, font=("Arial", 12))
cal.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

task_entry = tk.Entry(root, font=("Arial", 12))
task_entry.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
priority_label = tk.Label(root, text="Prioritás:", font=("Arial", 12))
priority_label.pack(pady=5, padx=20, anchor=tk.W)
priority_combobox = ttk.Combobox(root, values=("Magas", "Közepes", "Alacsony"), font=("Arial", 12))
priority_combobox.set("Közepes")
priority_combobox.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

add_button = tk.Button(root, text="Feladat hozzáadása", command=add_task, font=("Arial", 12))
add_button.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
remove_button = tk.Button(root, text="Feladat eltávolítása", command=remove_task, font=("Arial", 12))
remove_button.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
save_to_file_button = tk.Button(root, text="Feladatok mentése fájlba", command=save_tasks_to_file, font=("Arial", 12))
save_to_file_button.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
load_file_button = tk.Button(root, text="Feladatok betöltése fájlból", command=load_tasks_from_file, font=("Arial", 12))
load_file_button.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
random_button = tk.Button(root, text="Véletlenszerű feladat kiválasztása", command=select_random_task, font=("Arial", 12))
random_button.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
comleted_button = tk.Button(root, text="Feladat befejezése", command=befejezve, font=("Arial", 12))
comleted_button.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

task_list = tk.Listbox(root, font=("Arial", 12, "bold"))
task_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
