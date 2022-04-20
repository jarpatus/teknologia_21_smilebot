import pigpio
import time

# Settings
m1_mode_pin1 = 16
m1_mode_pin2 = 17
m1_mode_pin3 = 20
m1_enable_pin = 12
m1_dir_pin = 13
m1_step_pin = 19
m2_mode_pin1 = 21
m2_mode_pin2 = 22
m2_mode_pin3 = 27
m2_enable_pin = 4
m2_dir_pin = 24
m2_step_pin = 18

# Connect to pigpio
pi = pigpio.pi()

# Setup GPIO pins
pi.set_mode(m1_mode_pin1, pigpio.OUTPUT)
pi.set_mode(m1_mode_pin2, pigpio.OUTPUT)
pi.set_mode(m1_mode_pin2, pigpio.OUTPUT)
pi.set_mode(m1_enable_pin, pigpio.OUTPUT)
pi.set_mode(m1_dir_pin, pigpio.OUTPUT)
pi.set_mode(m1_step_pin, pigpio.OUTPUT)
pi.set_mode(m2_mode_pin1, pigpio.OUTPUT)
pi.set_mode(m2_mode_pin2, pigpio.OUTPUT)
pi.set_mode(m2_mode_pin2, pigpio.OUTPUT)
pi.set_mode(m2_enable_pin, pigpio.OUTPUT)
pi.set_mode(m2_dir_pin, pigpio.OUTPUT)
pi.set_mode(m2_step_pin, pigpio.OUTPUT)

# Disable motors
pi.write(m1_enable_pin, 0)
pi.write(m2_enable_pin, 0)
