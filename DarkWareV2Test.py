import subprocess
import time
import keyboard

# Function to rotate screen
def rotate_screen():
    subprocess.run(["DisplaySwitch.exe", "/rotate"])

# Main function
def main():
    duration = 60  # Duration in seconds
    interval = 0.5  # Interval in seconds

    end_time = time.time() + duration
    while time.time() < end_time:
        rotate_screen()
        time.sleep(interval)
        keyboard.press_and_release('esc') 
