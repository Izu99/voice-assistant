import os
import subprocess

# Define a function to open Microsoft Edge on Windows
def open_edge():
    os.system("start microsoft-edge:")

# Define a function to open File Explorer
def open_explorer():
    os.system("start explorer")

# Define a function to open Microsoft Store
def open_store():
    os.system("start ms-windows-store:")

# Define a function to open vscode
def open_vscode():
    os.system("start code:")

def open_idm():
    try:
        # Launch Scrcpy using subprocess
        subprocess.run(["C:\Program Files (x86)\Internet Download Manager\IDMan.exe"])
        # If scrcpy is not in your system path, you might need to provide the full path to the executable:
        # subprocess.run(["C:/path/to/scrcpy.exe"])

    except Exception as e:
        print(f"Error opening IDM: {e}")

# Define a function to open Microsoft Store
def open_music():
    os.system("start mswindowsmusic:")


# Define functions to open other applications...
# You can add functions for Word, PowerPoint, Paint, Notepad, etc.

if __name__ == "__main__":
    # Add test calls for each function here if needed
    open_edge()  # Test opening Microsoft Edge
    open_file_explorer()  # Test opening File Explorer
    open_store()  # Test opening Microsoft Store
    open_scrcpy()
    open_music()
