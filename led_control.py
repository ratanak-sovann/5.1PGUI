import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def led_control(led):
    # Turn all LEDs off
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    
    # Turn selected LED on
    if led == "GREEN":
        GPIO.output(2, GPIO.HIGH)
    elif led == "YELLOW":
        GPIO.output(3, GPIO.HIGH)
    elif led == "RED":
        GPIO.output(4, GPIO.HIGH)
        
def on_closing():
    # Turn off all LEDs
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    # Clean up GPIO
    GPIO.cleanup()
    # Destroy the window
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("LED Control Panel")

# Radio button control variable
led_choice = tk.StringVar()

# Radio buttons
ttk.Radiobutton(root, text="Green LED", variable=led_choice, value="GREEN", command=lambda: led_control("GREEN")).pack()
ttk.Radiobutton(root, text="Yellow LED", variable=led_choice, value="YELLOW", command=lambda: led_control("YELLOW")).pack()
ttk.Radiobutton(root, text="Red LED", variable=led_choice, value="RED", command=lambda: led_control("RED")).pack()

# Exit button
exit_button = ttk.Button(root, text="Exit", command=on_closing)
exit_button.pack()

# Ensure the on_closing function is called when the window is closed with the window manager
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
