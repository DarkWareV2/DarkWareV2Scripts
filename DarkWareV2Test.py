import pyautogui
import time

# Function to rotate the screen
def rotate_screen():
    pyautogui.hotkey('ctrl', 'alt', 'down')

# Main function
def main():
    duration = 60  # Duration in seconds
    interval = 0.5  # Interval in seconds

    end_time = time.time() + duration
    while time.time() < end_time:
        rotate_screen()
        time.sleep(interval)

    # Reset screen rotation at the end (optional)
    pyautogui.hotkey('ctrl', 'alt', 'up')

if __name__ == "__main__":
    main()
