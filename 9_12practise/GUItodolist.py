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
        self.root.title("待办事项")

        self.todo_list = TodoList()
        self.tasks = []

        # 界面组件
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="任务:").grid(
            row=0, column=0, padx=5, pady=5)  # 第一行的标签
        self.task_entry = tk.Entry(self.root, width=40)  # 输入框
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)  # 第一行的输入框

        tk.Button(self.root, text="添加任务", command=self.add_task).grid(
            row=0, column=2, padx=5, pady=5)
        tk.Button(self.root, text="删除任务", command=self.remove_task).grid(
            row=1, column=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(
            self.root, selectmode=tk.SINGLE, width=50, height=10)  # 任务列表框
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
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

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            _, message = self.todo_list.remove_task(task)
            messagebox.showinfo("删除任务", message)
            self.update_task_list()
        else:
            messagebox.showwarning("选择错误", "请先选择一个任务")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = self.todo_list.get_tasks()
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListGUI(root)
    root.mainloop()
