#Teleram Pract
sudo apt-get install python-pip
#1) Installing the venv module:-
sudo apt install python3-venv
#2) Creating a new virtual environment. Myenv is user-defined name
python3 -m venv myenv
#3) Activate the Virtual Environment
source myenv/bin/activate
#4) It should look like :- (myenv) pi@raspberrypi:- $
#5) Install telepot in virtual machine:-
pip install telepot
#6) pip install RPi.GPIO
#3) Edit the code to add your bot token
nano telegrambot.py
#4) After this the .py file will open. Paste the bot taken here
bot = telepot.Bot(&#39;your_bot_token&#39;)
#5) Run the Code
python telegrambot.py



#7-segemrnt pract
pip install RPi.GPIO --break-system-packages


#Oscilloscope
sudo raspi-config (enable i2c)
pip install board --break-system-packages
sudo pip install drawnow --break-system-packages
sudo apt-get install -y i2c-tools python3-smbus
python3 -m pip install --upgrade --no-cache-dir adafruit-blinka adafruit-circuitpython-busdevice
adafruit-circuitpython-ads1x15 --break-system-packages


# RFID 1
Command 1: sudo raspi-config (enable i2c)
Command 2: pip3 install adafruit-circuitpython-pn532 --break-system-packages

#RFID 2
Command:
Command 1: sudo raspi-config (enable i2c)
Command 2: sudo reboot
Command 3: pip3 install adafruit-circuitpython-pn532 --break-system-packages
Command 3: sudo apt install -y libnfc-bin libnfc-dev libusb-dev libpcsclite-dev i2c-tools
Command 4: sudo nano /etc/nfc/libnfc.conf
Edit the code: #Allow device auto-detection (default: true)
#Note: if this auto-detection is disabled, user has to set manually a device
#configuration using file or environment variable
allow_autoscan = false
#Allow intrusive auto-detection (default: false)
#Warning: intrusive auto-detection can seriously disturb other devices
#This option is not recommended, user should prefer to add manually his device.
#allow_intrusive_scan = false
#Set log level (default: error)
#Valid log levels are (in order of verbosity): 0 (none), 1 (error), 2 (info), 3 (debug)
#Note: if you compiled with --enable-debug option, the default log level is &quot;debug&quot;
#log_level = 1

#Manually set default device (no default)
#To set a default device, you must set both name and connstring for your device
#Note: if autoscan is enabled, default device will be the first device available in device list.
device.name = &quot;PN532 over I2C&quot;
device.connstring = &quot;pn532_i2c:/dev/i2c-1&quot;

Save the file.
Command 5: i2cdetect –y 1 (optional put sudo)
Command 6: nfc-list

import subprocess
import time

NAME = "Upasana"  # Put your name here

last_uid = None

try:
    while True:
        output = subprocess.getoutput("nfc-list")

        if "UID" in output:
            for line in output.splitlines():
                if "UID" in line:
                    uid = line.split(":")[1].strip().replace(" ", "")

                    if uid != last_uid:
                        print(f"{NAME}: {uid}")
                        last_uid = uid

                    break

        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped.")


#Fingerprint
pip3 install pyfingerprint
sudo python test.py

1: VCC Red Connect it to USB- TTL(5V) : VCC
2: GND Black Connect it to USB-TTL:GND

3: Tx Yellow Connect it to USB-TTL:Rx

4: Rx White Connect it to USB-TTL:Tx
