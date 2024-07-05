import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog
import os
import pyperclip
import platform
import webbrowser
import subprocess
import win32api
import win32con
import random

script_dir = os.path.dirname(__file__)

CORRECT_KEY1 = "PermFreeKeyForJob483gfjn54jkghnytuhsdk49gjkemf39jhfgdgdfgdg4g¤GRH&#¤E&%/&"
CORRECT_KEY2 = "@p0NVB}vtJ[\l^r0<]6Y'?A^&XV0$+C08pg%/E`:£2Yg,EnbD~!)k3Vwu_6GQCr0MCU/)N1S3eRLm`niKVovQ5fdsiojfui45jg954jgfiogj5yioutjmgfkhjmytoihjfkglhjt6iohjfiho"
CORRECT_KEY3 = "7UqUVmcRZjZTwXSBBMRK6V7gPYn3XYAf9dwU3oZQusNaGX6gjB2auKQjZdNQrWLnCdXyzSyqtw5pBxiJBPL4fSC2s3qfqzZT6g2d7JnRe9bdTvtxrtCWkkoAonRfhK7qoZvnQKSsBRmZfEZS3PHWCZwqVh7EoakRXQPfGuhN4kPxQAqkGrzTNKJWRru75LprbVFQyAfDcFN6GrYSkPVtJgwJqwugvc824vcf2dkaAAYrGww5LQ5AwLcenDSxTgvhSJDeuEt3dbhR#prSdwEyECRDpcV%qdPG@@*JeA4Ab$5$Z&kaoQwFrRocppemxotxspgenjDEQH7Bsqf5wxWoL^LKqKXS#g7cSZK6EQh$Kw!rTXtMdZXHXDzD@oC8EKQKgAFFpU9*BrZjSASaXhGy8Ci%H*33M&m3a*P4N6NjcY@g4sKhiuo&gm!sWc7VR$2B@NcWy3PU9#cMP8A@P7*fLX7%zCns&Wx4*B&6oaEYqkCz47d9dG5WMSrVZPXodqr6"
PREMIUM_KEY = "GiftedByOwnerKey"

# Initial state of topmost (0 = off, 1 = on)
topmost_enabled = 0
premium_enabled = False

links = [
    "https://link-target.net/1199116/darkwarev28",
    "https://direct-link.net/1199116/darkwarev27",
    "https://direct-link.net/1199116/darkwarev26",
    "https://direct-link.net/1199116/darkwarev25",
    "https://link-hub.net/1199116/darkwarev24",
    "https://link-center.net/1199116/darkwarev2",
    "https://direct-link.net/1199116/darkware-v2",
    "https://link-center.net/1199116/darkwarev23",
    "https://direct-link.net/1199116/darkware-v2",
    "https://link-center.net/1199116/darkwarev22",
    "https://link-target.net/1199116/darkwarev21",
    "https://link-center.net/1199116/darkwarev2",
]

def validate_key():
    entered_key = key_entry.get().strip()
    if entered_key in [CORRECT_KEY1, CORRECT_KEY2, CORRECT_KEY3, PREMIUM_KEY]:
        messagebox.showinfo("Success", "Key is valid.")
        key_entry.delete(0, tk.END)
        show_main_window(entered_key == PREMIUM_KEY)
    else:
        messagebox.showerror("Error", "Invalid key.")

def copy_key_link():
    link = random.choice(links)
    pyperclip.copy(link)
    messagebox.showinfo("Copied", "Key link copied to clipboard.")

def check_windows_version():
    try:
        product_info = win32api.GetVersionEx()
        major_version = product_info[0]
        minor_version = product_info[1]
        build_number = product_info[2]
        platform_id = product_info[3]
        csd_version = product_info[4]

        # Check if it's Windows 10 or 11
        if (major_version == 10 and build_number >= 22000) or (major_version == 11):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking Windows version: {e}")
        return False

def open_buy_link():
    buy_link = "https://www.productkeys.com/product/windows-11-professional-retail/?utm_source=Google%20Shopping&utm_campaign=ProductKeys-GoogleFeed-DK&utm_medium=cpc&utm_term=5041&gad_source=1&gclid=Cj0KCQjw7ZO0BhDYARIsAFttkChb_QtB3x6Yteomf5_lD35Y0SPBWAqUMFc13U4iTHv8nOBwNlsXZYgaAhgQEALw_wcB"
    webbrowser.open(buy_link)

def toggle_topmost():
    global topmost_enabled
    if topmost_enabled == 1:
        root.attributes("-topmost", 0)  # Disable topmost
        topmost_enabled = 0
    else:
        root.attributes("-topmost", 1)  # Enable topmost
        topmost_enabled = 1

