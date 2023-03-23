################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 04                                                       #
# Due: Feb 14                                                  #
#                                                              #
################################################################
import numpy as np                                             #
import matplotlib . pyplot as plt                              #
import scipy as sp                                             #
import scipy . signal as sig                                   #
import pandas as pd                                            #
import control                                                 #
import time                                                    #
import math                                                    #
from scipy . fftpack import fft , fftshift                     #
################################################################
R = 1000
C = 100*pow(10,-9)
L = 27*pow(10,-3)
def u(start,intake):
    if intake >= start:
        output= 1
    else:
        output = 0
    return output
def ten(power):
    return pow(10,power)
def r(start,intake):
    if intake >= start:
        output= intake-start
    else:
        output = 0
    return output
def populate(F1,f1):
    F1 = np.zeros(bound)
    for i in range(bound):
        j=i*step
        F1[i] = f1(j+low)
    return F1
def timed(t):
    return ((g/omega)*np.exp(alpha*t)*np.sin(omega*t+angle))*(u(0,t))
    
step = 1e-6
low = 0
up = 1.2*ten(-3)
dif = up-low
t = np.arange(low,up,step)
size = dif*2
bound = round(dif/step)

thing = 1/(R*C)
alpha = -thing*0.5
omega = math.sqrt((4/(L*C))-pow(thing,2))/2
angle = math.atan(omega/alpha)
g = math.sqrt(pow(thing*alpha,2)+pow(thing*omega,2))

timmy = {0}
timmy = populate(timmy, timed)

num = [thing,0]
den = [1, thing, 1/(L*C)]

tout , yout = sig.impulse ((num , den), T = t)

plt.figure(figsize=(dif*10000,up*10000))
plt.subplot(2,1,1)
plt.plot(t,-timmy)
plt.title('User Defined')
plt.subplot(2,1,2)
plt.plot(t,yout)
plt.title('Library Built')


