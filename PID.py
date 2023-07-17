import time

class PID:
    def __init__(self, p_term = 0.333, i_term = 0.333, d_term = 0.333):
        self.p_term = p_term
        self.i_term = i_term
        self.d_term = d_term
        self.running = False
        self.reset()

    def start(self):
        self.running = True
        self.last_time = time.time_ns() - self.time_before_pause
    
    def step(self, error):
        delta_t = (time.time_ns() - self.last_time) * 10**(-9) #seconds
        self.p = error * self.p_term
        self.i += error * self.i_term * delta_t
        self.d = error * self.d_term / delta_t
        self.out = -1 * (self.p + self.i + self.d)
        self.last_time = time.time_ns()

    def pause(self):
        self.running = False
        self.time_before_pause = time.time_ns() - self.last_time


    def reset(self):
        self.p = 0
        self.i = 0
        self.d = 0
        self.time_before_pause = 0
        self.out = 0
        self.last_time = 0

