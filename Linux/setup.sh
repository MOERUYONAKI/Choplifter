# Setup for GNU/Linux

#!/bin/bash

python3 -m PyInstaller --onefile --add-data "*.py:." --add-data "init/*.py:init" --add-data "assets/*.png:assets" --add-data "assets/*.jpg:assets" --add-data "assets/Songs/*.mp3:assets/Songs" --add-data "assets/Fonts/amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404/*.ttf:assets/Fonts/amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404" main.py

./dist/main.exe