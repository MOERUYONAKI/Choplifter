# Setup for windows

python3 -m PyInstaller --onefile main.py
python3 -m PyInstaller --onefile --add-data "assets\\Fonts\\amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404\\comic.ttf" --add-data "assets\\Songs\\Audiomachine - By the Hand of the Mortal.mp3" --add-data "assets\menu_bg.jpg" --add-data "assets\\choplifter_txt.png" --add-data "assets\\play_txt.png" --add-data "assets\\quit_txt.png" choplifter.py
python3 -m PyInstaller --onefile choplifter_survival.py
python3 -m PyInstaller --onefile init/assets.py
python3 -m PyInstaller --onefile --add-data "assets\\bg1.png;." --add-data "assets\\bg2.png;." --add-data "assets\\bg3.png;." init/background.py
python3 -m PyInstaller --onefile --add-data "assets\\helicopter.png" --add-data "assets\\revert_helicopter.png" --add-data "assets\\helico_ball.png" --add-data "assets\\grounded_helicopter.png" --add-data "assets\\green_pewpew.png" --add-data "assets\\green_pewpew2.png" --add-data "assets\\green_revert_pewpew.png" init/chop.py
python3 -m PyInstaller --onefile --add-data "assets\\tank.png" --add-data "assets\\revert_tank.png" --add-data "assets\\shooting_tank.png" --add-data"assets\\revert_shooting_tank.png" --add-data "assets\\tank_pew.png" --add-data "assets\\revert_tank_pew.png" init/tank.py
python3 -m PyInstaller --onefile --add-data "assets\\jet.png" --add-data "assets\\revert_jet.png" --add-data "assets\\jet_pew.png" --add-data "assets\\revert_jet_pew.png" init/jet.py
python3 -m PyInstaller --onefile --add-data "assets\\saucer.png" --add-data "assets\\laser.png" init/alien.py
python3 -m PyInstaller --onefile --add-data "assets\\basement.png" --add-data "assets\\hostage.png" --add-data "assets\\revert_hostage.png" init/init.py

Start-Process dist/main.exe