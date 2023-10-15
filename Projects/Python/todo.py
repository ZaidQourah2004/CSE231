import tkinter as tk
import tkcalendar
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
from tkinter.simpledialog import askstring
import json
import os
import platform
import sys
from tkinter import messagebox
from functools import partial
from datetime import date
from PIL import Image, ImageTk
import time
from datetime import datetime, timedelta
from tkinter import filedialog

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        master.geometry("1400x1200")

        # Set app style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), background="#2c2c2c", foreground="#000000", padding=0)
        style.configure("TEntry", font=("Helvetica", 12), foreground="#000000", padding=0)
        style.configure("TListbox", font=("Helvetica", 12), background="#f0f0f0", foreground="#000000", padding=0)
        
        self.task_list = self.load_tasks()
        self.category_list = self.load_categories()

        self.entry = ttk.Entry(master)
        self.entry.grid(row=0, column=1, padx=0, pady=0)

        self.add_button = ttk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=0, pady=0)

        self.delete_button = ttk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=0, pady=0)

        self.listbox = tk.Listbox(master, selectmode='extended')
        self.listbox.grid(row=1, columnspan=6, padx=0, pady=0, sticky="nsew")

        # Priority dropdown menu
        self.priority_var = tk.StringVar()
        self.priority_combo = ttk.Combobox(master, textvariable=self.priority_var, state="readonly")
        self.priority_combo['values'] = ("High", "Medium", "Low")
        self.priority_combo.current(1)  # Set default priority to "Medium"
        self.priority_combo.grid(row=0, column=3, padx=0, pady=0)

        # Category dropdown menu
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(master, textvariable=self.category_var, state="readonly")
        self.category_combo['values'] = self.category_list
        self.category_combo.current(0)  # Set default category
        self.category_combo.grid(row=0, column=4, padx=0, pady=0)

        # Manage categories button
        self.manage_categories_button = ttk.Button(master, text="Manage Categories", command=self.manage_categories)
        self.manage_categories_button.grid(row=0, column=5, padx=0, pady=0)

        # Filtering Buttons

        self.filter_due_date_button = ttk.Button(master, text="Filter by Due Date", command=self.filter_by_due_date)
        self.filter_due_date_button.grid(row=2, column=0, padx=0, pady=0)

        self.filter_priority_button = ttk.Button(master, text="Filter by Priority", command=self.filter_by_priority)
        self.filter_priority_button.grid(row=2, column=1, padx=0, pady=0)

        self.filter_category_button = ttk.Button(master, text="Filter by Category", command=self.filter_by_category)
        self.filter_category_button.grid(row=2, column=2, padx=0, pady=0)

        # Due date picker
        self.date_var = tk.StringVar(value=date.today().strftime("%Y-%m-%d"))
        self.date_button = ttk.Button(master, text="Pick Due Date", command=self.open_date_picker)
        self.date_button.grid(row=0, column=6, padx=0, pady=0)
        self.date_label = ttk.Label(master, textvariable=self.date_var)
        self.date_label.grid(row=1, column=6, padx=0, pady=0)

        # Load tasks from the file
        for task in self.task_list:
            self.listbox.insert(tk.END, f"{task['category']} - {task['priority']}: {task['description']} (Due: {task['due_date']})")

        # Set column and row weights
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)
        master.columnconfigure(4, weight=1)
        master.columnconfigure(5, weight=1)
        master.columnconfigure(6, weight=1)
        master.columnconfigure(7, weight=1)
        master.rowconfigure(1, weight=1)
        
        self.edit_button = ttk.Button(master, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=0, column=7, padx=10, pady=10)

        master.bind('<Return>', lambda _: self.add_task())


        # OS-specific key bindings

        if platform.system() == 'Darwin':  # macOS
            modifier = 'Command'
        else:  # Windows, Linux, and others
            modifier = 'Control'

        master.bind(f'<{modifier}-a>', lambda _: self.add_task())
        master.bind(f'<{modifier}-d>', lambda _: self.delete_task())
        master.bind(f'<{modifier}-e>', lambda _: self.edit_task())

        # Bind Enter, Delete, and Backspace keys
        master.bind('<Return>', lambda _: self.add_task())


        # Set focus on the Entry widget
        self.entry.focus_set()


    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                tasks = []
                for task in tasks_data:
                    if type(task) == str:
                        task_dict = {'description': task, 'priority': 'Medium', 'due_date': '', 'category': 'Uncategorized'}
                        tasks.append(task_dict)
                    else:
                        if 'category' not in task:
                            task['category'] = 'Uncategorized'
                        tasks.append(task)
        else:
            tasks = []
        return tasks

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.task_list, file)

    def load_categories(self):
        if os.path.exists("categories.json"):
            with open("categories.json", "r") as file:
                categories = json.load(file)
        else:
            categories = ["General"]
        return categories

    def save_categories(self):
        with open("categories.json", "w") as file:
            json.dump(self.category_list, file)

    def add_task(self):
        task_description = self.entry.get()
        task_priority = self.priority_var.get()
        task_due_date = self.date_var.get()
        task_category = self.category_var.get()

        if task_description:
            task = {"description": task_description, "priority": task_priority, "due_date": task_due_date, "category": task_category}
            self.task_list.append(task)
            self.listbox.insert(tk.END, f"{task['category']} - {task['priority']}: {task['description']} (Due: {task['due_date']})")
            self.entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        selected_indices = self.listbox.curselection()
        
        if not selected_indices:
            messagebox.showerror("Error", "No task selected.")
            return

        response = messagebox.askyesno("Delete Task(s)", "Do you want to delete the selected task(s)?")

        if response:
            for index in reversed(selected_indices):
                self.listbox.delete(index)
                self.task_list.pop(index)  # Remove the task from the task list
            self.save_tasks()  # Save the updated task list



    def open_date_picker(self):
        def on_date_selected():
            selected_date = cal.selection_get()
            self.date_var.set(selected_date.strftime("%Y-%m-%d"))
            top.destroy()

        top = tk.Toplevel(self.master)
        cal = Calendar(top, selectmode="day")
        cal.pack(padx=10, pady=10)
        ttk.Button(top, text="Select", command=on_date_selected).pack(padx=10, pady=10)

    def manage_categories(self):
        def add_category():
            new_category = askstring("Add Category", "Enter category name:")
            if new_category and new_category not in self.category_list:
                self.category_list.append(new_category)
                category_listbox.insert(tk.END, new_category)
                self.category_combo['values'] = self.category_list
                self.save_categories()

        def delete_category():
            selected_category = category_listbox.curselection()
            if selected_category:
                category_listbox.delete(selected_category)
                self.category_list.pop(selected_category[0])
                self.category_combo['values'] = self.category_list
                self.save_categories()

        def rename_category():
            selected_category = category_listbox.curselection()
            if selected_category:
                old_category = self.category_list[selected_category[0]]
                new_category = askstring("Rename Category", "Enter new category name:")
                if new_category and new_category not in self.category_list:
                    self.category_list[selected_category[0]] = new_category
                    category_listbox.delete(selected_category)
                    category_listbox.insert(selected_category, new_category)
                    self.category_combo['values'] = self.category_list
                    self.save_categories()

        category_window = tk.Toplevel(self.master)
        category_window.title("Manage Categories")

        category_listbox = tk.Listbox(category_window)
        category_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        for category in self.category_list:
            category_listbox.insert(tk.END, category)

        add_button = ttk.Button(category_window, text="Add", command=add_category)
        add_button.pack(padx=10, pady=10)

        delete_button = ttk.Button(category_window, text="Delete", command=delete_category)
        delete_button.pack(padx=10, pady=10)

        rename_button = ttk.Button(category_window, text="Rename", command=rename_category)
        rename_button.pack(padx=10, pady=10)

    def filter_by_due_date(self):
        self.listbox.delete(0, tk.END)
        sorted_tasks = sorted(self.task_list, key=lambda x: x['due_date'])
        for task in sorted_tasks:
            self.listbox.insert(tk.END, f"{task['category']} - {task['priority']}: {task['description']} (Due: {task['due_date']})")

    def filter_by_priority(self):
        self.listbox.delete(0, tk.END)
        sorted_tasks = sorted(self.task_list, key=lambda x: x['priority'], reverse=True)
        for task in sorted_tasks:
            self.listbox.insert(tk.END, f"{task['category']} - {task['priority']}: {task['description']} (Due: {task['due_date']})")

    def filter_by_category(self):
        self.listbox.delete(0, tk.END)
        category = self.category_var.get()
        filtered_tasks = [task for task in self.task_list if task['category'] == category]
        for task in filtered_tasks:
            self.listbox.insert(tk.END, f"{task['category']} - {task['priority']}: {task['description']} (Due: {task['due_date']})")


    def edit_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task = self.task_list[selected_task_index[0]]
            # Create a new window to show the edit form
            edit_window = tk.Toplevel(self.master)
            edit_window.title("Edit Task")

            # Create input fields for the edit form
            description_label = ttk.Label(edit_window, text="Description:")
            description_label.grid(row=0, column=0, padx=10, pady=10)
            description_entry = ttk.Entry(edit_window)
            description_entry.insert(tk.END, selected_task['description'])
            description_entry.grid(row=0, column=1, padx=10, pady=10)

            priority_label = ttk.Label(edit_window, text="Priority:")
            priority_label.grid(row=1, column=0, padx=10, pady=10)
            priority_var = tk.StringVar(value=selected_task['priority'])
            priority_combo = ttk.Combobox(edit_window, textvariable=priority_var, state="readonly")
            priority_combo['values'] = ("High", "Medium", "Low")
            priority_combo.grid(row=1, column=1, padx=10, pady=10)

            category_label = ttk.Label(edit_window, text="Category:")
            category_label.grid(row=2, column=0, padx=10, pady=10)
            category_var = tk.StringVar(value=selected_task['category'])
            category_combo = ttk.Combobox(edit_window, textvariable=category_var, state="readonly")
            category_combo['values'] = self.category_list
            category_combo.grid(row=2, column=1, padx=10, pady=10)

            due_date_label = ttk.Label(edit_window, text="Due Date:")
            due_date_label.grid(row=3, column=0, padx=10, pady=10)
            date_var = tk.StringVar(value=selected_task['due_date'])
            date_entry = DateEntry(edit_window, width=12, background='darkblue',
                                foreground='white', borderwidth=2, textvariable=date_var)
            date_entry.grid(row=3, column=1, padx=10, pady=10)

            # Create a function to update the task with the new values
            def update_task():
                updated_task = {"description": description_entry.get(), "priority": priority_var.get(),
                                "due_date": date_var.get(), "category": category_var.get()}
                self.task_list[selected_task_index[0]] = updated_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, f"{updated_task['category']} - {updated_task['priority']}: {updated_task['description']} (Due: {updated_task['due_date']})")
                self.save_tasks()
                edit_window.destroy()

            # Create a button to save the changes
            save_button = ttk.Button(edit_window, text="Save Changes", command=update_task)
            save_button.grid(row=4, column=1, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()