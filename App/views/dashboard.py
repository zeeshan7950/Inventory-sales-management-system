import tkinter as tk
from tkinter import ttk
from app.utils.style import apply_main_style


class DashboardWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory & Sales Management - Dashboard")
        self.master.geometry("800x500")
        self.master.resizable(False, False)

        apply_main_style(self.master)

        # ---- TOP BAR ----
        top_frame = tk.Frame(self.master, bg="#2b2b2b", height=60)
        top_frame.pack(fill="x")

        tk.Label(
            top_frame,
            text="Inventory & Sales Management System",
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        # ---- SIDEBAR ----
        sidebar = tk.Frame(self.master, bg="#333333", width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(
            sidebar,
            text="MENU",
            bg="#333333",
            fg="white",
            font=("Arial", 14, "bold")
        ).pack(pady=20)

        # ---- SIDEBAR BUTTONS ----
        buttons = [
            ("Products", self.open_products),
            ("Stock In/Out", self.open_stock),
            ("Sales Invoice", self.open_sales),
            ("Customers", self.open_customers),
            ("Suppliers", self.open_suppliers),
            ("Reports", self.open_reports),
            ("Logout", self.logout)
        ]

        for text, command in buttons:
            ttk.Button(sidebar, text=text, width=20, command=command).pack(pady=7)

        # ---- MAIN CONTENT AREA ----
        self.main_content = tk.Frame(self.master, bg="white")
        self.main_content.pack(side="right", fill="both", expand=True)

        tk.Label(
            self.main_content,
            text="Welcome to the Dashboard!",
            font=("Arial", 20, "bold"),
            bg="white"
        ).pack(pady=50)

    # ------------- PLACEHOLDER WINDOWS -------------
    def open_products(self):
        self.show_message("Products Module Coming Soon!")

    def open_stock(self):
        self.show_message("Stock In/Out Module Coming Soon!")

    def open_sales(self):
        self.show_message("Sales & Invoice Module Coming Soon!")

    def open_customers(self):
        self.show_message("Customers Module Coming Soon!")

    def open_suppliers(self):
        self.show_message("Suppliers Module Coming Soon!")

    def open_reports(self):
        self.show_message("Reports Module Coming Soon!")

    def logout(self):
        self.master.destroy()
        from app.views.login import LoginWindow
        root = tk.Tk()
        LoginWindow(root)
        root.mainloop()

    # Message display
    def show_message(self, msg):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        tk.Label(
            self.main_content,
            text=msg,
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=50)
