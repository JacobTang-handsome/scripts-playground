import tkinter as tk
from tkinter import messagebox


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            return True, f"任务 '{task}' 已添加"
        return False, f"任务添加失败"

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True, f"任务 '{task}' 已删除"
        return False, f"任务删除失败"

    def get_tasks(self):
        return self.tasks


class TodoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("待办事项列表")

        self.todo_list = TodoList()
        self.tasks = []

        # 任务列表
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack()

        # 界面组件
        self.create_widgets()
        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            _, message = self.todo_list.add_task(task)
            messagebox.showinfo("添加任务", message)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("输入错误", "任务不能为空")

    def create_widgets(self):
        # 输入框
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        # 添加按钮
        self.add_button = tk.Button(
            self.root, text="添加任务", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # 任务列表
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # 删除按钮
        self.remove_button = tk.Button(
            self.root, text="删除任务", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def remove_task(self):
        selected_indices = self.task_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("选择错误", "请先选择一个任务")
            return
        for index in reversed(selected_indices):
            task = self.task_listbox.get(index)
            _, message = self.todo_list.remove_task(task)
            messagebox.showinfo("删除任务", message)
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.get_tasks():
            self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListGUI(root)
    root.mainloop()
