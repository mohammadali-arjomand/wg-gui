#!/bin/bash
cp ./wg-gui.py /usr/local/bin/wg-gui
cp ./run-wg-gui.sh /usr/local/bin/run-wg-gui
mkdir /.wg-gui
cp ./icon.png /.wg-gui/icon.png
cp ./wg-gui.desktop /usr/share/applications/wg-gui.desktop
echo "Done"
