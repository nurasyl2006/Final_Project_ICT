

from datetime import datetime
import tkinter as tk
from tkinter import ttk

def number_of_days(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date_1 = datetime.strptime(date_str1, date_format)
    date_2 = datetime.strptime(date_str2, date_format)
    return abs((date_2 - date_1).days)

def calculate_days():
    date_str1 = entry_date1.get()
    date_str2 = entry_date2.get()
    result = number_of_days(date_str1, date_str2)
    label_result.config(text=f"Number of Days between the given Dates are: {result} days")


root = tk.Tk()
root.title("Калькулятор дней")


label_date1 = ttk.Label(root, text="Enter date 1 (yyyy-mm-dd):")
label_date1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_date1 = ttk.Entry(root)
entry_date1.grid(row=0, column=1, padx=10, pady=10)

label_date2 = ttk.Label(root, text="Enter date 2 (yyyy-mm-dd):")
label_date2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_date2 = ttk.Entry(root)
entry_date2.grid(row=1, column=1, padx=10, pady=10)


button_calculate = ttk.Button(root, text="Calculate", command=calculate_days)
button_calculate.grid(row=2, column=0, columnspan=2, pady=10)


label_result = ttk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()



