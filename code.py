import pyautogui
import time

# Path to the text file
file_path = "File path"  

# Delay before typing starts
print("You have 10 seconds to focus the typing area...")
time.sleep(3)

# Read the code from the text file
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Typing speed control
typing_speed = 0.3   # Adjust this value for typing speed (seconds per character)

# Type out the code
print("Typing started...")
for line in lines:
    clean_line = line.lstrip()  # Remove leading whitespace (tabs + spaces)
    
    # Type the line with the desired speed
    pyautogui.typewrite(clean_line, interval=typing_speed)
print("Typing completed.")
