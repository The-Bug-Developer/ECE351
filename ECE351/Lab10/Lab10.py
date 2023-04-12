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
r=1e3
l=27e-3
c=100e-9
ricky = 1/(r*c)
licky = 1/(l*c)
w= np.arange(pow(10,3),pow(10,6),100)

def autorange(bound,step):
    array = np.arange(-bound,bound+1,step*2*bound)
    return array



def fun1(t):
    return np.cos(2*np.pi*100*t)+np.cos(2*np.pi*3024*t)+np.sin(2*np.pi*50000*t)

magma = 10*np.log((w*licky) / np.sqrt( (w*licky)**2 + (licky-w**2)**2))
angel = ((np.pi/2) - np.arctan( (w*licky) / (-1*(w**2) + (licky)) )) * (180/np.pi)



sys = sig.TransferFunction([ricky],[1,ricky,licky])
w2,mag2,phase2 = sig.bode(sys)

plt.figure(figsize=(20,10))
plt.subplot(2,1,1)
plt.semilogx(w,magma,color="black")
plt.xlabel("t(s)")
plt.title('Magnitude(w)')
plt.grid()
plt.subplot(2,1,2)
plt.semilogx(w,angel,color="red")
plt.xlabel("t(s)")
plt.title('Phase(w)')
plt.grid()

plt.figure(figsize=(20,10))
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
plt.figure(figsize=(20,10))
plt.semilogx(timmy,data1,color="blue")
plt.xlabel("t(s)")
plt.title('x1(t)')
plt.grid()