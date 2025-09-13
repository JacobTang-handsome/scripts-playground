import tkinter as tk
from tkinter import messagebox


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "存款金额必须为正数"
        self.balance += amount
        return True, f"存款成功，当前余额: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "取款金额必须为正数"
        if self.balance < amount:
            return False, "余额不足"
        self.balance -= amount
        return True, f"取款成功，当前余额: {self.balance}"

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        if amount <= 0:
            return False, "转账金额必须为正数"
        if self.balance >= amount:
            self.withdraw(amount)
            target_account.deposit(amount)
            return True, f"转账成功，当前余额: {self.balance}"
        else:
            return False, "余额不足，转账失败"


class BankAccountGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("银行账户管理")

        # 创建两个示例账户
        self.account1 = BankAccount(100)
        self.account2 = BankAccount(50)

        # 当前操作的账户
        self.current_account = self.account1

        # 界面组件
        self.create_widgets()

    def create_widgets(self):
        # 账户选择
        tk.Label(self.root, text="选择账户:").grid(
            row=0, column=0, padx=5, pady=5)  # 第一行的标签
        self.account_var = tk.StringVar(value="账户1")  # 账户选择变量
        tk.Radiobutton(self.root, text="账户1", variable=self.account_var, value="账户1",  # 单击选择账户1
                       # 第一行的单选按钮
                       command=self.switch_account).grid(row=0, column=1, padx=5, pady=5)
        tk.Radiobutton(self.root, text="账户2", variable=self.account_var, value="账户2",  # 单击选择账户2
                       # 第一行的单选按钮
                       command=self.switch_account).grid(row=0, column=2, padx=5, pady=5)

        # 余额显示
        tk.Label(self.root, text="当前余额:").grid(row=1, column=0, padx=5, pady=5)
        self.balance_label = tk.Label(
            self.root, text=str(self.current_account.get_balance()))
        self.balance_label.grid(row=1, column=1, padx=5, pady=5)  # 第二行的标签和余额显示

        # 金额输入
        tk.Label(self.root, text="金额:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.root)  # 金额输入框
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        # 操作按钮
        tk.Button(self.root, text="存款", command=self.deposit).grid(
            row=3, column=0, padx=5, pady=5)  # 第四行的按钮
        tk.Button(self.root, text="取款", command=self.withdraw).grid(
            row=3, column=1, padx=5, pady=5)  # 第四行的按钮
        tk.Button(self.root, text="转账到另一账户", command=self.transfer).grid(
            row=3, column=2, padx=5, pady=5)

    def switch_account(self):
        if self.account_var.get() == "账户1":
            self.current_account = self.account1  # 选择账户1
        else:
            self.current_account = self.account2  # 选择账户2
        self.update_balance_display()

    def update_balance_display(self):  # 更新余额显示
        self.balance_label.config(text=str(self.current_account.get_balance()))

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            success, msg = self.current_account.deposit(amount)
            messagebox.showinfo("提示", msg)  # 弹出信息框显示结果
            self.update_balance_display()  # 更新余额显示
            self.amount_entry.delete(0, tk.END)  # 清空输入框
        except ValueError:
            messagebox.showerror("错误", "请输入有效的金额")  # 弹出错误信息框

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            success, msg = self.current_account.withdraw(amount)
            messagebox.showinfo("提示", msg)  # 弹出信息框显示结果
            self.update_balance_display()  # 更新余额显示
            self.amount_entry.delete(0, tk.END)  # 清空输入框
        except ValueError:
            messagebox.showerror("错误", "请输入有效的金额")

    def transfer(self):
        target = self.account2 if self.current_account == self.account1 else self.account1  # 目标账户
        try:
            amount = float(self.amount_entry.get())
            success, msg = self.current_account.transfer(amount, target)
            messagebox.showinfo("提示", msg)  # 弹出信息框显示结果
            self.update_balance_display()  # 更新余额显示
            # 更新目标账户显示（如果当前显示的是目标账户）
            if self.account_var.get() == ("账户2" if self.current_account == self.account1 else "账户1"):
                self.update_balance_display()
            self.amount_entry.delete(0, tk.END)  # 清空输入框
        except ValueError:
            messagebox.showerror("错误", "请输入有效的金额")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankAccountGUI(root)
    root.mainloop()
