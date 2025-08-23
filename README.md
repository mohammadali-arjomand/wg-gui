# WireGuard GUI
A simple GUI for managing WireGuard configs on Linux (client-side)

![WireGuard GUI ScreenShot](screenshot.png)

> **Important** WireGuard GUI does not work on Windows.
> Windows users should use the [official WireGuard Client](https://www.wireguard.com/install/)

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

> Make sure you have Python3 with Tkinter support installed

[More installation instructions for WireGuard on other distros](https://www.wireguard.com/install/)

# Installation
Clone project in your system. Then run `install.sh` script as root:
```bash
git clone https://github.com/mohammadali-arjomand/wg-gui.git
cd wg-gui
sudo ./install.sh
```

Now you can run WireGuard GUI using:
```bash
run-wg-gui
```

# Usage
1. Import a config using **Add Config** button.
2. Select it from the list.
3. Click **Connect** and enjoy!

(See screenshot above)

<!-- TODO: Add a GIF of usage -->

# Todo
- Improving Multi-config management and connections

# Contribute
Interested in this project? [create an issue](http://github.com/mohammadali-arjomand/wg-gui/issues/new/) and share your thoughts!

# License
Licensed under [MIT License](https://github.com/mohammadali-arjomand/wg-gui/blob/main/LICENSE)
Copyright (c) 2025 MohammadAli Arjomand
