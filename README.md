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
git pull

# Execute
pigpiod -s 2

# Contribute
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git config --global credential.helper store
pip freeze > requirements.txt \n
git add --all
git commit
git push
TODO

