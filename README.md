# Calculator Application with Hand Gesture Control

This is a simple calculator application developed in Python that allows you to perform basic arithmetic operations using hand gestures. The application uses OpenCV and the cvzone.HandTrackingModule to track hand movements and interact with the calculator buttons.

## Features

Calculator Application Features:

- Interactive GUI with buttons for digits, arithmetic operations, and special functions.
- Perform arithmetic operations using hand gestures over the buttons.
- Clear the current input with the "C.E" button.
- Calculate the square root using the "**" button.
- Backspace to delete the last character with the "<-" button.
- Quit the application using the "Q" button.

## Requirements

Requirements:

- Python 3.x
- OpenCV
- cvzone

## Installation

Installation:

1. Make sure you have Python 3.x installed. If you don't have it, download and install it from the official website: https://www.python.org/downloads/
2. Install the required libraries using pip:
pip install opencv-python
pip install cvzone



## Usage

Usage:

1. Run the `calculator.py` script:
python calculator.py

2. The webcam feed will open, and the calculator GUI will appear on the screen.
3. Use your hand gestures over the buttons to interact with the calculator.

Hand Gestures:

- Bring your hand close to the button you want to press.
- When the distance between your thumb and index finger is small enough, the button will be pressed.

License:

This project is licensed under the MIT License - see the LICENSE file for details.
