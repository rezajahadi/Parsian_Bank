# Parsian Bank ATM App

This is a Python application that simulates an ATM for Parsian Bank. 

## Overview

The app provides a graphical user interface for customers to enter their PIN and access bank services like getting a new debit card. It uses the Tkinter library for the UI and PyGame for sounds.

The main features are:

- PIN entry screen with on-screen keypad
- Virtual debit card request
- Parsian Bank branding and assets

## Usage

To start the app, run `python parsian_bank.py`. 

Enter your 4-digit PIN using the on-screen keypad. Click the "Get Debit Card" button to request a new virtual card.

The app will validate the PIN and show appropriate messages.

## Code Overview

- `parsian_bank.py` - Main app class and UI code 
- `assets/` - Folder containing images and audio assets
- `pins.txt` - Sample PIN numbers for demo

The code handles:

- Setting up the Tkinter window and widgets
- Loading assets like bank logo and card images 
- Input validation and PIN verification
- Playing audio cues
- Displaying debit card receipt

## Requirements

- Python 3
- Tkinter 
- PyGame

See `requirements.txt` for all package versions.

## Future Improvements

Some ideas for enhancing the app:

- Connect to a real banking API for live data
- Add more transaction options like deposits, transfers
- User accounts and login
- Animations and transitions

Let me know if you would like me to modify or expand this README.
