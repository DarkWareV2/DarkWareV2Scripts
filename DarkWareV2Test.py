import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog
import os
import pyperclip
import platform
import webbrowser
import subprocess

script_dir = os.path.dirname(__file__)

CORRECT_KEY = "FreeKeyYesSir"
PREMIUM_KEY = "PremiumKeyYesSir"

# Initial state of topmost (0 = off, 1 = on)
topmost_enabled = 0

def validate_key():
    entered_key = key_entry.get().strip()
    if entered_key == CORRECT_KEY:
        messagebox.showinfo("Success", "Key is valid.")
        key_entry.delete(0, tk.END)
        show_main_window(normal_key=True)
    elif entered_key == PREMIUM_KEY:
        messagebox.showinfo("Success", "Premium key is valid.")
        key_entry.delete(0, tk.END)
        show_main_window(normal_key=False)
    else:
        messagebox.showerror("Error", "Invalid key.")

def copy_key_link():
    link = "https://raw.githubusercontent.com/DarkWareV2/DarkWareV2Scripts/main/Key.txt"
    pyperclip.copy(link)
    messagebox.showinfo("Copied", "Key link copied to clipboard.")

def check_windows_version():
    version = platform.version()
    if "Professional" in version or "Pro" in version:
        return True
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

def show_main_window(normal_key=True):
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

        # Rainbow outline animation for the text box
        outline_rect = canvas.create_rectangle(text_box_x, text_box_y, text_box_x + text_box_width, text_box_y + text_box_height, width=10, outline='')

        rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]
        num_colors = len(rainbow_colors)
        color_index = 0

        def update_outline_color():
            nonlocal color_index
            color_index = (color_index + 1) % num_colors
            next_color_index = (color_index + 1) % num_colors

            current_color = rainbow_colors[color_index]
            next_color = rainbow_colors[next_color_index]

            blend_colors_smoothly(current_color, next_color, 0)

        def blend_colors_smoothly(color1, color2, step):
            def blend(color1, color2, ratio):
                r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:], 16)
                r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:], 16)

                r = int(r1 * (1 - ratio) + r2 * ratio)
                g = int(g1 * (1 - ratio) + g2 * ratio)
                b = int(b1 * (1 - ratio) + b2 * ratio)

                return f"#{r:02x}{g:02x}{b:02x}"

            if step > 10:
                return
            
            blend_color = blend(color1, color2, step / 10)
            canvas.itemconfig(outline_rect, outline=blend_color)
            root.after(50, blend_colors_smoothly, color1, color2, step + 1)

            if step == 10:
                root.after(200, update_outline_color)

        update_outline_color()

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

        # Create buttons
        button_margin = 10

        exit_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2ExitButton.png")
        if os.path.exists(exit_button_path):
            exit_button_image = PhotoImage(file=exit_button_path)
            exit_button = tk.Button(main_frame, image=exit_button_image, bd=0, highlightthickness=0, command=close_window)
            exit_button.image = exit_button_image
            canvas.create_window(image_width - exit_button_image.width() - button_margin, button_margin, anchor='nw', window=exit_button)

        injector_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Injector.png")
        if os.path.exists(injector_button_path):
            injector_button_image = PhotoImage(file=injector_button_path)
            injector_button = tk.Button(main_frame, image=injector_button_image, bd=0, highlightthickness=0, command=inject_button_click)
            injector_button.image = injector_button_image
            canvas.create_window(image_width - injector_button_image.width() - button_margin, image_height - injector_button_image.height() - button_margin, anchor='nw', window=injector_button)

        settings_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Settings.png")
        if os.path.exists(settings_button_path):
            settings_button_image = PhotoImage(file=settings_button_path)
            settings_button = tk.Button(main_frame, image=settings_button_image, bd=0, highlightthickness=0, command=open_settings_window)
            settings_button.image = settings_button_image
            canvas.create_window(button_margin, button_margin, anchor='nw', window=settings_button)

            if normal_key:
                lock_image_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Lock.png")
                if os.path.exists(lock_image_path):
                    lock_image = PhotoImage(file=lock_image_path)
                    lock_label = tk.Label(main_frame, image=lock_image, bd=0, highlightthickness=0)
                    lock_label.image = lock_image
                    canvas.create_window(button_margin, button_margin, anchor='nw', window=lock_label)

    else:
        print(f"Error: The background image 'DarkWareV2Background.png' does not exist in the directory '{script_dir}'.")

def open_settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.overrideredirect(True)  # Remove window decorations
    settings_window.geometry("400x300")

    settings_background_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2SettingsBackground.png")
    if os.path.exists(settings_background_path):
        settings_background_image = PhotoImage(file=settings_background_path)
        settings_background_label = tk.Label(settings_window, image=settings_background_image, bd=0, highlightthickness=0)
        settings_background_label.image = settings_background_image
        settings_background_label.pack()

        def close_settings_window():
            settings_window.destroy()

        close_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2ExitButton.png")
        if os.path.exists(close_button_path):
            close_button_image = PhotoImage(file=close_button_path)
            close_button = tk.Button(settings_window, image=close_button_image, bd=0, highlightthickness=0, command=close_settings_window)
            close_button.image = close_button_image
            close_button.pack(anchor='ne', padx=10, pady=10)

        toggle_topmost_button = tk.Button(settings_window, text="Toggle Topmost", font=('Arial', 14), command=toggle_topmost, state=tk.DISABLED)
        toggle_topmost_button.pack(pady=20)

        if key_entry.get().strip() == PREMIUM_KEY:
            toggle_topmost_button.config(state=tk.NORMAL)

    else:
        print(f"Error: The settings background image 'DarkWareV2SettingsBackground.png' does not exist in the directory '{script_dir}'.")

def close_window():
    root.destroy()

root = tk.Tk()
root.overrideredirect(True)

key_frame = tk.Frame(root)
key_frame.pack(fill=tk.BOTH, expand=True)

main_frame = tk.Frame(root)

key_entry = tk.Entry(key_frame, bd=5, font=('Arial', 14), foreground='black')
key_entry.pack(pady=20, side=tk.LEFT, padx=10)

validate_button = tk.Button(key_frame, text="Check Key", font=('Arial', 14), command=validate_key)
validate_button.pack(pady=20, side=tk.LEFT, padx=10)

copy_link_button = tk.Button(key_frame, text="Copy Key Link", font=('Arial', 14), command=copy_key_link)
copy_link_button.pack(pady=20, side=tk.LEFT, padx=10)

root.mainloop()
