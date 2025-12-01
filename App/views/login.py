import tkinter as tk
from tkinter import messagebox
from App.services.user_service import UserService
from App.utils.style import apply_main_style

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory & Sales Management - Login")
        self.master.geometry("450x350")
        self.master.resizable(False, False)

        apply_main_style(self.master)

        # DB service
        self.user_service = UserService()

        # Load logo image
        try:
            self.logo = tk.PhotoImage(file="App/assets/logo.png")  # Change path to your logo
            tk.Label(self.master, image=self.logo).pack(pady=10)
        except Exception as e:
            print("Logo not found:", e)

        # Frame
        self.frame = tk.Frame(self.master, padx=20, pady=20, bd=2, relief="ridge", bg="#f5f5f5")
        self.frame.pack(pady=10)

        # Title
        tk.Label(self.frame, text="Login", font=("Arial", 20, "bold"), bg="#f5f5f5").grid(row=0, column=0, columnspan=2, pady=10)

        # Username
        tk.Label(self.frame, text="Username:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, sticky="w")
        self.username_entry = tk.Entry(self.frame, width=25)
        self.username_entry.grid(row=1, column=1, pady=5)

        # Password
        tk.Label(self.frame, text="Password:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(self.frame, show="*", width=25)
        self.password_entry.grid(row=2, column=1, pady=5)

        # Login Button
        tk.Button(self.frame, text="Login", width=15, bg="#4caf50", fg="white", command=self.handle_login).grid(row=3, column=0, columnspan=2, pady=15)

        # Signup Button
        tk.Button(self.frame, text="Create Account", width=15, bg="#2196f3", fg="white", command=self.open_signup_window).grid(row=4, column=0, columnspan=2)

    # ---------- AUTH LOGIC ----------
    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        user = self.user_service.authenticate_user(username, password)

        if user:
            messagebox.showinfo("Success", f"Welcome {username}!")
            self.master.destroy()
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_dashboard(self):
        from App.views.dashboard import DashboardWindow
        root = tk.Tk()
        DashboardWindow(root)
        root.mainloop()

    def open_signup_window(self):
        SignupWindow(self.master, self.user_service)


# ---------- Signup Window with graphics ----------
class SignupWindow:
    def __init__(self, master, user_service):
        self.top = tk.Toplevel(master)
        self.top.title("Create Account")
        self.top.geometry("350x300")
        self.top.resizable(False, False)
        self.user_service = user_service

        # Frame
        self.frame = tk.Frame(self.top, padx=20, pady=20, bd=2, relief="ridge", bg="#f0f0f0")
        self.frame.pack(pady=10)

        # Logo/Image
        try:
            self.icon = tk.PhotoImage(file="App/assets/signup_icon.png")  # Change path to your image
            tk.Label(self.frame, image=self.icon, bg="#f0f0f0").pack(pady=5)
        except Exception as e:
            print("Signup icon not found:", e)

        # Username
        tk.Label(self.frame, text="Username:", bg="#f0f0f0").pack(pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(pady=5)

        # Password
        tk.Label(self.frame, text="Password:", bg="#f0f0f0").pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(pady=5)

        # Create Account button
        tk.Button(self.frame, text="Create Account", width=15, bg="#2196f3", fg="white", command=self.create_account).pack(pady=10)

    def create_account(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        success = self.user_service.create_user(username, password)
        if success:
            messagebox.showinfo("Success", "Account created successfully!")
            self.top.destroy()
        else:
            messagebox.showerror("Error", "Username already exists!")


# ------------------ RUN APP ------------------
if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
