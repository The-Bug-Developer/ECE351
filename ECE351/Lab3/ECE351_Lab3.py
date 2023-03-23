################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 03                                                       #
# Due: Feb 07                                                  #
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
step = 1e-2
low = 0
up = 20
dif = up-low
hi = dif/2
t = np.arange(low,up,step)
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
def f1(intake):
    output = u(2,intake)-u(9,intake)
    return output
def f2(intake):
    output = np.exp(-intake)*u(0,intake)
    return output
def f3(intake):
    output = r(2,intake)*(u(2,intake)-u(3,intake))+r(4,-intake)*(u(3,intake)-u(4,intake))
    return output
F1 = np.zeros(round(dif/step))
for i in range(round(up/step)):
    j=i*step
    F1[i] = f1(j)

plt.figure(figsize=(dif,hi))
plt.plot(t,F1)
plt.title('F1')

F2 = np.zeros(round(dif/step))
for i in range(round(up/step)):
    j=i*step
    F2[i] = f2(j)

plt.figure(figsize=(dif,hi))
plt.plot(t,F2)
plt.title('F2')

F3 = np.zeros(round(dif/step))
for i in range(round(up/step)):
    j=i*step
    F3[i] = f3(j)

plt.figure(figsize=(dif,hi))
plt.plot(t,F3)
plt.title('F3')



def other_conv(f1, f2):
    f1 = np.append(f1,np.zeros(len(f2)))
    f2 = np.append(f2,np.zeros(len(f1)))
    result = np.zeros(len(f1)+len(f2))
    for i in range((len(f1)+len(f2))-2):
        result[i]=0
        for j in range(len(f1)):
            if(((i-j+1)>0)):
                try:
                    result[i]+=f1[j]*f2[i-j+1]
                except:
                    print(i,j)
    return result


convloved1 = np.zeros(round(dif/step)*5)
convloved2 = np.zeros(round(dif/step)*5)
convloved3 = np.zeros(round(dif/step)*5)
convolved1 = other_conv(F1,F2)
convolved2 = other_conv(F2,F3)
convolved3 = other_conv(F1,F3)

t = np.arange(low,up*5,step)
plt.figure(figsize=(dif,hi))
plt.plot(t,convolved1)
plt.title('Convolved')

plt.figure(figsize=(dif,hi))
plt.plot(t,convolved2)
plt.title('Convolved')

plt.figure(figsize=(dif,hi))
plt.plot(t,convolved3)
plt.title('Convolved')