################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 06                                                       #
# Due: Feb 28                                                  #
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
    
step = 1e-3
low = 0
up = 2
dif = up-low
hi = dif/2
t = np.arange(low,up,step)
size = dif*2
bound = 2000
pi=3.14159

def populate(F1,f1):
    F1 = np.zeros(bound)
    for i in range(bound):
        try:
            j=i*step
            F1[i] = f1(j+low)
        except:
            k=1
    return F1

def Hs(s):
    return -6/(s+6)+2/(s+4)
def Ht(t):
    return u(0,t)*(2*np.exp(-2*t)-6*np.exp(-6*t))
def Steps(s):
    return 1/(2*s)+1/(s+6)+1/(2*s+8)
def Stept(t):
    return (0.5*u(0,t)+1*np.exp(-6*t)+0.5*np.exp(-8*t))*0.5*u(-0.001,t)

H1 = t
H2 = t
S1 = t
S2 = t

H1 = populate(H1,Hs)
H2 = populate(H2,Ht)
S1 = populate(S1,Steps)
S2 = populate(S2,Stept)
time, skippy = sig.step(([1,6,12],[1,10,24]),T=t)
timmy, skipped = sig.impulse(([1,6,12],[1,10,24]),T=t)
[R1,P1,_] = sig.residue([1,6,12],[1,10,24,0])

print("roots are ",R1)
print("poles are ",P1)

plt.figure(figsize=(20,10))
plt.subplot(3,1,1)
plt.plot(t,S2)
plt.title('Step t')
plt.subplot(3,1,2)
plt.plot(t,skippy)
plt.title('Step response')
plt.subplot(3,1,3)
plt.plot(t,-skipped)
plt.title('Impulse response')
