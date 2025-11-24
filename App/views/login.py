import tkinter as tk
from tkinter import messagebox
import app.services.user_service
import app.utils.style


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory & Sales Management - Login")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        apply_main_style(self.master)

        # Frame
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(expand=True)

        # Title
        tk.Label(self.frame, text="Login", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # Username
        tk.Label(self.frame, text="Username:", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
        self.username_entry = tk.Entry(self.frame, width=25)
        self.username_entry.grid(row=1, column=1, pady=5)

        # Password
        tk.Label(self.frame, text="Password:", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(self.frame, show="*", width=25)
        self.password_entry.grid(row=2, column=1, pady=5)

        # Login Button
        tk.Button(self.frame, text="Login", width=15, command=self.handle_login).grid(row=3, column=0, columnspan=2, pady=15)

        # Signup Button (Optional)
        tk.Button(self.frame, text="Create Account", width=15, command=self.open_signup_window).grid(row=4, column=0, columnspan=2)

    # ---------- AUTH LOGIC ----------
    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        user_service = UserService()
        user = user_service.authenticate_user(username, password)

        if user:
            messagebox.showinfo("Success", f"Welcome {username}!")
            self.master.destroy()
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    # Placeholder for dashboard window
    def open_dashboard(self):
        from app.views.dashboard import DashboardWindow
        root = tk.Tk()
        DashboardWindow(root)
        root.mainloop()

    # Placeholder signup window
    def open_signup_window(self):
        messagebox.showinfo("Signup", "Signup window coming soon!")


# For direct testing (optional)
if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
