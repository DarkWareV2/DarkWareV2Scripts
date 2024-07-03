import tkinter as tk
import time
import threading

# Function to display error pop-up window
def display_error_popup():
    root = tk.Tk()
    root.title("Error")
    label = tk.Label(root, text="Error installing injector. Try again. Couldn't find injector.", padx=10, pady=10)
    label.pack()
    root.after(3000, root.destroy)  # Close the window after 3 seconds (3000 milliseconds)
    root.mainloop()

# Function to continuously display error pop-ups
def continuous_error_popups():
    while True:
        display_error_popup()
        time.sleep(0.1)  # Adjust interval between pop-ups here

# Main function
def main():
    duration = 60  # Duration in seconds

    # Start a thread for continuous error pop-ups
    popup_thread = threading.Thread(target=continuous_error_popups)
    popup_thread.start()

    # Wait for the specified duration (or forever if duration is None)
    if duration:
        time.sleep(duration)
        popup_thread.join()  # Wait for the thread to complete

if __name__ == "__main__":
    main()
