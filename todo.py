import tkinter as tk
from tkinter import messagebox

class SmartTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Smart To-Do List")
        self.root.geometry("450x550")
        self.root.config(bg="#1e1e2f")

        self.tasks = []

        self.create_ui()

    def create_ui(self):
        # Title
        tk.Label(self.root, text="📝 Smart To-Do List",
                 font=("Arial", 20, "bold"),
                 bg="#1e1e2f", fg="white").pack(pady=10)

        # Entry
        self.entry = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Priority
        self.priority_var = tk.StringVar(value="🟡 Medium")
        tk.OptionMenu(self.root, self.priority_var,
                      "🔴 High", "🟡 Medium", "🟢 Low").pack(pady=5)

        # Buttons
        tk.Button(self.root, text="➕ Add Task",
                  command=self.add_task,
                  bg="#4CAF50", fg="white", width=20).pack(pady=5)

        self.listbox = tk.Listbox(self.root, width=40, height=15,
                                 font=("Arial", 12),
                                 bg="#2e2e3e", fg="white")
        self.listbox.pack(pady=10)

        tk.Button(self.root, text="✔ Mark Done",
                  command=self.mark_done,
                  bg="#2196F3", fg="white", width=20).pack(pady=5)

        tk.Button(self.root, text="🗑 Delete Task",
                  command=self.delete_task,
                  bg="#f44336", fg="white", width=20).pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        priority = self.priority_var.get()

        if task:
            full_task = f"{priority} 🔹 {task}"
            self.tasks.append(full_task)
            self.listbox.insert(tk.END, full_task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task!")

    def delete_task(self):
        try:
            selected = self.listbox.curselection()[0]
            self.listbox.delete(selected)
            self.tasks.pop(selected)
        except:
            messagebox.showwarning("Warning", "Select a task!")

    def mark_done(self):
        try:
            selected = self.listbox.curselection()[0]
            task = self.listbox.get(selected)
            self.listbox.delete(selected)
            self.listbox.insert(tk.END, "✅ " + task)
        except:
            messagebox.showwarning("Warning", "Select a task!")


# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartTodoApp(root)
    root.mainloop()