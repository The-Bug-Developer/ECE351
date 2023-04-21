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
def autorange(bound,step):
    array = np.arange(-bound,bound+1,step*2*bound)
    return array
class filter():
    def __init__(self,cut,proto,Type):
        self.scale = (cut)
        self.cl = [2/proto,proto/2]
        self.rh = [2/proto,proto/2]
        if Type == 'low':
            self.num = [self.scale**2/(self.cl[0]*self.cl[1])]
            self.den = [1,2*self.scale/self.cl[1],self.scale**2/(self.cl[0]*self.cl[1])]
        if Type == 'high':
            self.num = [1,0,0]
            self.den = [1,2*self.scale/self.rh[1],self.scale**2/(self.rh[0]*self.rh[1])]
        self.transfer = sig.TransferFunction(self.num,self.den)
        self.w,self.m,self.p = sig.bode(self.transfer)
    
def combine(f1,f2):
    n = np.convolve(f1.num,f2.num)
    d = np.convolve(f1.den,f2.den)
    return sig.TransferFunction(n,d)

top = 2000
bot = 1800

lo = [filter(top,0.518,'low'),filter(top,1.41,'low'),filter(top,1.932,'low')]
hi = [filter(bot,0.518,'high'),filter(bot,1.41,'high'),filter(bot,1.932,'high')]

lo1 = combine(lo[0],lo[1])
low = combine(lo1,lo[2])

hi1 = combine(hi[0],hi[1])
high = combine(hi1,hi[2])

wL,mL,pL = sig.bode(low)
wH,mH,pH = sig.bode(high)

lobw = [wH,wH,wH]
lobm = [mH,mH,mH]
lobp = [pH,pH,pH]

hobw = [wH,wH,wH]
hobm = [mH,mH,mH]
hobp = [pH,pH,pH]

i =0
lobw[i],lobm[i],lobp[i]= sig.bode(lo[i].transfer)
i =1
lobw[i],lobm[i],lobp[i]= sig.bode(lo[i].transfer)
i =2
lobw[i],lobm[i],lobp[i]= sig.bode(lo[i].transfer)


i =0
hobw[i],hobm[i],hobp[i]= sig.bode(hi[i].transfer)
i =1
hobw[i],hobm[i],hobp[i]= sig.bode(hi[i].transfer)
i =2
hobw[i],hobm[i],hobp[i]= sig.bode(hi[i].transfer)

total = combine(high,low)
#total.num*=2
#total.den*=2
wt,mt,pt = sig.bode(total)

plt.figure(figsize=(20,10))
plt.grid()
plt.subplot(3,1,1)
plt.semilogx(wL,lobm[0],color="red")
plt.semilogx(wL,lobm[1],color="orange")
plt.semilogx(wL,lobm[2],color="green")
plt.semilogx(wL,mL,color="blue")
plt.axvline(top, color='PURPLE') # cutoff frequency
plt.subplot(3,1,2)
plt.semilogx(wH,hobm[0],color="red")
plt.semilogx(wH,hobm[1],color="orange")
plt.semilogx(wH,hobm[2],color="green")
plt.semilogx(wH,mH,color="blue")
plt.axvline(bot, color='PURPLE') # cutoff frequency
plt.subplot(3,1,3)
plt.axvline(top, color='PURPLE') # cutoff frequency
plt.axvline(bot, color='PURPLE') # cutoff frequency
plt.semilogx(wt,mt,color="black")

df = pd . read_csv ( 'NoisySignal.csv')

t = df [ '0' ]. values
sensor_sig = df [ '1' ]. values
plt . figure ( figsize = (10 , 7) )
plt . plot (t , sensor_sig )
plt . grid ()
plt . title ( ' Noisy Input Signal ')
plt . xlabel ( ' Time [ s ] ')
plt . ylabel ( ' Amplitude [ V ] ')
plt . show ()


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
    
    #print ('top',top,'bottom',bottom)
    
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

after = df * mt
plt.figure(figsize=(20,10))
plt.grid()
plt.semilogx(wL,after,color="red")