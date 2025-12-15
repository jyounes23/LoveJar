# LoveJar

LoveJar is a Python-based graphical chatbot application that greets users with a splash screen and provides an interactive experience via a custom Tkinter GUI. It utilizes external image assets and a structured folder for messages to deliver a them to a loved one or a friend.

## Features

- **Splash Screen**: Displays a customizable splash screen with an image on startup.
- **Graphical Interface**: Presents a main window with themed visuals and user-friendly interaction buttons.
- **Image Handling**: Dynamically loads and resizes images for display in the GUI.
- **Packaged App Support**: Compatible with PyInstaller, dynamically adjusting paths for bundled apps.

## Installation

1. Ensure Python 3.8+ is installed.
2. Clone the repository:
```bash
git clone https://github.com/yourusername/LoveJar.git
cd LoveJar
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Ensure the following files and folders exist in the project root:
   - `logo.jpg` — splash screen image
   - `jar_image.jpeg` — main GUI image
   - `messages/` — directory for text/message files

## Usage

To run JayBot:
```bash
python3 jaybotv2.py
```

Upon launch:
- A splash screen will appear with your logo.
- After a short delay, the main GUI opens, displaying an image and interactive elements.

## File Structure

```
JayBot/
├── jaybotv2.py
├── logo.jpg
├── jar_image.jpeg
├── messages/
│   └── [message text files]
└── requirements.txt
```

## Packaging with PyInstaller

To package the app as an executable:
```bash
pyinstaller --onefile --add-data "logo.jpg:." --add-data "jar_image.jpeg:." --add-data "messages:messages" jaybotv2.py
```

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please contact younesj@moravian.edu

