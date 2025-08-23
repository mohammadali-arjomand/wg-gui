#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
import subprocess

win = tk.Tk()
win.title("Wireguard Simple GUI")
win.minsize(300, 150)

# check running as root
def isRoot():
    output = subprocess.run(["whoami"], capture_output=True).stdout.decode()
    if "root" in output:
        return True
    return False

if not isRoot():
    messagebox.showerror("Permission denied", "You should be root to run this application.")
    exit()

configName = "fast"

def isConnected():
    output = subprocess.run(["wg", "show"], capture_output=True).stdout.decode()
    if len(output) > 0:     
        return True
    return False

connected = isConnected()
if not connected:
    btnText = "Connect"
else:
    btnText = "Disconnect"

def connection():
    global connected
    if connected:
        btn.config(text="Disconnecting...")
        win.update()
        subprocess.run(["wg-quick", "down", configName])
        btn.config(text="Connect")
        connected = False
    else: 
        btn.config(text="Connecting...")
        win.update()
        subprocess.run(["wg-quick", "up", configName])
        btn.config(text="Disconnect")
        connected = True

tk.Label(win, text="\nWireGuard Simple GUI!\n").pack()

btn = tk.Button(win, text=btnText, command=connection)
btn.pack()

win.mainloop()