def toggle_topmost_with_key():
    global premium_enabled
    entered_key = simpledialog.askstring("Enter Premium Key", "Enter Premium key to enable topmost:")
    if entered_key == PREMIUM_KEY:
        toggle_topmost()
        premium_enabled = True
        apply_rainbow_outline(canvas, outline_rect_main)
        apply_rainbow_outline(canvas, outline_rect_textbox)
    else:
        messagebox.showerror("Invalid Key", "Premium key is incorrect.")

def inject_button_click():
    if check_windows_version():
        injector_path = os.path.join(script_dir, "Injector", "DarkWareV2Injector.exe")
        if os.path.exists(injector_path):
            subprocess.run(injector_path, check=True)
        else:
            messagebox.showerror("Error", "Injector executable not found.")
    else:
        response = messagebox.askquestion("Need Windows Pro Version", "You need a Windows Pro version. Would you like to buy it?")
        if response == "yes":
            open_buy_link()

def show_main_window(is_premium):
    global premium_enabled, outline_rect_main, outline_rect_textbox, canvas
    premium_enabled = is_premium

    key_frame.pack_forget()
    main_frame.pack(fill=tk.BOTH, expand=True)

    image_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Background.png")
    if os.path.exists(image_path):
        image = PhotoImage(file=image_path)
        image_width = image.width()
        image_height = image.height()

        root.geometry(f"{image_width}x{image_height}")

        canvas = tk.Canvas(main_frame, width=image_width, height=image_height, highlightthickness=0)
        canvas.pack()

        canvas.create_image(0, 0, anchor='nw', image=image)
        main_frame.image = image

        # Create a text box in the center of the main window
        text_box = tk.Text(main_frame, bd=5, font=('Arial', 12), foreground='black', background='white', wrap=tk.WORD)
        text_box.config(state=tk.NORMAL)  # Make the text box editable
        text_box_width = 300
        text_box_height = 200
        text_box_x = (image_width - text_box_width) // 2
        text_box_y = (image_height - text_box_height) // 2
        canvas.create_window(text_box_x, text_box_y, anchor='nw', width=text_box_width, height=text_box_height, window=text_box)

        # Main window rainbow outline
        outline_rect_main = canvas.create_rectangle(0, 0, image_width, image_height, width=10, outline='')

        # Text box rainbow outline
        outline_rect_textbox = canvas.create_rectangle(text_box_x, text_box_y, text_box_x + text_box_width, text_box_y + text_box_height, width=10, outline='')

        if is_premium:
            apply_rainbow_outline(canvas, outline_rect_main)
            apply_rainbow_outline(canvas, outline_rect_textbox)

        # Function to handle window dragging
        def start_drag(event):
            global x, y
            x = event.x
            y = event.y

        def drag_window(event):
            x_new = event.x_root - x
            y_new = event.y_root - y
            root.geometry(f"+{x_new}+{y_new}")

        canvas.bind("<ButtonPress-1>", start_drag)
        canvas.bind("<B1-Motion>", drag_window)

        # Create buttons on the main window
        inject_button = tk.Button(main_frame, text="Inject", command=inject_button_click)
        inject_button_window = canvas.create_window(image_width - 100, image_height - 50, anchor='nw', window=inject_button)

        copy_key_link_button = tk.Button(main_frame, text="Copy Key Link", command=copy_key_link)
        copy_key_link_button_window = canvas.create_window(20, image_height - 50, anchor='nw', window=copy_key_link_button)

    else:
        messagebox.showerror("Image Error", "DarkWareV2Background.png not found.")

def apply_rainbow_outline(canvas, item_id):
    def change_color():
        colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3']
        color = random.choice(colors)
        canvas.itemconfigure(item_id, outline=color)
        root.after(100, change_color)

    change_color()

# Create main window
root = tk.Tk()
root.title("DarkWare V2")
root.iconbitmap(os.path.join(script_dir, "Icons", "darkware_icon.ico"))

# Create frames
key_frame = tk.Frame(root)
main_frame = tk.Frame(root)

# Show key entry frame initially
key_frame.pack(fill=tk.BOTH, expand=True)

# Create and position key entry widgets
key_label = tk.Label(key_frame, text="Enter Key:")
key_label.pack(pady=10)

key_entry = tk.Entry(key_frame, width=50)
key_entry.pack(padx=10, pady=5)

validate_button = tk.Button(key_frame, text="Validate Key", command=validate_key)
validate_button.pack(pady=10)

toggle_topmost_button = tk.Button(key_frame, text="Toggle Topmost", command=toggle_topmost_with_key)
toggle_topmost_button.pack()

root.mainloop()
