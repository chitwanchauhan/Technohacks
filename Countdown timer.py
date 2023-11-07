import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.time_remaining = 0
        self.is_running = False

        self.label = tk.Label(root, text="Countdown Timer")
        self.label.pack()

        self.display = tk.Label(root, text="")
        self.display.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)

        self.start_button.pack()
        self.stop_button.pack()
        self.reset_button.pack()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.time_remaining = self.time_remaining_entry.get()
            self.countdown()

    def countdown(self):
        if self.time_remaining > 0 and self.is_running:
            self.display.config(text=f"Time left: {self.time_remaining} seconds")
            self.time_remaining -= 1
            self.root.after(1000, self.countdown)
        elif self.is_running:
            self.is_running = False
            self.display.config(text="Time's up!")
            messagebox.showinfo("Countdown Timer", "Time's up!")

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.display.config(text="")
        self.time_remaining = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)

    app.time_remaining_entry = tk.IntVar()
    time_entry_label = tk.Label(root, text="Enter time in seconds:")
    time_entry = tk.Entry(root, textvariable=app.time_remaining_entry)
    time_entry_label.pack()
    time_entry.pack()

    root.mainloop()
