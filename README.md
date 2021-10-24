# Introduction
Software for Teknologia 21 Amazing Robots -competition robot "smilebot".

# Hardware
Raspberry PI 3/4

# Software
OS: Raspbian or equivalent

# Install
sudo apt-get update \
sudo apt-get -y install git python3 python3-venv \
sudo apt-get -y install pigpio \
sudo apt-get -y install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test libilmbase23 libharfbuzz-dev  \
#sudo apt-get -y install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test python3-numpy libblas-dev liblapack-dev \
git clone https://github.com/jarpatus/teknologia_21_smilebot.git \
cd teknologia_21_smilebot \
python3 -m venv env \
source env/bin/activate \
wget -P /tmp https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.0.0/tensorflow-2.0.0-cp37-none-linux_armv7l.whl \
pip3 install pigpio RPi.GPIO \
pip3 install opencv-contrib-python==4.1.0.25 keras /tmp/tensorflow-2.0.0-cp37-none-linux_armv7l.whl

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

