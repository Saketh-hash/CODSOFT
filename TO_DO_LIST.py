import tkinter as tk
from tkinter import messagebox
class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        add_task_button = tk.Button(root, text="Add Task", command=self.addtask)
        add_task_button.pack(pady=5)
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=15)
        update_task_button = tk.Button(root, text="Update Task", command=self.updatetask)
        update_task_button.pack(pady=5)
        delete_task_button = tk.Button(root, text="Delete Task", command=self.deletetask)
        delete_task_button.pack()
        clear_entry_button = tk.Button(root, text="Clear Entry", command=self.clearentry)
        clear_entry_button.pack(pady=5)
        clear_all_button = tk.Button(root, text="Clear All Tasks", command=self.clearalltasks)
        clear_all_button.pack(pady=5)
        self.populatelistbox()
    def populatelistbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    def addtask(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.populatelistbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    def updatetask(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.populatelistbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")
    def deletetask(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.populatelistbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    def clearentry(self):
        self.task_entry.delete(0, tk.END)
    def clearalltasks(self):
        self.tasks = []
        self.populatelistbox()
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()
