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
step = 1e-4
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
    return 2*np.cos(4*np.pi*t-2)+np.sin(12*np.pi*t+3)

def autorange(bound,step):
    array = np.arange(-bound,bound,step*2*bound)
    return array

timmy = autorange(2,step)
freaky = autorange(50,step)

one = fun1(timmy)
two = fun2(timmy)
three = fun3(timmy)

buffer1,buffer2,buffer3 = point(one,100)
buffer4,buffer5,buffer6 = point(two,100)
buffer7,buffer8,buffer9 = point(three,100)

def crank(t,f,b1,b2,b3):
    plt.figure(figsize=(10,5))
    plt.subplot(3,2,(1,2))
    plt.plot(t,f,color="purple")
    plt.xlabel("t(s)")
    plt.title('x(t)')
    plt.grid()
    
    plt.subplot(3,2,3)
    plt.plot(b3,b1,color="blue")
    plt.xlabel("F(w)")
    plt.title('XMAG')
    plt.grid()
    
    plt.subplot(3,2,4)
    plt.plot(b3,b2,color="red")
    plt.xlabel("F(w)")
    plt.title('XANG')
    plt.grid()
    
    interest = f[(int)(f.size/2-2*100):(int)(f.size/2+2*100)]
    print(interest[0],interest[399])
    i1,i2,i3 = point(interest,100)
    
    plt.subplot(3,2,5)
    plt.plot(i3,i1,color="blue")
    plt.xlabel("F(w)")
    plt.title('XMAG')
    plt.grid()
    
    plt.subplot(3,2,6)
    plt.plot(i3,i2,color="red")
    plt.xlabel("F(w)")
    plt.title('XANG')
    plt.grid()
    
crank(timmy,one,buffer1,buffer2,buffer3)
