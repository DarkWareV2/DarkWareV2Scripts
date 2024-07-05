import tkinter as tk
from tkinter import PhotoImage, messagebox
import os

# Function to handle window dragging
def start_drag(event):
    global x, y
    x = event.x
    y = event.y

def drag_window(event):
    x_new = root.winfo_x() + (event.x - x)
    y_new = root.winfo_y() + (event.y - y)
    root.geometry(f"+{x_new}+{y_new}")

def start_drag_settings(event):
    global x, y
    x = event.x
    y = event.y

def drag_settings_window(event):
    x_new = settings_window.winfo_x() + (event.x - x)
    y_new = settings_window.winfo_y() + (event.y - y)
    settings_window.geometry(f"+{x_new}+{y_new}")

# Function to close the window
def close_window():
    root.destroy()

# Placeholder function for Executer button click
def on_executer_click():
    print("Executer button clicked")

# Function to handle Settings button click
def on_settings_click():
    settings_image_name = "DarkWareV2SettingsBackground.png"
    settings_image_path = os.path.join("EXECUTER LOOKS", settings_image_name)

    if os.path.exists(settings_image_path):
        # Create a Toplevel window for settings
        global settings_window
        settings_window = tk.Toplevel(root)
        settings_window.overrideredirect(True)  # Remove window borders and title bar

        # Load and display the settings image
        settings_image = PhotoImage(file=settings_image_path)
        settings_label = tk.Label(settings_window, image=settings_image, bd=0)
        settings_label.pack()

        # Set window size based on image dimensions
        settings_window.geometry(f"{settings_image.width()}x{settings_image.height()}")

        # Bind escape key to close the settings window
        settings_window.bind("<Escape>", lambda event: settings_window.destroy())

        # Bind mouse events for window dragging
        settings_label.bind("<Button-1>", start_drag_settings)
        settings_label.bind("<B1-Motion>", drag_settings_window)

        settings_window.mainloop()
    else:
        messagebox.showerror("Error", f"{settings_image_name} not found in EXECUTER LOOKS folder.")

# Function to handle Injector button click
def open_injector():
    print("Injector button clicked")

# Create the main window without the title bar
root = tk.Tk()
root.overrideredirect(True)  # Remove window borders and title bar

# Define the image path relative to the script's directory
image_folder = os.path.join(os.path.dirname(__file__), "EXECUTER LOOKS")
image_name = "DarkWareV2Background.png"
image_path = os.path.join(image_folder, image_name)

# Check if the image file exists in the specified directory
if not os.path.exists(image_path):
    print(f"Error: The image '{image_name}' does not exist in the directory '{image_folder}'.")
    root.destroy()
else:
    # Load the image to get its dimensions
    image = PhotoImage(file=image_path)
    image_width = image.width()
    image_height = image.height()

    # Set window size to match the image dimensions
    root.geometry(f"{image_width}x{image_height}")

    # Create a canvas to cover the entire window
    canvas = tk.Canvas(root, width=image_width, height=image_height, highlightthickness=0)
    canvas.pack()

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor='nw', image=image)

    # Function to handle click on exit button
    def on_exit_click():
        close_window()

    # Margin for button placement
    button_margin = 10

    # Load and place the exit button image
    exit_button_path = os.path.join(image_folder, "DarkWareV2ExitButton.png")
    if os.path.exists(exit_button_path):
        exit_button_image = PhotoImage(file=exit_button_path)
        exit_button = tk.Button(root, image=exit_button_image, bd=0, highlightthickness=0, command=on_exit_click)
        exit_button.image = exit_button_image
        canvas.create_window(image_width - exit_button_image.width() - button_margin, button_margin, anchor='nw', window=exit_button)
    else:
        print(f"Error: The exit button image 'DarkWareV2ExitButton.png' does not exist in the directory '{image_folder}'.")

    # Load and place the injector button image
    injector_button_path = os.path.join(image_folder, "DarkWareV2Injector.png")
    if os.path.exists(injector_button_path):
        injector_button_image = PhotoImage(file=injector_button_path)

        # Define function to open injector
        def on_injector_click():
            open_injector()

        injector_button = tk.Button(root, image=injector_button_image, bd=0, highlightthickness=0, command=on_injector_click)
        injector_button.image = injector_button_image
        canvas.create_window(image_width - injector_button_image.width() - button_margin, image_height - injector_button_image.height() - button_margin, anchor='nw', window=injector_button)
    else:
        print(f"Error: The injector button image 'DarkWareV2Injector.png' does not exist in the directory '{image_folder}'.")

    # Load and place the executer button image
    executer_button_path = os.path.join(image_folder, "DarkWareV2Executer.png")
    if os.path.exists(executer_button_path):
        executer_button_image = PhotoImage(file=executer_button_path)
        executer_button = tk.Button(root, image=executer_button_image, bd=0, highlightthickness=0, command=on_executer_click)
        executer_button.image = executer_button_image
        canvas.create_window(image_width - injector_button_image.width() - executer_button_image.width() - button_margin * 2, image_height - executer_button_image.height() - button_margin, anchor='nw', window=executer_button)
    else:
        print(f"Error: The executer button image 'DarkWareV2Executer.png' does not exist in the directory '{image_folder}'.")

    # Load and place the settings button image
    settings_button_path = os.path.join(image_folder, "DarkWareV2Settings.png")
    if os.path.exists(settings_button_path):
        settings_button_image = PhotoImage(file=settings_button_path)
        settings_button = tk.Button(root, image=settings_button_image, bd=0, highlightthickness=0, command=on_settings_click)
        settings_button.image = settings_button_image
        canvas.create_window(image_width - settings_button_image.width() - button_margin, image_height - injector_button_image.height() - settings_button_image.height() - button_margin * 2, anchor='nw', window=settings_button)
    else:
        print(f"Error: The settings button image 'DarkWareV2Settings.png' does not exist in the directory '{image_folder}'.")

    # Create a rectangle on the canvas for the outline
    outline_rect = canvas.create_rectangle(0, 0, image_width, image_height, width=10, outline='')

    # List of colors for the rainbow effect
    rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]
    num_colors = len(rainbow_colors)

    # Function to update the outline color with smooth fading
    def update_outline_color():
        global color_index
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

    # Start the color update loop
    color_index = 0
    update_outline_color()

    # Bind mouse events for window dragging
    canvas.bind("<Button-1>", start_drag)
    canvas.bind("<B1-Motion>", drag_window)

    # Start the Tkinter event loop
    root.mainloop()
