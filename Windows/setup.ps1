# Setup for windows

python3 -m PyInstaller --onefile main.py
python3 -m PyInstaller --onefile choplifter.py
python3 -m PyInstaller --onefile choplifter_survival.py
python3 -m PyInstaller --onefile init/assets.py
python3 -m PyInstaller --onefile --add-data "assets\\bg1.png;." --add-data "assets\\bg2.png;." --add-data "assets\\bg3.png;." init/background.py
python3 -m PyInstaller --onefile init/chop.py
python3 -m PyInstaller --onefile init/tank.py
python3 -m PyInstaller --onefile init/jet.py
python3 -m PyInstaller --onefile init/alien.py
python3 -m PyInstaller --onefile init/init.py

Start-Process dist/main.exe