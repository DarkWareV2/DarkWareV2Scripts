import tkinter as tk
from tkinter import PhotoImage, messagebox
import os
import pyperclip

script_dir = os.path.dirname(__file__)

CORRECT_KEY = "OwnerKey"

def validate_key():
    entered_key = key_entry.get().strip()
    if entered_key == CORRECT_KEY:
        messagebox.showinfo("Success", "Key is valid.")
        key_entry.delete(0, tk.END)
        show_main_window()
    else:
        messagebox.showerror("Error", "Invalid key.")

def copy_key_link():
    link = "https://direct-link.net/1192813/darkwarev2-key-system"
    pyperclip.copy(link)
    messagebox.showinfo("Copied", "Key link copied to clipboard.")

def show_main_window():
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

            def on_injector_click():
                # Placeholder function
                print("Injector button clicked")

            injector_button = tk.Button(main_frame, image=injector_button_image, bd=0, highlightthickness=0, command=on_injector_click)
            injector_button.image = injector_button_image
            canvas.create_window(image_width - injector_button_image.width() - button_margin, image_height - injector_button_image.height() - button_margin, anchor='nw', window=injector_button)

        executer_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Executer.png")
        if os.path.exists(executer_button_path):
            executer_button_image = PhotoImage(file=executer_button_path)

            def on_executer_click():
                # Placeholder function
                print("Executer button clicked")

            executer_button = tk.Button(main_frame, image=executer_button_image, bd=0, highlightthickness=0, command=on_executer_click)
            executer_button.image = executer_button_image
            canvas.create_window(image_width - injector_button_image.width() - executer_button_image.width() - button_margin * 2, image_height - executer_button_image.height() - button_margin, anchor='nw', window=executer_button)

    else:
        print(f"Error: The background image 'DarkWareV2Background.png' does not exist in the directory '{script_dir}'.")

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
