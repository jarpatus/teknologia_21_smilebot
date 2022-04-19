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
wheel_diameter = 75
wheel_radius = wheel_diameter/2
step_angle = 1.8
step_angle_rad = step_angle*0.01745329252
step_length = wheel_radius*step_angle_rad

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

# Initialize motors
pi.set_PWM_dutycycle(m1_step_pin, 128)
pi.set_PWM_dutycycle(m2_step_pin, 128)
pi.set_PWM_frequency(m1_step_pin, 0)
pi.set_PWM_frequency(m2_step_pin, 0)
pi.write(m1_mode_pin1, 0)
pi.write(m1_mode_pin2, 0)
pi.write(m1_mode_pin3, 0)
pi.write(m2_mode_pin1, 0)
pi.write(m2_mode_pin2, 0)
pi.write(m2_mode_pin3, 0)
pi.write(m1_enable_pin, 0)
pi.write(m2_enable_pin, 0)
pi.write(m1_dir_pin, 1)
pi.write(m2_dir_pin, 0)


# Start motors
def start():
	print("Start motors")
	pi.write(m1_enable_pin, 1)
	pi.write(m2_enable_pin, 1)


# Stop motors
def stop():
	print("Stop motors")
	pi.write(m1_enable_pin, 0)
	pi.write(m2_enable_pin, 0)


# Drive forwards
def fwd(mm, pps):
	steps = mm/step_length
	t = steps/pps*25
	print("Drive forward", mm, "mm @", pps, "pps,", steps, "steps,", t, "s")
	pi.set_PWM_frequency(m1_step_pin, pps)
	pi.set_PWM_frequency(m2_step_pin, pps)
	pi.write(m1_dir_pin, 1)
	pi.write(m2_dir_pin, 0)
	pi.write(m1_enable_pin, 1)
	pi.write(m2_enable_pin, 1)
	time.sleep(t)
	pi.write(m1_enable_pin, 0)
	pi.write(m2_enable_pin, 0)


# Drive backwards
def bwd(mm, pps):
	steps = mm/step_length
	t = steps/pps*25
	print("Drive backward", mm, "mm @", pps, "pps,", steps, "steps,", t, "s")
	pi.set_PWM_frequency(m1_step_pin, pps)
	pi.set_PWM_frequency(m2_step_pin, pps)
	pi.write(m1_dir_pin, 0)
	pi.write(m2_dir_pin, 1)
	pi.write(m1_enable_pin, 1)
	pi.write(m2_enable_pin, 1)
	time.sleep(t)
	pi.write(m1_enable_pin, 0)
	pi.write(m2_enable_pin, 0)

# Main
try:
	fwd(100, 1000)
	time.sleep(0.5)
	bwd(100, 1000)
	while True:
		time.sleep(0.5)
except Exception as e:
	print(e)
finally:
	stop()
	pi.stop()
