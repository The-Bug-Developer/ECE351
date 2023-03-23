################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 02                                                       #
# Due: Jan 31                                                  #
#                                                              #
################################################################
import numpy as np                                             #
import matplotlib . pyplot as plt                              #
import scipy as sp                                             #
import scipy . signal as sig                                   #
import pandas as pd                                            #
import control                                                 #
import time                                                    #
from scipy . fftpack import fft , fftshift                     #
################################################################
step = 1e-1
low = -5
up = 15+step
dif = up-low
t = np.arange(low,up,step)
fun1 = np.cos(t)

plt.figure(figsize=(dif,3))
plt.plot(t,fun1)
plt.title('Example of Cosine')


def u(start,intake):
    if intake >= start:
        output= 1
    else:
        output = 0
    return output
def r(start,intake):
    if intake >= start:
        output= intake-start
    else:
        output = 0
    return output
time = low


ft = np.zeros(round(dif/step))
for i in range(round(dif/step)):
    j = i*step
    if t[i]<0:
        ft[i]=0
    else:
        ft[i] = r(0-time,j)-r(3-time,j)+5*u(3-time,j)-2*u(6-time,j)-2*r(6-time,j)+2*r(9-time,j)
plt.figure(figsize=((dif),5))
plt.plot(t,ft)
plt.title('Function Untouched')

time = low
ft = np.zeros(round(dif/step))
for i in range(round(dif/step)):
    j = i*step
    if t[i]<0:
        ft[i]=0
    else:
        ft[i] = r(0-time,j)-r(3-time,j)+5*u(3-time,j)-2*u(6-time,j)-2*r(6-time,j)+2*r(9-time,j)
plt.figure(figsize=((dif),5))
plt.plot(-t,ft)
plt.title('Function Reversed')

time = low-4
ft = np.zeros(round(dif/step))
for i in range(round(dif/step)):
    j = i*step
    if t[i]<0:
        ft[i]=0
    else:
        ft[i] = r(0-time,j)-r(3-time,j)+5*u(3-time,j)-2*u(6-time,j)-2*r(6-time,j)+2*r(9-time,j)
plt.figure(figsize=((dif),5))
plt.plot(t,ft)
plt.title('Function Translated by 4')

time = low-4
ft = np.zeros(round(dif/step))
for i in range(round(dif/step)):
    j = i*step
    if t[i]<0:
        ft[i]=0
    else:
        ft[i] = r(0-time,j)-r(3-time,j)+5*u(3-time,j)-2*u(6-time,j)-2*r(6-time,j)+2*r(9-time,j)
plt.figure(figsize=((dif),5))
plt.plot(-t,ft)
plt.title('Function Inverted and Translated by 4')

time = low
ft = np.zeros(round(dif/step))
for i in range(round(dif/step)):
    j = i*step
    if t[i]<0:
        ft[i]=0
    else:
        ft[i] = r(0-time,j)-r(3-time,j)+5*u(3-time,j)-2*u(6-time,j)-2*r(6-time,j)+2*r(9-time,j)
ft = np.append(ft,0)
plt.figure(figsize=((dif),5))
plt.plot(t,np.diff(ft))
plt.title('Function Derivative')


ft = np.zeros(round(dif/step))
for i in range(round(dif/step)):
    j = i*step
    if t[i]<0:
        ft[i]=0
    else:
        ft[i] = r(0-time,j)-r(3-time,j)+5*u(3-time,j)-2*u(6-time,j)-2*r(6-time,j)+2*r(9-time,j)
plt.figure(figsize=((dif),5))
plt.plot(t/2,ft)
plt.title('Function Halved')

ft = np.zeros(round(dif/step))
for i in range(round(dif/step)):
    j = i*step
    if t[i]<0:
        ft[i]=0
    else:
        ft[i] = r(0-time,j)-r(3-time,j)+5*u(3-time,j)-2*u(6-time,j)-2*r(6-time,j)+2*r(9-time,j)
plt.figure(figsize=((dif),5))
plt.plot(2*t,ft)
plt.title('Function Doubled')