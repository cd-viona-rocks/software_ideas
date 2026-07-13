import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root=None):
        self.root = root or tk.Tk()
        self.root.title("A very simple login screen")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.frames = {}
        self.current_frame = None

        self.create_screen("login", self.login_screen)
        self.create_screen("dashboard", self.dashboard_screen)
        self.show_screen("login")

    # - - - 

    def create_screen(self, name, builder):
        frame = builder()
        self.frames[name] = frame
        frame.pack_forget()

    def show_screen(self, name):
        if self.current_frame is not None:
            self.current_frame.pack_forget()

        self.current_frame = self.frames[name]
        self.current_frame.pack(fill="both", expand=True)

    # - - - 

    def login_screen(self):
        frame = tk.Frame(self.root, padx=20, pady=20)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.message_var = tk.StringVar()

        tk.Label(frame, text="Username", anchor="w").pack(fill="x")
        self.username_entry = tk.Entry(frame, textvariable=self.username_var)
        self.username_entry.pack(fill="x", pady=(0, 12))

        tk.Label(frame, text="Password", anchor="w").pack(fill="x")
        self.password_entry = tk.Entry(frame, textvariable=self.password_var, show="*")
        self.password_entry.pack(fill="x", pady=(0, 16))

        tk.Label(frame, textvariable=self.message_var, fg="red", anchor="w").pack(fill="x")

        button_frame = tk.Frame(frame)
        button_frame.pack(fill="x")

        tk.Button(
            button_frame,
            text="Forgot Password",
            command=self.forget_password,
        ).pack(side="left", padx=(0, 10))

        tk.Button(
            button_frame,
            text="Sign Up",
            command=self.register,
        ).pack(side="left")

        tk.Button(
            frame,
            text="Login",
            command=self.login,
        ).pack(fill="x", pady=(8, 0))

        return frame

    def dashboard_screen(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        label = tk.Label(frame, text="You are logged in.", font=("Arial", 12, "bold"))
        label.pack(pady=20)

        tk.Button(
            frame,
            text="Logout",
            command=lambda: self.show_screen("login"),
        ).pack(fill="x")

        return frame

    # - - -

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if username == "admin" and password == "1234":
            self.message_var.set("")
            self.show_screen("dashboard")
        else:
            self.message_var.set("Wrong username or password")

    def register(self):
        messagebox.showinfo("Sign Up", "Registration flow would go here.")

    def forget_password(self):
        messagebox.showinfo("Forgot Password", "Recovery flow would go here.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    App().run()
