# Introduction
Software for Teknologia 21 Amazing Robots -competition robot "smilebot".

# Hardware
Raspberry PI 3/4

# Software
OS: Raspbian or equivalent (developed using Raspbian 10.9)

For rgbmatrix enable I2C using raspi.config . Disable SPI and 1-Wire if enabled as they may interfere with GPIOs used by motor shield. 

# Install
sudo apt-get update \
sudo apt-get -y install git python3 python3-venv \
sudo apt-get -y install pigpio \
sudo apt-get -y install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test libblas-dev liblapack-dev gfortran \
sudo apt-get -y install libharfbuzz-dev libilmbase23 libopenexr23 libavcodec58 libavformat58 libswscale5

git clone https://github.com/jarpatus/teknologia_21_smilebot.git

cd teknologia_21_smilebot \
python3 -m venv env \
source env/bin/activate

wget -P /tmp https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.0.0/tensorflow-2.0.0-cp37-none-linux_armv7l.whl \
pip3 install pigpio RPi.GPIO \
pip3 install numpy==1.21.4 opencv-contrib-python==4.1.0.25 h5py==2.10.0 keras /tmp/tensorflow-2.0.0-cp37-none-linux_armv7l.whl scipy \
pip3 install smbus pillow

sudo sh -c "cat rgbboot.service > /etc/systemd/system/rgbboot.service" \
sudo sudo systemctl enable rgbboot

# Update 
git pull

# Execute
pigpiod -s 2

# Contribute
git config --global user.email "you@example.com" \
git config --global user.name "Your Name" \
git config --global credential.helper store \
pip freeze > requirements.txt \
git add --all \
git commit \
git push
