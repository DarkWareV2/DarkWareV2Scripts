import tkinter as tk
import time

# Function to display error pop-up window
def display_error_popup():
    root = tk.Tk()
    root.title("Error")
    label = tk.Label(root, text="Error installing injector. Try again. Couldn't find injector.", padx=10, pady=10)
    label.pack()
    root.after(3000232, root.destroy)  # Close the window after 3 seconds (3000 milliseconds)
    root.mainloop()

# Main function
def main():
    duration = 60  # Duration in seconds
    interval = 0.1  # Interval in seconds

    end_time = time.time() + duration
    while time.time() < end_time:
        display_error_popup()
        time.sleep(interval)

if __name__ == "__main__":
    main()
