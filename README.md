# WireGuard GUI
There is a simple WireGuard GUI to manage wireguard configs in linux as client

![ScreenShot](screenshot.png)
> Running WireGuard GUI in XFCE Desktop!

> **Important** WireGuard GUI doesn't work on Windows. If you're a Windows user, [install official WireGuard Client](https://www.wireguard.com/install/)

# Requirements
Install `wireguard`, `git` and `tkinter`  on your system
```bash
# Debian/Ubuntu
sudo apt install wireguard git python3-tk

# Fedora
sudo dnf install wireguard-tools git-all python3-tkinter

# Arch
sudo pacman -S wireguard-tools git python-tk
```
[To install wireguard on other distros, click here](https://www.wireguard.com/install/)

# Installation
Clone project in your system. Then run `install.sh` script as root:
```bash
git clone https://github.com/mohammadali-arjomand/wg-gui.git
sudo ./wg-gui/install.sh
```

Now you can run WireGuard GUI using `run-wg-gui`:
```bash
run-wg-gui
```

# Usage
Import a config using `Add Config` button and choose it. Then click on `Connect` button and enjoy! (See screenshot above)

# License
MIT License, Copyright (c) 2025 MohammadAli Arjomand [(more details)](https://github.com/mohammadali-arjomand/wg-gui/blob/main/LICENSE)
