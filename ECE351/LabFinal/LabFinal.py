################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 12                                                       #
# Due: Apr 25                                                  #
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
from matplotlib import patches                                 #
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

def autorange(bound,step):
    array = np.arange(-bound,bound+1,step*2*bound)
    return array

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


lpc = np.array([2.61,0.38,1.08,0.924])
lpc = lpc/(2000*2*np.pi)

A = 2/lpc[0]
B = 2/lpc[2]

lol = sig.TransferFunction([1/(lpc[0]*lpc[1])*1/(lpc[2]*lpc[3])],[1,A+B,2+A*B,A+B,1])
hi = sig.TransferFunction([1,0,0,0,0],[1,A+B,2+A*B,A+B,1])
wl,ml,pl = sig.bode(lol)
wh,mh,ph = sig.bode(lol)


plt.figure(figsize=(10,4))
plt.semilogx(wl,ml)
plt.figure(figsize=(10,4))
plt.semilogx(wh,mh)
