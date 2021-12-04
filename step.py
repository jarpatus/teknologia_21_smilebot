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


# Drive

def ramp(pin, start_freq, stop_freq, ramp_time, step_time):
	pi.wave_clear()
	waves = []

	steps = int(ramp_time/step_time)
	step_freq = (stop_freq-start_freq)/steps
	for i in range(steps+1):
		f = int(start_freq+i*step_freq)
		print(f)
		wave = []
		wave.append(pigpio.pulse(1<<pin, 0, int(500000/f)))
		wave.append(pigpio.pulse(0, 1<<pin, int(500000/f)))
		pi.wave_add_generic(wave)
		waves.append(pi.wave_create())

#	for i in range(steps+1):
#		pi.wave_send_repeat(waves[i])
#		time.sleep(step_time)

	wavechain = []
#	for i in range(steps+1):
#		steps = 300
#		x = steps & 255
#		y = steps >> 8
#		wavechain += [255, 0, waves[i], 255, 1, x, y]

	wavechain = [
		255, 0, 
		waves[4],
		
	]

	#pi.wave_send_repeat(waves[4])
#	pi.wave_chain(wavechain)



#	pi.wave_send_repeat(waves[400])


def start():
	print("Start motors")
	pi.write(m1_enable_pin, 1)
	pi.write(m2_enable_pin, 1)


def stop():
	print("Stop motors")
	pi.write(m1_enable_pin, 0)
	pi.write(m2_enable_pin, 0)


def fwd(mm, pps):
	steps = mm/step_length
	t = steps/pps*25
	print("Drive forward", mm, "mm @", pps, "pps,", steps, "steps,", time, "s")
	pi.write(m1_dir_pin, 1)
	pi.write(m2_dir_pin, 0)
	pi.write(m1_enable_pin, 1)
	pi.write(m2_enable_pin, 1)
	ramp(m1_step_pin, 100, 500, 2, 0.2)




def xfwd(mm, pps):
	steps = mm/step_length
	t = steps/pps*25
	print("Drive forward", mm, "mm @", pps, "pps,", steps, "steps,", time, "s")
	pi.set_PWM_frequency(m1_step_pin, pps)
	pi.set_PWM_frequency(m2_step_pin, pps)
	pi.write(m1_dir_pin, 1)
	pi.write(m2_dir_pin, 0)
	pi.write(m1_enable_pin, 1)
	pi.write(m2_enable_pin, 1)
	time.sleep(t)
	pi.write(m1_enable_pin, 0)
	pi.write(m2_enable_pin, 0)


def bwd(mm, pps):
	steps = mm/step_length
	t = steps/pps*25
	print("Drive backward", mm, "mm @", pps, "pps,", steps, "steps,", time, "s")
	pi.set_PWM_frequency(m1_step_pin, pps)
	pi.set_PWM_frequency(m2_step_pin, pps)
	pi.write(m1_dir_pin, 0)
	pi.write(m2_dir_pin, 1)
	pi.write(m1_enable_pin, 1)
	pi.write(m2_enable_pin, 1)
	time.sleep(t)
	pi.write(m1_enable_pin, 0)
	pi.write(m2_enable_pin, 0)

try:
	fwd(200, 1000)
	time.sleep(3)
	#bwd(200, 1000)
	stop()
	#while True:
	#	time.sleep(0.5)
except Exception as e:
	print(e)
finally:
	stop()
	pi.stop()
