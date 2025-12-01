import tkinter as tk
from tkinter import ttk

def apply_main_style(window):
    window.configure(bg="#f2f2f2")

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TButton",
                    padding=6,
                    background="#4c8bf5",
                    foreground="white",
                    font=("Arial", 11, "bold"))

    style.map("TButton",
              background=[("active", "#3a6fd0")])

    style.configure("TLabel",
                    background="#f2f2f2",
                    foreground="#333",
                    font=("Arial", 12))

    style.configure("TEntry", padding=4)
