# Setup for windows

python3 -m PyInstaller --onefile main.py
python3 -m PyInstaller --onefile --add-data "assets\\Fonts\\amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404\\comic.ttf;assets" --add-data "assets\\Songs\\Audiomachine - By the Hand of the Mortal.mp3;assets" --add-data "assets\menu_bg.;assets" --add-data "assets\\choplifter_txt.png;assets" --add-data "assets\\play_txt.png;assets" --add-data "assets\\quit_txt.png;assets" choplifter.py
python3 -m PyInstaller --onefile --add-data "assets\\Fonts\\amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404\\comic.ttf;assets" --add-data "assets\\Songs\\Audiomachine - By the Hand of the Mortal.mp3;assets" --add-data "assets\\menu_bg.;assets" --add-data "assets\\choplifter_txt.png;assets" --add-data "assets\\play_txt.png;assets" --add-data "assets\\quit_txt.png;assets" choplifter_survival.py
python3 -m PyInstaller --onefile init/assets.py
python3 -m PyInstaller --onefile --add-data "assets\\bg1.png;assets" --add-data "assets\\bg2.png;assets" --add-data "assets\\bg3.png;assets" init/background.py
python3 -m PyInstaller --onefile --add-data "assets\\helicopter.png;assets" --add-data "assets\\revert_helicopter.png;assets" --add-data "assets\\helico_ball.png;assets" --add-data "assets\\grounded_helicopter.png;assets" --add-data "assets\\green_pewpew.png;assets" --add-data "assets\\green_pewpew2.png;assets" --add-data "assets\\green_revert_pewpew.png;assets" init/chop.py
python3 -m PyInstaller --onefile --add-data "assets\\tank.png;assets" --add-data "assets\\revert_tank.png;assets" --add-data "assets\\shooting_tank.png;assets" --add-data"assets\\revert_shooting_tank.png;assets" --add-data "assets\\tank_pew.png;assets" --add-data "assets\\revert_tank_pew.png;assets" init/tank.py
python3 -m PyInstaller --onefile --add-data "assets\\jet.png;assets" --add-data "assets\\revert_jet.png;assets" --add-data "assets\\jet_pew.png;assets" --add-data "assets\\revert_jet_pew.png;assets" init/jet.py
python3 -m PyInstaller --onefile --add-data "assets\\saucer.png;assets" --add-data "assets\\laser.png;assets" init/alien.py
python3 -m PyInstaller --onefile --add-data "assets\\basement.png;assets" --add-data "assets\\hostage.png;assets" --add-data "assets\\revert_hostage.png;assets" init/init.py

Start-Process dist/main.exe