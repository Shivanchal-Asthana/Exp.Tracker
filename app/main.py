import tkinter as tk
from tkinter import messagebox
from logic import add_expense, calculate_total, export_csv


def add_expense_gui():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()

        if not category:
            raise ValueError("Category cannot be empty")

        add_expense(amount, category)
        update_total()

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Expense Added!")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def update_total():
    total = calculate_total()
    total_label.config(text=f"Total Expense: ₹{total:.2f}")


def export_data():
    export_csv()
    messagebox.showinfo("Success", "Data exported to expenses.csv")


# GUI Setup
root = tk.Tk()
root.title("AI Expense Tracker")
root.geometry("400x300")

tk.Label(root, text="Amount").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack(pady=5)
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense_gui).pack(pady=10)
tk.Button(root, text="Export CSV", command=export_data).pack(pady=5)

total_label = tk.Label(root, text="Total Expense: ₹0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=20)

update_total()

root.mainloop()
