import pigpio
import time

class PWMDrive():

    # Constructor
    def __init__(self):
    
        # Settings
        self.m1_mode_pin1 = 16
        self.m1_mode_pin2 = 17
        self.m1_mode_pin3 = 20
        self.m1_enable_pin = 12
        self.m1_dir_pin = 13
        self.m1_step_pin = 19
        self.m2_mode_pin1 = 21
        self.m2_mode_pin2 = 22
        self.m2_mode_pin3 = 27
        self.m2_enable_pin = 4
        self.m2_dir_pin = 24
        self.m2_step_pin = 18
        self.wheel_diameter = 75
        self.wheel_radius = self.wheel_diameter/2
        self.step_angle = 1.8
        self.step_angle_rad = self.step_angle*0.01745329252
        self.step_length = self.wheel_radius*self.step_angle_rad
    
        # Connect to pigpio
        self.pi = pigpio.pi()

        # Setup GPIO pins
        self.pi.set_mode(self.m1_mode_pin1, pigpio.OUTPUT)
        self.pi.set_mode(self.m1_mode_pin2, pigpio.OUTPUT)
        self.pi.set_mode(self.m1_mode_pin2, pigpio.OUTPUT)
        self.pi.set_mode(self.m1_enable_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.m1_dir_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.m1_step_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.m2_mode_pin1, pigpio.OUTPUT)
        self.pi.set_mode(self.m2_mode_pin2, pigpio.OUTPUT)
        self.pi.set_mode(self.m2_mode_pin2, pigpio.OUTPUT)
        self.pi.set_mode(self.m2_enable_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.m2_dir_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.m2_step_pin, pigpio.OUTPUT)

        # Initialize motors
        self.pi.set_PWM_dutycycle(self.m1_step_pin, 128)
        self.pi.set_PWM_dutycycle(self.m2_step_pin, 128)
        self.pi.set_PWM_frequency(self.m1_step_pin, 0)
        self.pi.set_PWM_frequency(self.m2_step_pin, 0)
        self.pi.write(self.m1_mode_pin1, 0)
        self.pi.write(self.m1_mode_pin2, 0)
        self.pi.write(self.m1_mode_pin3, 0)
        self.pi.write(self.m2_mode_pin1, 0)
        self.pi.write(self.m2_mode_pin2, 0)
        self.pi.write(self.m2_mode_pin3, 0)
        self.pi.write(self.m1_enable_pin, 0)
        self.pi.write(self.m2_enable_pin, 0)
        self.pi.write(self.m1_dir_pin, 1)
        self.pi.write(self.m2_dir_pin, 0)

    # Start motors
    def start(self):
        #print("Start motors")
        self.pi.write(self.m1_enable_pin, 1)
        self.pi.write(self.m2_enable_pin, 1)


    # Stop motors
    def stop(self):
        #print("Stop motors")
        self.pi.write(self.m1_enable_pin, 0)
        self.pi.write(self.m2_enable_pin, 0)


    # Drive forwards
    def fwd(self, mm, pps):
        steps = mm/self.step_length
        t = steps/pps*25
        print("Forwards", mm, "mm @", pps, "pps,", steps, "steps,", t, "s")
        self.drivet(1, 0, t, pps)


    # Drive backwards
    def bwd(self, mm, pps):
        steps = mm/self.step_length
        t = steps/pps*25
        print("Backwards", mm, "mm @", pps, "pps,", steps, "steps,", t, "s")
        self.drivet(0, 1, t, pps)


    # Rotate clockwise
    # Didn't bother to calculate steps properly based on wheel size, just eyeballing it...
    def cw(self, angle, pps):
        steps = (angle*0.7)/self.step_length 
        t = steps/pps*25
        print("Rotate ", angle, "degrees @", pps, "pps,", steps, "steps,", t, "s")
        if (t > 0):
            self.drivet(0, 0, t, pps)
        else: 
            self.drivet(1, 1, -t, pps)
        
        
    # Rotate counterclockwise
    def ccw(self, angle, pps):
        self.cw(-angle, pps)
    
    
    # Arc 
    # This is totally unfinished, need to define radius and calculate pps', also fwd vs bwd vs left vs right etc.
    def arc(self, mm, pps):
        steps = mm/self.step_length
        t = steps/pps*25
        print("Arc left", mm, "mm @", pps, "pps,", steps, "steps,", t, "s")
        self.drivet(1, 0, t, pps, round(0.5*pps))

        
    # Drive for given time
    def drivet(self, m1d, m2d, t, m1pps, m2pps=-1):
        self.drive(m1d, m2d, m1pps, m2pps)
        time.sleep(t)
        self.stop()


    # Drive until stopped
    def drive(self, m1d, m2d, m1pps, m2pps=-1):
        if (m2pps == -1): m2pps = m1pps
        self.pi.set_PWM_frequency(self.m1_step_pin, m1pps)
        self.pi.set_PWM_frequency(self.m2_step_pin, m2pps)
        self.pi.write(self.m1_dir_pin, m1d)
        self.pi.write(self.m2_dir_pin, m2d)
        self.pi.write(self.m1_enable_pin, 1)
        self.pi.write(self.m2_enable_pin, 1)
        
    
if __name__ == "__main__":
    pwm = PWMDrive()
    try:
        pwm.fwd(50, 1000)
        time.sleep(0.5)
        pwm.bwd(50, 1000)
        time.sleep(0.5)
        pwm.cw(45, 500)
        time.sleep(0.5)
        pwm.ccw(45, 500)
    except Exception as e:
        print(e)
    finally:
        pwm.stop()
