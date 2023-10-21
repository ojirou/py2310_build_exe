import tkinter as tk
from tkinter import ttk
class ClickerWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("250x250")
        self.master.title("Clicker")
        self.label = ttk.Label(self.master, text="0", font=("Times New Roman", 80))
        self.label.pack(anchor="center", pady=40)
        self.button = ttk.Button(self.master, text="CLICK", command=self.click_btn)
        self.button.pack(anchor="center")
    def click_btn(self):
        i = int(self.label["text"]) + 1
        self.label["text"] = str(i)
        self.label.update()
if __name__ == "__main__":
    root = tk.Tk()
    app = ClickerWindow(master=root)
    app.mainloop()