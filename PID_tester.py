from matplotlib import pyplot as plt
import numpy as np
import time
from PID import PID

def log_sweep(t,startHz,endHz,total_time):
    f = startHz + (endHz-startHz)*(np.exp(t)-1)/(np.exp(total_time)-1)
    #start: 0
    #end: ln(total_time+1)
    return np.sin(t*2*np.pi * f), f

def error(t): #seconds
    l,f = log_sweep(t,5,100,10)
    print(f)
    return l
    freq1 = 4 #hz
    freq2 = 15
    return np.sin(t*2*np.pi * freq1) + np.sin(t*2*np.pi * freq2 + 0.5)

def main():
    x = []
    outs = []
    errs = []
    ins = []
    start_time = time.time_ns()
    run_time = 10#seconds
    pid = PID(0.7, 0.7, 0)
    pid.start()
    last_out = 0
    gains = []
    phases = []
    while time.time_ns() < start_time + run_time*10**(9):
        t = (time.time_ns() - start_time)*10**(-9)
        err = -(error(t) - last_out)
        pid.step(err)
        last_out = pid.out
        x.append(t)
        errs.append(err)
        ins.append(error(t))
        outs.append(last_out)
    plt.figure(figsize=(10,5))
    # plt.plot(x,outs)
    # plt.plot(x,ins)
    # plt.plot(x,errs)
    plt.plot(x,)
    plt.show()


if __name__ == "__main__":
    main()