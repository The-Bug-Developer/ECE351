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
    return (2*np.cos(4*np.pi*t-2)+np.sin(12*np.pi*t+3))

def autorange(bound,step):
    array = np.arange(-bound,bound+1,step*2*bound)
    return array

timmy = autorange(2,step)
freaky = autorange(50,step)

one = fun1(timmy)
two = fun2(timmy)
three = fun3(timmy)

def crank(t,f,i,fs):
    b1,b2,b3 = point(f,fs)
    plt.figure(figsize=(45,15))
    plt.subplot(3,2,(1,2))
    plt.plot(t,f,color="purple")
    plt.xlabel("t(s)")
    plt.title('x(t)')
    plt.grid()
    
    plt.subplot(3,2,3)
    plt.stem(b3,b1,markerfmt="blue",linefmt="blue")
    plt.xlabel("F(w)")
    plt.title('XMAG')
    plt.grid()
    
    plt.subplot(3,2,4)
    plt.stem(b3,b2,markerfmt="red",linefmt="red")
    plt.xlabel("F(w)")
    plt.title('XANG')
    plt.grid()
    
    top = (int)((len(f)/2)+(i))+1
    bottom = (int)((len(f)/2)-(i))
    
    print ('top',top,'bottom',bottom)
    
    i1 = b1[bottom:top]
    i2 = b2[bottom:top]
    
    funky = autorange(i,1/(2*i))
    
    plt.subplot(3,2,5)
    plt.stem(funky,i1,markerfmt="blue",linefmt="blue")
    plt.xlabel("F(w)")
    plt.title('XMAG')
    plt.grid()
    
    plt.subplot(3,2,6)
    plt.stem(funky,i2,markerfmt="red",linefmt="red")
    plt.xlabel("F(w)")
    plt.title('XANG')
    plt.grid()

crank(timmy,one,2,100)
crank(timmy,two,2,100)
crank(timmy,three,2,100)

high = 16
low = 0
t = np.arange(low,high,step)
T = 8
omega = 2*np.pi/T

def approximate(Time,terms):
    waves = np.zeros(Time.size)
    for k in range(terms):
        if(k!=0):
            for t in range(Time.size):
                waves[t]+=(2/(np.pi*k))*(1-np.cos(np.pi*k))*(np.sin(k*omega*t*step))
    return waves
square = approximate(t,15)
crank(t,square,10,100)


crank(timmy,one,2,10)
crank(timmy,one,2,100)
crank(timmy,one,2,1000)
crank(timmy,one,2,10000)
crank(timmy,one,2,100000)