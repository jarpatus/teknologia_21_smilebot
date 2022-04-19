import RPi.GPIO as GPIO
import time

# Settings
dir_pin = 24
step_pin = 18
enable_pin = 4
mode_pins = (21, 22, 27)
steps = 10240
stepdelay = 0.00001

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(mode_pins, GPIO.OUT)

# Start
GPIO.output(enable_pin, 1)

# Turn
for i in range(steps):
	GPIO.output(step_pin, True)
	time.sleep(stepdelay)
	GPIO.output(step_pin, False)
	time.sleep(stepdelay)

# Stop
#GPIO.output(enable_pin, 0)
