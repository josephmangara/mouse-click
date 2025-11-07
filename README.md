# Mouse click tool
A simple Python tool that shows mouse clicks visually on the screen using colored circles.

## What it does
- Displays a circle for mouse clicks.  
- Circles fade automatically after 1 second.  
- The overlay is transparent and doesn’t block mouse actions.
- This tool can be used during screen recordings to show mouse activity and ease tracking for people viewing the recordings. 

## Requirements
- Python 3.7 or higher  
- PyQt5  
- pynput  
- tkinter

## Installation
1. Clone the repository:
```bash
    git clone https://github.com/josephmangara/mouse-click
    cd mouse-click
```
2. Install the required packages.
```bash
    pip install PyQt5 pynput
    pip install tkinter
    # For mac os  
    pip3 install pynput
    # or 
    python3 -m pip install pynput
    brew install python-tk
```
- Alternatively, you can create and activate a virtual environment:
```bash
    python -m venv venv
    source venv/bin/activate       # Linux/Mac
    venv\Scripts\activate          # Windows
    # Install dependencies 
    pip install PyQt5 pynput tkinter
```

## How to run 
- Run the script from the terminal:
```bash
    python3 showclick.py 
    or 
    python showclick.py
```
- You should see a colored circle when you click anywhere on the screen.
- You can end the session by clicking ctrl + C in Linux and cmd + C in macOS.

## Quick install
You can also install all dependencies at once:
```bash
    pip install -r requirements.txt
```

## Troubleshooting
- **macOS:** You may need to grant accessibility permissions under  
  *System Preferences → Security & Privacy → Accessibility.*

## License
This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
