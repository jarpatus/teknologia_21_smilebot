# Introduction
Software for Teknologia 21 Amazing Robots -competition robot "smilebot".

# Hardware
Raspberry PI 3/4

# Software
OS: Raspbian or equivalent
Packages: git python3 python3-venv pigpio

# Install
sudo apt-get update \
sudo apt-get -y install git python3 python3-venv pigpio \
git clone https://github.com/jarpatus/teknologia_21_smilebot.git \
cd teknologia_21_smilebot \
python3 -m venv env \
source env/bin/activate \
pip install -r requirements.txt 

# Update 
TBD

# Push
pip freeze > requirements.txt \n
TODO


# Run
pigpiod -s 2
