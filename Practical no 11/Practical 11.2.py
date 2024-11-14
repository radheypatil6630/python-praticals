import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter GUI")
root.geometry("500x300")
def show_text():
    input_text = entry.get()
    if input_text:
        label_output.config(text=f"Hii, {input_text}!")
    else:
        messagebox.showwarning("Warning", "Please enter some text as you like")

label_prompt = tk.Label(root, text="Enter your name:")
label_prompt.pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

button = tk.Button(root, text="Display", command=show_text)
button.pack(pady=10)

label_output = tk.Label(root, text="")
label_output.pack(pady=10)

root.mainloop()
