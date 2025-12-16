import tkinter as tk
from tkinter import messagebox

from order_detail import add_order, get_orders
from bill_generate import generate_bill
from feedback import take_feedback

# ---------- Main Window ----------
root = tk.Tk()
root.title("Patata Farm 🍔")
root.geometry("420x520")
root.resizable(False, False)

# ---------- Heading ----------
tk.Label(
    root,
    text="🍟 Welcome To Patata Farm 🍕",
    font=("Arial", 18, "bold"),
    fg="green"
).pack(pady=15)

# ---------- Quantity Input ----------
qty_var = tk.StringVar()

tk.Label(root, text="Enter Quantity:", font=("Arial", 12)).pack()
qty_entry = tk.Entry(root, textvariable=qty_var, font=("Arial", 12), width=10)
qty_entry.pack(pady=5)

# ---------- Functions ----------
def add_item(item, price):
    if qty_var.get() == "":
        messagebox.showwarning("Warning", "Please enter quantity")
        return

    qty = int(qty_var.get())
    add_order(item, price, qty)
    messagebox.showinfo("Order Added", f"{item} x {qty} added successfully")
    qty_var.set("")

def show_bill():
    orders = get_orders()
    if not orders:
        messagebox.showwarning("Empty", "No orders found")
        return

    bill_text = ""
    total = 0

    for item, price, qty in orders:
        amount = price * qty
        bill_text += f"{item}  x{qty}  = ₹{amount}\n"
        total += amount

    bill_text += "\n------------------\n"
    bill_text += f"Total Bill: ₹{total}"

    messagebox.showinfo("Your Bill", bill_text)
    take_feedback()

# ---------- Buttons ----------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(
    btn_frame, text="🍔 Burger (₹120)", width=20,
    command=lambda: add_item("Burger", 120)
).grid(row=0, column=0, pady=5)

tk.Button(
    btn_frame, text="🍕 Pizza (₹220)", width=20,
    command=lambda: add_item("Pizza", 220)
).grid(row=1, column=0, pady=5)

tk.Button(
    btn_frame, text="☕ Cold Coffee (₹80)", width=20,
    command=lambda: add_item("Cold Coffee", 80)
).grid(row=2, column=0, pady=5)

tk.Button(
    btn_frame, text="🍵 Chai (₹20)", width=20,
    command=lambda: add_item("Chai", 20)
).grid(row=3, column=0, pady=5)

# ---------- Generate Bill ----------
tk.Button(
    root,
    text="🧾 Generate Bill",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=25,
    command=show_bill
).pack(pady=15)

# ---------- Exit ----------
tk.Button(
    root,
    text="❌ Exit",
    width=15,
    command=root.destroy
).pack(pady=10)

root.mainloop()

