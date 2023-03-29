################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 09                                                       #
# Due: Mar 28                                                  #
#                                                              #
################################################################
import numpy as np                                             #
import matplotlib . pyplot as plt                              #
import scipy as sp                                             #
import scipy . signal as sig                                   #
import pandas as pd                                            #                                               #
import time                                                    #
import math                                                    #
from scipy . fftpack import fft , fftshift                     #
################################################################
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
def point(x,fs):
    N = len ( x ) # find the length of the signal
    X_fft = sp.fftpack.fft ( x ) # perform the fast Fourier transform ( fft )
    X_fft_shifted = sp.fftpack.fftshift( X_fft ) # shift zero frequency components
    # to the center of the spectrum
    freq = np.arange ( - N /2 , N /2) * fs / N # compute the frequencies for the output
    # signal , ( fs is the sampling frequency and
    # needs to be defined previously in your code
    X_mag = np.abs ( X_fft_shifted ) / N # compute the magnitudes of the signal
    X_phi = np.angle ( X_fft_shifted ) # compute the phases of the signal
    # ----- End of user defined function ----- #
    
    
    return X_mag,X_phi,freq

def fun1(t):
    return np.cos(2*np.pi*t)
def fun2(t):
    return 5*np.sin(2*np.pi*t)
def fun3(t):
    return 2*np.cos(4*np.pi-2)+np.sin(12*np.pi+3)*np.sin(12*np.pi+3)
step = 1e-1
timmy = np.arange(-2,2,step)
freaky = np.arange(-50,50,step)
interest = np.arange(-20,20,step)
uno = timmy
one = interest

uno = fun1(uno)
one = fun1(one)

buffer1 = freaky
buffer2 = freaky
buffer3 = 0

buff1 = interest
buff2 = interest

buffer1,buffer2,buffer3 = point(uno,100)
buff1,buff2,buffer3 = point(one,100)

def plotmachine(t,f,i,first,second,third,fourth,fifth):
    plt.figure(figsize=(10,5))
    plt.subplot(3,2,(1,2))
    plt.plot(t,first,color="red")
    plt.xlabel("t(s)")
    plt.title('x(t)')
    plt.grid()
    plt.subplot(3,2,3)
    plt.stem(f,second,linefmt="yellow",markerfmt="yellow")
    plt.ylabel('XANG')
    plt.xlabel('f[Hz]')
    plt.grid()
    plt.subplot(3,2,4)
    plt.stem(i,third,linefmt="yellow",markerfmt="yellow")
    plt.ylabel('XANG')
    plt.xlabel('f[Hz]')
    plt.grid()
    plt.subplot(3,2,5)
    plt.stem(f,fourth,linefmt="green",markerfmt="green")
    plt.ylabel('XANG')
    plt.xlabel('f[Hz]')
    plt.grid()
    plt.subplot(3,2,6)
    plt.stem(i,fifth,linefmt="green",markerfmt="green")
    plt.ylabel('XMAG')
    plt.xlabel('f[Hz]')
    plt.grid()

plotmachine(timmy,freaky,interest,uno,buffer1,buff1,buffer2,buff2)
