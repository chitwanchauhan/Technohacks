import tkinter as tk
from tkinter import messagebox

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")  # Passwords should be hidden
        self.password_entry.pack()

        self.confirm_password_label = tk.Label(root, text="Confirm Password:")
        self.confirm_password_label.pack()

        self.confirm_password_entry = tk.Entry(root, show="*")
        self.confirm_password_entry.pack()

        self.register_button = tk.Button(root, text="Register", command=self.validate_registration)
        self.register_button.pack()

    def validate_registration(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            messagebox.showinfo("Success", "Registration successful!")
            # You can add code here to save the registration data to a database or perform other actions.

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
