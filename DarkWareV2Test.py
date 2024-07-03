import ctypes
import tkinter as tk
import time

# Function to change desktop background to solid black
def change_background_to_black():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "black.jpg", 0)

# Function to display error pop-up window
def display_error_popup():
    root = tk.Tk()
    root.title("Error")
    label = tk.Label(root, text="Error installing injector. Try again. Couldn't find injector.", padx=10, pady=10)
    label.pack()
    root.mainloop()

# Main function
def main():
    duration = 60  # Duration in seconds
    interval = 0.1  # Interval in seconds

    end_time = time.time() + duration
    while time.time() < end_time:
        change_background_to_black()
        display_error_popup()
        time.sleep(interval)

if __name__ == "__main__":
    main()
