################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 10                                                       #
# Due: Apr 04                                                  #
#                                                              #
################################################################
import numpy as np                                             #
import matplotlib . pyplot as plt                              #
import scipy as sp                                             #
import scipy . signal as sig                                   #
import pandas as pd                                            #                                               #
import time                                                    #
import math                                                    #
import control as con                                          #
from scipy . fftpack import fft , fftshift                     #
################################################################
r = 1000
l = 0.027
c = 0.0000001
ricky = 1/(r*c)
licky = 1/(l*c)

def fun1(t):
    return np.cos(2*np.pi*100*t)+np.cos(2*np.pi*3024*t)+np.sin(2*np.pi*50000*t)
def mag(w):
    num = ricky*w
    den = np.sqrt(pow(w,4)+pow(w,2)*(pow(ricky,2)-2*licky)+pow(licky,2))
    return num/den
def phase(r,l,c,w):
    num = ricky*w
    den = -pow(w,2)+licky
    return np.pi/2 - np.arctan(num/den)


funky= np.arange(pow(10,3),pow(10,6),100)
print(funky)
magma = mag(funky)
phasor = phase(r,l,c,funky)


sys = sig.TransferFunction([ricky],[1,ricky,licky])
w2,mag2,phase2 = sig.bode(sys)

plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.plot(funky,magma,color="black")
plt.xlabel("t(s)")
plt.title('Magnitude(w)')
plt.grid()
plt.subplot(2,1,2)
plt.plot(funky,phasor,color="red")
plt.xlabel("t(s)")
plt.title('Phase(w)')
plt.grid()

plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.semilogx(w2,mag2,color="black")
plt.xlabel("t(s)")
plt.title('Magnitude(w)')
plt.grid()
plt.subplot(2,1,2)
plt.semilogx(w2,phase2,color="red")
plt.xlabel("t(s)")
plt.title('Phase(w)')
plt.grid()


timmy = np.arange(0,0.01,1e-6)
data1 = fun1(timmy)
plt.figure(figsize=(10,5))
plt.semilogx(timmy,data1,color="blue")
plt.xlabel("t(s)")
plt.title('x1(t)')
plt.grid()