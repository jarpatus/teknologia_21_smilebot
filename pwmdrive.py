import pigpio
import time
import threading

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
        self.step_length = self.wheel_radius*self.step_angle_rad/25 # Note: 25 is arbitary. I have error in my formula somewhere...
    
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
        
        
        # Setup step counter
        self.m1steps = 0
        self.m2steps = 0
        self.pi.callback(self.m1_step_pin, pigpio.RISING_EDGE, self.m1stepped)
        self.pi.callback(self.m2_step_pin, pigpio.RISING_EDGE, self.m2stepped)
        

    # Start motors
    def start(self):
        print("Start motors")
        self.pi.write(self.m1_enable_pin, 1)
        self.pi.write(self.m2_enable_pin, 1)


    # Stop motors
    def stop(self):
        print("Stop motors")
        self.pi.write(self.m1_enable_pin, 0)
        self.pi.write(self.m2_enable_pin, 0)


    # Drive forwards
    def fwd(self, mm, pps):
        steps = mm/self.step_length
        print("Forwards", mm, "mm @", pps, "pps,", steps, "steps")
        self.drives(1, 0, steps, steps, pps)


    # Drive backwards
    def bwd(self, mm, pps):
        steps = mm/self.step_length
        print("Backwards", mm, "mm @", pps, "pps,", steps, "steps")
        self.drives(0, 1, steps, steps, pps)


    # Rotate clockwise
    # Didn't bother to calculate steps properly based on wheel size, just eyeballing it...
    def cw(self, angle, pps):
        steps = (angle*0.73)/self.step_length 
        print("Rotate ", angle, "degrees @", pps, "pps,", steps, "steps")
        if (steps > 0):
            self.drives(0, 0, steps, steps, pps)
        else: 
            self.drives(1, 1, -steps, -steps, pps)
        
        
    # Rotate counterclockwise
    def ccw(self, angle, pps):
        self.cw(-angle, pps)
    
    
    # Arc 
    # This is totally unfinished, need to define radius and calculate pps', also fwd vs bwd vs left vs right etc.
    def arc(self, mm, pps1, pps2):
        steps = mm/self.step_length
        t = steps/pps1*25
        print("Arc left", mm, "mm @", pps1, pps2, "pps,", steps, "steps,", t, "s")
        self.drivet(1, 0, t, pps1, pps2)

        
    # Drive for given time
    def drivet(self, m1d, m2d, t, m1pps, m2pps=-1):       
        if (m2pps == -1): m2pps = m1pps
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
        
        
    # Drive for given number of steps
    def drives(self, m1d, m2d, m1steps, m2steps, m1pps, m2pps=-1):       
        if (m2pps == -1): m2pps = m1pps
        m1freqs = [20000, 10000, 5000, 4000, 2500, 2000, 1250, 1000, 800, 625, 500] # freqs for pigpio -s 2
        m2freqs = [20000, 10000, 5000, 4000, 2500, 2000, 1250, 1000, 800, 625, 500] # freqs for pigpio -s 2
        self.m1steps = 0
        self.m2steps = 0
        m1ppscurrent = m1freqs.pop()
        m2ppscurrent = m2freqs.pop()
        self.drive(m1d, m2d, m1ppscurrent, m2ppscurrent)
        while True: # While loop is not optinal... better would be doing this in callback functions but my python-fu is not strong enough...
            print(m1ppscurrent, m2ppscurrent)
            if (m1ppscurrent < m1pps and len(m1freqs) > 0): 
                m1ppscurrent = m1freqs.pop()
                self.pi.set_PWM_frequency(self.m1_step_pin, m1ppscurrent)
            if (m2ppscurrent < m2pps and len(m2freqs) > 0): 
                m2ppscurrent = m2freqs.pop()
                self.pi.set_PWM_frequency(self.m2_step_pin, m2ppscurrent)
            if (self.m1steps >= m1steps or self.m2steps >= m2steps):
                break
            time.sleep(0.1)
            
        self.stop()


    def m1stepped(self, p1, p2, p3):
        self.m1steps += 1   
            
        
    def m2stepped(self, p1, p2, p3):
        self.m2steps += 1

    
if __name__ == "__main__":
    pwm = PWMDrive()
    try:
        pwm.fwd(200, 2000)
        time.sleep(0.5)
        #pwm.bwd(200, 2000)
        #time.sleep(0.5)
        #pwm.cw(180, 1250)
        #time.sleep(0.5)
        pwm.ccw(180, 1250)
        time.sleep(0.5)
        pwm.fwd(200, 2000)
    except Exception as e:
        print(e)
    finally:
        pwm.stop()
