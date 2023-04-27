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
import pandas as pd                                            #                                               
import time                                                    #
import math                                                    #
import control as con                                          #
from scipy . fftpack import fft , fftshift                     #
################################################################

step = 1
low = 1e3
high = 1e6

w = np.arange(low, high, step)

R=1e3
L=27e-3
C=100e-9

magma = 10*np.log((w/(R*C)) / np.sqrt( (w/(R*C))**2 + (1/(L*C)-w**2)**2))
angel = ((np.pi/2) - np.arctan( (w/(R*C)) / (-1*(w**2) + (1/(L*C))) )) * (180/np.pi)

plt.figure(figsize=(20,10))
plt.subplot(2,1,1) #Top Figure
plt.grid()
plt.semilogx(w, magma)
plt.title("Hand caclulated")
plt.subplot(2,1,2)
plt.grid()
plt.semilogx(w, angel)
plt.show()

num = [1/(R*C),0]
den = [1,1/(R*C),1/(L*C)]
sys = sig.TransferFunction(num,den)
ang,mag,phase = sig.bode(sys,w)

plt.figure(figsize=(20,10))
plt.subplot(2,1,1) 
plt.grid()
plt.semilogx(ang, mag)
plt.subplot(2,1,2)
plt.grid()
plt.semilogx(ang, phase)

sys = con.TransferFunction(num,den)
_ = con.bode(sys, w, dB=True, Hz=True, deg=True, Plot=True)

tea = 1e-7
t = np.arange(0, 0.01+tea, tea)
x = (np.cos(2*np.pi*100*t)+ np.cos(2*np.pi*3024*t) + np.sin(2*np.pi* 50000*t))

numZ, denZ = sig.bilinear(num, den, 1/tea)
xFiltered = sig.lfilter(numZ, denZ, x)

plt.figure(figsize=(20,7))
plt.subplot(2,1,1)
plt.grid()
plt.plot(t,x, color = 'purple')
plt.title("Sample Signal")
plt.subplot(2,1,2)
plt.plot(t,xFiltered, color = 'red')
plt.title("Post Filtered Signal")
plt.grid()