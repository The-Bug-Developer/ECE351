################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 04                                                       #
# Due: Feb 14                                                  #
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

def other_conv(f1, f2):
    dif12 = len(f1)-len(f2)
    dif21 = len(f2)-len(f1)
    if dif12 > 0:
        app1=dif12
    else:
        app1 =0
    if dif21 > 0:
        app2=dif21
    else:
        app2 =0
    f1 = np.append(f1,np.zeros(app1))
    f2 = np.append(f2,np.zeros(app2))
    result = np.zeros(len(f1)+len(f2))
    for i in range((len(f1)+len(f2))-2):
        result[i]=0
        for j in range(len(f1)):
            if(((i-j+1)>0)):
                try:
                    result[i]+=f1[j]*f2[i-j+1]
                except:
                   1==1
    return result

def u(start,intake):
    if intake >= start:
        output= 1
    else:
        output = 0
    return output
def U(intake):
    if intake >= 0:
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


def h1(intake):
    return np.exp(-2*intake)*(u(0,intake)-u(3,intake))
def h2(intake):
    return u(2,intake)-u(6,intake)
def h3(intake):
    return np.cos(omega*intake)*u(0,intake)
def populate(F1,f1):
    F1 = np.zeros(bound)
    for i in range(bound):
        j=i*step
        F1[i] = f1(j+low)
    return F1

step = 1e-2
low = -10
up = 10
dif = up-low
conSize = 5*dif
hi = dif/2
t = np.arange(low,up,step)
size = dif*2
omega = np.pi/2
bound = round(dif/step)

H1 = {0}
H1= populate(H1,h1)
H2 = {0}
H2= populate(H2,h2)
H3 = {0}
H3= populate(H3,h3)
Ut={0}
Ut=populate(Ut,U)

plt.figure(figsize=(dif,hi))
plt.subplot(3,1,1)
plt.plot(t,H1)
plt.title('H1')
plt.subplot(3,1,2)
plt.plot(t,H2)
plt.title('H2')
plt.subplot(3,1,3)
plt.plot(t,H3)
plt.title('H3')
print('top done')

t = np.arange(low,up,step/2)
h11=other_conv(H1,Ut)
plt.figure(figsize=(dif,hi))
plt.subplot(3,1,1)
plt.plot(t,h11)
plt.title('H1')
print('1 done')

h12=other_conv(H2,Ut)
plt.subplot(3,1,2)
plt.plot(t,h12)
plt.title('H2')
print('2 done')

h13=other_conv(H3,Ut)
plt.subplot(3,1,3)
plt.plot(t,h13)
plt.title('H3')
print('3 done')
