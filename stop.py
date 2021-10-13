import pigpio
import RPi.GPIO as GPIO
import time

# Settings
dir_pin = 24
step_pin = 18
enable_pin = 4
mode_pins = (21, 22, 27)
steps = 10240
stepdelay = 0.00001




pi = pigpio.pi()




# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(mode_pins, GPIO.OUT)

# Stop
GPIO.output(enable_pin, 1)
#pi.write(enable_pin, 0)


pi.stop()

