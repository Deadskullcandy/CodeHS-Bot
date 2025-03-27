# CodeHS-Bot

A bot that can make it look like it is writing the code instead of copy pasting.

✅ Step-by-Step Guide: Setting Up and Running Python Code with PyAutoGUI from VS Code
🛠️ Part 1: For Windows
💻 Step 1: Install the Required Software
Download and Install VS Code

Go to: VS Code Download

Click on the “Download for Windows” button.

Once the installer downloads, open it and follow the installation instructions.

During installation:

Select “Add to PATH (recommended)”.

Check the box for “Install Python and related tools” (if available).

Install Python

Go to: Python Download

Click the “Download Python” button.

Open the installer and check the box that says Add Python to PATH.

Click Install Now and wait for the installation to complete.

To confirm the installation:

Open Command Prompt (Press Win + R, type cmd, and press Enter).

Type:

shell
Copy
Edit
python --version
If you see the version number, Python is installed correctly.

Install Git (Optional but Recommended)

Go to: Git Download

Download and install Git by following the installation instructions.

Git is useful for version control but not necessary for PyAutoGUI.

⚙️ Step 2: Install and Run PyAutoGUI
Open VS Code

Click on Start Menu → search for Visual Studio Code → open it.

Install Python Extension

In VS Code, click on the Extensions icon (left sidebar).

Search for Python and install the one from Microsoft.

Restart VS Code after installation.

Open the Terminal in VS Code

Go to Terminal → New Terminal.

Install PyAutoGUI

In the terminal, type the following command and press Enter:

shell
Copy
Edit
pip install pyautogui
Create a Python File

Go to File → New File → Save it with a .py extension (e.g., script.py).

Add your PyAutoGUI code inside the file.

Set the File Path

If you want to read from a specific file, specify the path like this:

python
Copy
Edit
file_path = r"C:\Users\<YourUsername>\Desktop\example.txt"
with open(file_path, "r") as file:
    content = file.read()
print(content)
Replace <YourUsername> with your Windows username.

Use double backslashes \\ in file paths or add an r before the path to prevent escape sequence errors.

Run the Code

Click on the Run button (green triangle) or press F5.

You should see the script running and typing out the content.

🍎 Part 2: For macOS
💻 Step 1: Install the Required Software
Download and Install VS Code

Go to: VS Code Download

Click on “Download for macOS”.

Open the .zip file and drag Visual Studio Code.app into your Applications folder.

Install Python

Go to: Python Download

Click “Download Python” for macOS.

Open the .pkg installer and follow the installation steps.

To verify Python is installed:

Open Terminal (Cmd + Space → search Terminal).

Type:

shell
Copy
Edit
python3 --version
If you see a version number, Python is installed.

Install Git (Optional)

Open Terminal and type:

shell
Copy
Edit
xcode-select --install
This installs Git along with command-line developer tools.

⚙️ Step 2: Install and Run PyAutoGUI
Open VS Code

Go to Applications → Visual Studio Code → open it.

Install Python Extension

In VS Code, click the Extensions icon.

Search for Python and install the one by Microsoft.

Restart VS Code.

Open Terminal in VS Code

Go to Terminal → New Terminal.

Install PyAutoGUI

In the terminal, type:

shell
Copy
Edit
pip3 install pyautogui
Create a Python File

Go to File → New File → Save it with a .py extension (e.g., script.py).

Add your PyAutoGUI code inside the file.

Set the File Path

Use this format for macOS:

python
Copy
Edit
file_path = "/Users/<YourUsername>/Desktop/example.txt"
with open(file_path, "r") as file:
    content = file.read()
print(content)
Replace <YourUsername> with your macOS username.

Run the Code

Click the Run button (green triangle) or press F5.

Your PyAutoGUI script should start running.

✅ Key Differences Between Windows and macOS
File Path Format:

Windows uses C:\ format with double backslashes or raw string prefix (r"C:\path\to\file").

macOS uses /Users/username/ format with regular slashes.

Python Command:

Windows: python

macOS: python3

Terminal Navigation:

Windows: Command Prompt (cmd)

macOS: Terminal

🎯 Troubleshooting Tips
VS Code not recognizing Python:

Close and reopen VS Code.

Verify Python is added to PATH.

Use the Command Palette (Ctrl + Shift + P → Python: Select Interpreter) and select the correct Python interpreter.

PyAutoGUI not working on macOS:

Go to System Preferences → Security & Privacy → Accessibility.

Click the lock, enter your password, and add Visual Studio Code to the list to allow automation permissions.

File Path Issues:

Always use raw strings (r"...") or double backslashes for Windows file paths.

Use standard / slashes for macOS.

