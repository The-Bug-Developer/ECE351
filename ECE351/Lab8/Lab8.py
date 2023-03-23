################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 07                                                       #
# Due: Mar 21                                                  #
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
high = 16
low = 0
step = 0.01
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
total = 1+3+15+50+150+1500

terms = 1
ammount = terms*t.size
one = np.zeros(ammount)
one = approximate(t*step,terms)
print("Loading:",100*(1/total),"%")
terms = 3
ammount = terms*t.size
three = np.zeros(ammount)
three = approximate(t*step,terms)
print("Loading:",100*(4/total),"%")
terms = 15
ammount = terms*t.size
fifteen = np.zeros(ammount)
fifteen = approximate(t*step,terms)
print("Loading:",100*(19/total),"%")
terms = 50
ammount = terms*t.size
fifty = np.zeros(ammount)
fifty = approximate(t*step,terms)
print("Loading:",100*(69/total),"%")
terms = 150
ammount = terms*t.size
onefity = np.zeros(ammount)
onefity = approximate(t*step,terms)
print("Loading:",100*(219/total),"%")
terms = 1500
ammount = terms*t.size
bunch = np.zeros(ammount)
bunch = approximate(t*step,terms)

plt.figure(figsize=(20,10))
plt.subplot(6,1,1)
plt.plot(t,one)
plt.title('N=1')
plt.subplot(6,1,2)
plt.plot(t,three)
plt.title('N=3')
plt.subplot(6,1,3)
plt.plot(t,fifteen)
plt.title('N=15')
plt.subplot(6,1,4)
plt.plot(t,fifty)
plt.title('N=50')
plt.subplot(6,1,5)
plt.plot(t,onefity)
plt.title('N=150')
plt.subplot(6,1,6)
plt.plot(t,bunch)
plt.title('N=1500')