# led pract  6 9 14 20 --gnd
# finger .py #vcc -red, gnd-black, tx- yellow,rx-white
# home controller #GND - 6, VCC - 2, IN1 - 26, IN2 - 24, IN3 - 21
# 7 segment #gnd -14, vcc - 4, D10 - 18, clk-16
#oscilloscope #vdd - pin 1 #gnd - pin 2 #sda - pin 3 #scl - pin 5
# RFID #6 -gnd  #2-vcc, 3 sda, 4- scl
#cannel 1-on, channel 2 -off
# Windows
Steps:
Step 1: Download the latest pre-release version of WoR tool
https://www.worproject.ml/downloads and extract the files.

Step 2: Prepare Windows 10 ARM64 ISO
1. Go to UUPDump.net.
2. Choose Windows 10 ARM64 build (choose latest stable).
3. Download the script (zip file) and run it on your Windows PC.
o It downloads required files directly from Microsoft and builds an ISO.
4. At the end, you’ll have a Windows 10 ARM64 ISO file.

Step 3: Install WoR and Prepare the SD/SSD
1. Insert your SD card or SSD into your Windows PC.
2. Open WoR.exe (run as Administrator).
3. Follow the wizard:

o Step 1: Select your device (SD/SSD).

o Step 2: Point to your Windows 10 ARM64 ISO.

o Step 3: Select your device type: Raspberry Pi 4.
o Step 4: Provide the UEFI firmware and drivers.

o Step 5: Confirm installation settings.

4. WoR will now flash the Windows image to your device.
o This can take 30–60 minutes depending on storage speed.

Step 4: Booting Raspberry Pi 4
1. Insert the prepared storage into your Raspberry Pi 4.
2. Power it on → it will first load into the UEFI firmware screen.
3. (Optional but recommended):
o Go into UEFI settings.
o Change Boot Order to make your SD/SSD the first boot option.

o Save and reboot.
4. Now, Windows 10 setup begins.
o Select language, region, keyboard layout.
o Create or skip Microsoft account.
o Configure system preferences.
5. For network access, use a USB to Ethernet or a compatible WiFi dongle.
6. Install Microsoft Edge by double

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

If this is on your Raspberry Pi fingerprint-sensor practical, the error can come from either the pyfingerprint installation or from the sensor/serial connection.

Please run these commands one at a time and send me the exact output if one gives an error:

pip3 install pyfingerprint --break-system-packages

Then check whether it installed:

pip3 show pyfingerprint

Then run:

sudo python3 test.py
Important

You wrote:

sudo python test.py

On newer Raspberry Pi OS versions, use:

sudo python3 test.py

3: Tx Yellow Connect it to USB-TTL:Rx

4: Rx White Connect it to USB-TTL:Tx
