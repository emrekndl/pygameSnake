## pygameSnake
# Simple Snake Game with Pygame

![Screenshot](https://github.com/emrekndl/pygameSnake/blob/master/screenShot1.png)
## -
![Screenshot](https://github.com/emrekndl/pygameSnake/blob/master/screenShot2.png)

## Installing:
Clone the repository:
```sh
$ git clone https://github.com/emrekndl/pygameSnake.git
```
Cd in to the directory:
```sh
$ cd pygameSnake
```
Install dependencies:
```sh
pip3 install -r requirements.txt
```
pip3 not installed:
- For Debian-Based GNU/Linux Distros:
```sh
sudo apt install python3-pip 
```
- For Arch GNU/Linux Distro:
```sh
sudo pacman -S python3-pip
```
##  Converting to executable game file
```sh
pip install pyinstaller
```
```sh
pyinstaller --onefile --windowed  snakePygame.py
```
or icon file adding(app.ico: icon file name):
```sh
pyinstaller --onefile --windowed --icon=app.ico snakePygame.py
```
