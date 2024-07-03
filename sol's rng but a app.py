import tkinter as tk
from tkinter import messagebox
import random
import json

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ROLL_BUTTON_TEXT = "Roll"
INVENTORY_BUTTON_TEXT = "Inventory"
AUTO_ROLL_TEXT = "Auto Roll"
DATA_FILE = "inventory.json"
AUTO_ROLL_INTERVAL = 2000  # in milliseconds (2 seconds)

# Rarity definitions
RARITIES = {
    1: "Common",
    2: "Uncommon",
    3: "Rare",
    4: "Epic",
    5: "Legendary",
    6: "Rip, nothing"
}

# Probabilities (cumulative)
RARITY_PROBABILITIES = {
    1: 0.50,   # 50% for Common
    2: 0.85,   # 35% for Uncommon (50% + 35%)
    3: 0.95,   # 10% for Rare (50% + 35% + 10%)
    4: 0.995,  # 5% for Epic (50% + 35% + 10% + 5%)
    5: 0.996,  # 0.1% for Legendary (50% + 35% + 10% + 5% + 0.1%)
    6: 1.00    # Remainder for "Rip, nothing"
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

    def roll_item(self, show_message=True):
        rarity_roll = random.random()  # Get a random number between 0 and 1
        item_rarity = self.determine_rarity(rarity_roll)
        if show_message:
            self.show_message(f"You rolled: {item_rarity}")
        else:
            print(f"You rolled: {item_rarity}")

        # Add item to inventory
        if item_rarity in self.inventory:
            self.inventory[item_rarity] += 1
        else:
            self.inventory[item_rarity] = 1

        # Save inventory to file
        self.save_inventory()

    def determine_rarity(self, roll):
        for rarity, probability in RARITY_PROBABILITIES.items():
            if roll <= probability:
                return RARITIES[rarity]
        return "Rip, nothing"

    def show_inventory(self):
        inventory_text = "Inventory:\n"
        for rarity, count in self.inventory.items():
            inventory_text += f"{rarity}: {count}\n"
        self.show_message(inventory_text)

    def show_message(self, msg):
        messagebox.showinfo("Message", msg)

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
            self.auto_roll()
        else:
            self.root.after_cancel(self.auto_roll_job)

    def auto_roll(self):
        self.roll_item(show_message=False)
        self.auto_roll_job = self.root.after(AUTO_ROLL_INTERVAL, self.auto_roll)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

