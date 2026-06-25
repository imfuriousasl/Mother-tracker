import tkinter as tk
from datetime import datetime

mothers = []

def add_mother():
    name = name_entry.get()
    mode = mode_var.get()

    today = datetime.today()

    if mode == "new":
        mothers.append({
            "name": name,
            "start_date": today,
            "base_days": 0
        })

    else:
        base = int(days_entry.get())
        mothers.append({
            "name": name,
            "start_date": today,
            "base_days": base
        })

    update_list()


def update_list():
    listbox.delete(0, tk.END)
    today = datetime.today()

    for m in mothers:
        days = (today - m["start_date"]).days + m["base_days"]
        listbox.insert(tk.END, f"{m['name']} → {days} days")


root = tk.Tk()
root.title("Mother Tracker")
root.geometry("400x500")

name_entry = tk.Entry(root)
name_entry.pack()

mode_var = tk.StringVar(value="new")

tk.Radiobutton(root, text="Start from 0", variable=mode_var, value="new").pack()
tk.Radiobutton(root, text="Already started", variable=mode_var, value="existing").pack()

days_entry = tk.Entry(root)
days_entry.pack()
days_entry.insert(0, "Enter days (if existing)")

tk.Button(root, text="Add", command=add_mother).pack()

listbox = tk.Listbox(root, width=40)
listbox.pack(fill="both", expand=True)

root.mainloop()