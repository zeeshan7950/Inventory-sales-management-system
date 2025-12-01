import tkinter as tk
from tkinter import ttk, messagebox
from App.services.billing_service import BillingService

class BillingWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Invoice / Billing")
        self.master.geometry("800x550")
        self.master.resizable(False, False)
        self.master.config(bg="#f0f0f0")

        # Billing service (DB)
        self.billing_service = BillingService()

        # ---------- TITLE ----------
        tk.Label(
            self.master,
            text="Sales Invoice",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0"
        ).pack(pady=10)

        # ---------- CUSTOMER DETAILS ----------
        customer_frame = tk.LabelFrame(self.master, text="Customer Details", padx=10, pady=10, bg="#f0f0f0")
        customer_frame.pack(fill="x", padx=15, pady=5)

        tk.Label(customer_frame, text="Customer Name:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
        self.customer_name = tk.Entry(customer_frame, width=30)
        self.customer_name.grid(row=0, column=1, padx=5)

        tk.Label(customer_frame, text="Phone:", bg="#f0f0f0").grid(row=0, column=2, sticky="w", padx=20)
        self.customer_phone = tk.Entry(customer_frame, width=20)
        self.customer_phone.grid(row=0, column=3)

        # ---------- PRODUCT SELECTION ----------
        product_frame = tk.LabelFrame(self.master, text="Add Product", padx=10, pady=10, bg="#f0f0f0")
        product_frame.pack(fill="x", padx=15, pady=5)

        tk.Label(product_frame, text="Product Name:", bg="#f0f0f0").grid(row=0, column=0)
        self.product_name = tk.Entry(product_frame, width=25)
        self.product_name.grid(row=0, column=1, padx=10)

        tk.Label(product_frame, text="Price:", bg="#f0f0f0").grid(row=0, column=2)
        self.product_price = tk.Entry(product_frame, width=10)
        self.product_price.grid(row=0, column=3)

        tk.Label(product_frame, text="Qty:", bg="#f0f0f0").grid(row=0, column=4)
        self.product_qty = tk.Entry(product_frame, width=5)
        self.product_qty.grid(row=0, column=5, padx=10)

        ttk.Button(product_frame, text="Add Item", command=self.add_item).grid(row=0, column=6, padx=10)

        # ---------- INVOICE TABLE ----------
        table_frame = tk.Frame(self.master)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = ("name", "price", "qty", "total")
        self.invoice_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)

        self.invoice_table.heading("name", text="Product Name")
        self.invoice_table.heading("price", text="Price")
        self.invoice_table.heading("qty", text="Qty")
        self.invoice_table.heading("total", text="Total")

        self.invoice_table.column("name", width=200)
        self.invoice_table.column("price", width=80)
        self.invoice_table.column("qty", width=80)
        self.invoice_table.column("total", width=100)

        self.invoice_table.pack(fill="both", expand=True)

        # ---------- TOTAL BILL SECTION ----------
        bottom_frame = tk.Frame(self.master)
        bottom_frame.pack(fill="x", padx=15, pady=10)

        tk.Label(bottom_frame, text="Grand Total:", font=("Arial", 14, "bold")).pack(side="left")
        self.grand_total_var = tk.StringVar(value="0")
        tk.Label(bottom_frame, textvariable=self.grand_total_var, font=("Arial", 14, "bold")).pack(side="left", padx=10)

        ttk.Button(bottom_frame, text="Generate Bill", command=self.generate_bill).pack(side="right")
        ttk.Button(bottom_frame, text="Clear", command=self.clear_bill).pack(side="right", padx=10)

    # ------------------ FUNCTIONS ------------------
    def add_item(self):
        name = self.product_name.get()
        price = self.product_price.get()
        qty = self.product_qty.get()

        if not name or not price or not qty:
            messagebox.showwarning("Input Error", "Enter all fields!")
            return

        try:
            price = float(price)
            qty = int(qty)
        except ValueError:
            messagebox.showerror("Invalid Input", "Price must be number, Qty must be integer.")
            return

        total = price * qty
        self.invoice_table.insert("", "end", values=(name, price, qty, total))
        self.update_total()

        self.product_name.delete(0, "end")
        self.product_price.delete(0, "end")
        self.product_qty.delete(0, "end")

    def update_total(self):
        total_sum = 0
        for item in self.invoice_table.get_children():
            total_sum += float(self.invoice_table.item(item, "values")[3])
        self.grand_total_var.set(str(total_sum))

    def clear_bill(self):
        self.invoice_table.delete(*self.invoice_table.get_children())
        self.grand_total_var.set("0")
        self.customer_name.delete(0, "end")
        self.customer_phone.delete(0, "end")

    def generate_bill(self):
        if not self.invoice_table.get_children():
            messagebox.showwarning("Empty", "No items added in the bill!")
            return

        customer_name = self.customer_name.get().strip()
        customer_phone = self.customer_phone.get().strip()

        if not customer_name or not customer_phone:
            messagebox.showwarning("Input Error", "Enter customer details!")
            return

        # Save each item to DB
        for item in self.invoice_table.get_children():
            name, price, qty, total = self.invoice_table.item(item, "values")
            self.billing_service.save_bill_item(customer_name, customer_phone, name, float(price), int(qty), float(total))

        messagebox.showinfo("Bill Generated", f"Bill saved successfully!\nGrand Total: {self.grand_total_var.get()}")
        self.clear_bill()
