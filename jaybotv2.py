import sys
import os
import random
import tkinter as tk
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk  # For handling images

# Detect if running inside a PyInstaller bundle
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Extracted PyInstaller temp directory
else:
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory

# Define paths to required resources
splash_screen_path = os.path.join(base_path, "logo.jpg")  # Update with actual splash image filename
gui_image_path = os.path.join(base_path, "jar_image.jpeg")  # Update with actual GUI image filename
messages_folder = os.path.join(base_path, "messages")  # Ensure messages folder is properly accessed

class SplashScreen:
    def __init__(self, root, image_path, duration=3000):
        self.root = root
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.geometry("600x600")  # Set the size of the splash screen
        self.center_window(self.root)  # Center the window

        # Load the image
        try:
            self.image = Image.open(image_path)
            self.image = self.image.resize((400, 400), Image.Resampling.LANCZOS)  # Resize the image
            self.tk_image = ImageTk.PhotoImage(self.image)
        except FileNotFoundError:
            print(f"Error: The image file '{image_path}' was not found.")
            self.root.destroy()
            return

        # Create a label to display the image
        self.label = tk.Label(root, image=self.tk_image)
        self.label.pack()

        # Close the splash screen after the specified duration
        self.root.after(duration, self.close)

    def close(self):
        self.root.destroy()
        start_main()  # Start the main app **after** the splash screen closes

    def center_window(self, window):
        window.update_idletasks()
        width = 400  # Set explicit width
        height = 400  # Set explicit height
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

class TextMessageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Love Jar")
        self.root.geometry("400x400")  
        self.center_window(self.root)  

        # Load and display the GUI image
        try:
            self.image = Image.open(gui_image_path)
            self.image = self.image.resize((400, 400), Image.Resampling.LANCZOS)
            self.tk_image = ImageTk.PhotoImage(self.image)
        except FileNotFoundError:
            print(f"Error: The GUI image file '{gui_image_path}' was not found.")
            self.root.destroy()
            return

        self.label = tk.Label(root, image=self.tk_image)
        self.label.pack()

        # Button to display a random message
        self.button = Button(root, text="Grab a note from the Jar", command=self.show_message)
        self.button.pack(pady=10)

    def center_window(self, window):
        width = 500
        height = 600
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def show_message(self):
        # Ensure messages folder exists
        if not os.path.exists(messages_folder):
            print(f"Error: Messages folder '{messages_folder}' not found.")
            return

        # Get a list of message files
        message_files = [f for f in os.listdir(messages_folder) if f.endswith(".txt")]
        if not message_files:
            print("No notes found in the jar.")
            return

        # Select a random message file
        random_file = random.choice(message_files)
        message_path = os.path.join(messages_folder, random_file)

        # Read and display the message
        try:
            with open(message_path, "r", encoding="utf-8") as file:
                message = file.read().strip()
        except Exception as e:
            print(f"Error reading message file '{message_path}': {e}")
            return

        # Display message in a new window
        message_window = Toplevel(self.root)
        message_window.title("Your Note")
        Label(message_window, text=message, padx=20, pady=20).pack()

# Start the main app after splash screen closes
def start_main():
    app_root = tk.Tk()
    TextMessageApp(app_root)
    app_root.mainloop()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    splash = SplashScreen(root, splash_screen_path, duration=3000)
    root.mainloop()  # Run splash screen event loop