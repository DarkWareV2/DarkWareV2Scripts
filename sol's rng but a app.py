import tkinter as tk
from tkinter import messagebox
import random
import json
import pygame
import os

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ROLL_BUTTON_TEXT = "Roll"
INVENTORY_BUTTON_TEXT = "Inventory"
AUTO_ROLL_TEXT = "Auto Roll"
DATA_FILE = "inventory.json"
AUTO_ROLL_INTERVAL = 1000  # in milliseconds (1 second)
ROLL_COOLDOWN = 500  # in milliseconds (0.5 seconds)
SOL_S_DELAY = 23000  # 23 seconds delay for Sol's item
SOUND_FILE_PATH = os.path.join(os.getcwd(), "Sounds SFX", "heavenly-music-gaming-sound-effect-hd-mp3cut.mp3")

# Rarity definitions
RARITIES = {
    1: "Common",
    2: "Uncommon",
    3: "Rare",
    4: "Epic",
    5: "Legendary",
    6: "Sol's",
    7: "Rip, nothing"
}

# Probabilities (cumulative)
RARITY_PROBABILITIES = {
    1: 0.50,   # 50% for Common
    2: 0.85,   # 35% for Uncommon (50% + 35%)
    3: 0.95,   # 10% for Rare (50% + 35% + 10%)
    4: 0.99,   # 4% for Epic (50% + 35% + 10% + 4%)
    5: 0.999,  # 1% for Legendary (50% + 35% + 10% + 4% + 1%)
    6: 1.00    # 0.1% for Sol's (50% + 35% + 10% + 4% + 1% + 0.1%)
}

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Item Roller")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Load inventory data from file
        self.inventory = self.load_inventory()

        # Create main frame
        self.main_frame = tk.Frame(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        # Roll button
        self.roll_button = tk.Button(self.main_frame, text=ROLL_BUTTON_TEXT, command=self.roll_item)
        self.roll_button.pack(pady=20)

        # Inventory button
        self.inventory_button = tk.Button(self.main_frame, text=INVENTORY_BUTTON_TEXT, command=self.show_inventory)
        self.inventory_button.pack(side=tk.BOTTOM, pady=20)

        # Auto Roll checkbox
        self.auto_roll_var = tk.BooleanVar()
        self.auto_roll_checkbutton = tk.Checkbutton(self.main_frame, text=AUTO_ROLL_TEXT, variable=self.auto_roll_var, command=self.toggle_auto_roll)
        self.auto_roll_checkbutton.pack(side=tk.TOP, anchor="ne", padx=20, pady=20)

        # Entry for commands
        self.command_entry = tk.Entry(self.main_frame)
        self.command_entry.pack(pady=10)
        self.command_entry.bind("<Return>", self.check_command)

        # Variables for managing auto-roll state and cooldown
        self.auto_roll_job = None
        self.current_message_box = None

        # Initialize pygame mixer
        pygame.mixer.init()

    def roll_item(self, show_message=True):
        rarity_roll = random.random()  # Get a random number between 0 and 1
        item_rarity = self.determine_rarity(rarity_roll)
        if show_message:
            self.show_message(f"You rolled: {item_rarity}", item_rarity)
        else:
            print(f"You rolled: {item_rarity}")

        # Add item to inventory
        if item_rarity in self.inventory:
            self.inventory[item_rarity] += 1
        else:
            self.inventory[item_rarity] = 1

        # Save inventory to file
        self.save_inventory()

        # Disable the roll button until an action is taken
        self.roll_button.config(state=tk.DISABLED)

    def determine_rarity(self, roll):
        for rarity, probability in RARITY_PROBABILITIES.items():
            if roll <= probability:
                return RARITIES[rarity]
        return "Rip, nothing"

    def show_inventory(self):
        inventory_text = "Inventory:\n"
        for rarity, count in self.inventory.items():
            inventory_text += f"{rarity}: {count}\n"
        messagebox.showinfo("Inventory", inventory_text)

    def show_message(self, msg, item_rarity):
        if self.current_message_box is not None and self.current_message_box.winfo_exists():
            self.current_message_box.destroy()

        msg_box = tk.Toplevel(self.root)
        self.current_message_box = msg_box
        msg_box.title("Message")
        tk.Label(msg_box, text=msg).pack(pady=10)

        # If "Sol's" item is rolled, play sound and disable buttons for 23 seconds
        if item_rarity == "Sol's":
            pygame.mixer.music.load(SOUND_FILE_PATH)
            pygame.mixer.music.play()
            claim_button = tk.Button(msg_box, text="Claim", state=tk.DISABLED, command=lambda: self.claim_item(msg_box, item_rarity))
            skip_button = tk.Button(msg_box, text="Skip", state=tk.DISABLED, command=lambda: self.skip_item(msg_box, item_rarity))
            self.root.after(SOL_S_DELAY, lambda: self.enable_buttons(claim_button, skip_button))
        else:
            claim_button = tk.Button(msg_box, text="Claim", command=lambda: self.claim_item(msg_box, item_rarity))
            skip_button = tk.Button(msg_box, text="Skip", command=lambda: self.skip_item(msg_box, item_rarity))

        claim_button.pack(side=tk.LEFT, padx=20, pady=20)
        skip_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def enable_buttons(self, claim_button, skip_button):
        claim_button.config(state=tk.NORMAL)
        skip_button.config(state=tk.NORMAL)

    def claim_item(self, msg_box, item_rarity):
        msg_box.destroy()
        self.enable_roll_button()
        print(f"Item {item_rarity} claimed.")

    def skip_item(self, msg_box, item_rarity):
        msg_box.destroy()
        if item_rarity in self.inventory and self.inventory[item_rarity] > 0:
            self.inventory[item_rarity] -= 1
            self.save_inventory()
        self.enable_roll_button()
        print(f"Item {item_rarity} skipped.")

    def enable_roll_button(self):
        self.roll_button.config(state=tk.NORMAL)

    def load_inventory(self):
        try:
            with open(DATA_FILE, 'r') as f:
                inventory_data = json.load(f)
        except FileNotFoundError:
            inventory_data = {}
        return inventory_data

    def save_inventory(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.inventory, f)

    def toggle_auto_roll(self):
        if self.auto_roll_var.get():
            self.auto_roll_job = self.root.after(AUTO_ROLL_INTERVAL, self.auto_roll)
        else:
            if self.auto_roll_job:
                self.root.after_cancel(self.auto_roll_job)
                self.auto_roll_job = None

    def auto_roll(self):
        if self.auto_roll_var.get():
            if self.current_message_box is not None and self.current_message_box.winfo_exists():
                self.current_message_box.destroy()
            self.roll_item(show_message=True)
            self.auto_roll_job = self.root.after(AUTO_ROLL_INTERVAL, self.auto_roll)

    def check_command(self, event):
        command = self.command_entry.get().strip()
        self.command_entry.delete(0, tk.END)
        if command == "BertramKey":
            self.add_item_to_inventory("Sol's")
            self.show_message("You received: Sol's", "Sol's")
            pygame.mixer.music.load(SOUND_FILE_PATH)
            pygame.mixer.music.play()
            return

        if command.startswith("/give @s "):
            item_name = command.split("/give @s ")[1].strip()
            for rarity in RARITIES.values():
                if rarity.lower() == item_name.lower():
                    self.add_item_to_inventory(rarity)
                    self.show_message(f"You received: {rarity}", rarity)
                    return

            self.show_message("Invalid item name!", "Error")

    def add_item_to_inventory(self, item_rarity):
        if item_rarity in self.inventory:
            self.inventory[item_rarity] += 1
        else:
            self.inventory[item_rarity] = 1
        self.save_inventory()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
