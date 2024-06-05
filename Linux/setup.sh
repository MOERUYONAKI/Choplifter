# Setup for GNU/Linux

#!/bin/bash

python3 -m PyInstaller --onefile --add-data "*.py:." --add-data "init/*.py:init" --add-data "assets/*.png:assets" --add-data "assets/*.jpg:assets" --add-data "assets/Songs/*.mp3:assets/Songs" --add-data "assets/Fonts/*.ttf:assets/Fonts" main.py

./dist/main.exe