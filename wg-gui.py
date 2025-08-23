#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import subprocess

win = tk.Tk()
win.title("Wireguard Simple GUI")
win.minsize(300, 180)

# check running as root
def isRoot():
    output = subprocess.run(["whoami"], capture_output=True).stdout.decode()
    if "root" in output:
        return True
    return False

if not isRoot():
    messagebox.showerror("Permission denied", "You should be root to run this application.")
    exit()

def isConnected():
    output = subprocess.run(["wg", "show"], capture_output=True).stdout.decode()
    if len(output) > 0:     
        firstLine = output.split("\n")[0]
        activeConfig = firstLine.split(" ")[1]
        return True, activeConfig
    return False, ""

connected, activeConfig = isConnected() # TODO: Complete here
if not connected:
    btnText = "Connect"
else:
    btnText = "Disconnect"

def connection():
    global connected
    configName = configsCombo.get()

    if not checkConfigExists(configName):
        messagebox.showerror("Config Error", "Chosen config does not exist")
        return

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

def checkConfigExists(configName):
    return len(subprocess.run(["ls", f"/etc/wireguard/{configName}.conf"], capture_output=True).stdout.decode()) > 0

def listOfConfigs():
    configs = subprocess.run(["ls", "/etc/wireguard/"], capture_output=True).stdout.decode().split("\n")
    for i in range(len(configs)):
        configs[i] = configs[i].split(".")[0]
    configs.remove("")
    return configs

def newConfig():
    configPath = filedialog.askopenfilename(
        initialdir="/home",
        title="Choose config file",
        filetypes=(("Config files", "*.conf"), ("All files", "*"))
    )
    if configPath:
        subprocess.run(["cp", configPath, "/etc/wireguard/"])
        configsCombo.config(values=listOfConfigs())
        configsCombo.set(configPath.split("/")[-1].split(".")[0])

# GUI:

tk.Label(win, text="\nWireGuard Simple GUI!\n").pack()

configFrm = tk.Frame(win)
configFrm.pack()

configs = listOfConfigs()
configsCombo = ttk.Combobox(configFrm, values=configs)
configsCombo.set(configs[0])
configsCombo.grid(row=0, column=0)

newConfigBtn = tk.Button(configFrm, text="New Config", command=newConfig)
newConfigBtn.grid(row=0, column=1)

tk.Label(win, text="").pack()

btn = tk.Button(win, text=btnText, command=connection)
btn.pack()

win.mainloop()
