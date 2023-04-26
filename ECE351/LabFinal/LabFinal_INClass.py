# -*- coding: utf-8 -*-
"""
DeLuca, Zachary
V00838015
Section 53
EE
"""

#default headers
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
"""
Task 1
"""
plt.rcParams.update({'font.size':18})
first = np.arange(-20,15,1)
first = first*-1
print('First Task')
print('Arange:',first)
"""
The arange function creates a list that starts at the bottom number and ends at the 
top number, moving in increments of the third argument, or step size 
"""

second = np.linspace(0.+0.j,5.+5.j,6)
print('Linspace:',second)
"""
The linspace function is like the arange function, except it works with complex
numbers and it asks for how many elements instead of step size
"""

third = np.array([0,-9,-12,-15,-18,-21,-24,-27,-30,-33,-36])
print('Array:', third)
"""
The array function creates an array from a given list instead of auto populating 
the container like the previous funcitons
"""

t = np.arange(0,6,1e-3)

def fun1(t):
    return np.sin(5*np.pi*t)
def fun2(t):
    return 4*np.cos(0.6*np.pi*t)
def fun3(t):
    return 5*np.exp(-0.2*t)*np.sin(3.2*np.pi*t)
def fun4(t):
    return np.exp(-2*t)+2*np.exp(-4.6*t)+3*np.exp(-0.3*t)

one,two,three,four = t,t,t,t
one = fun1(t)
two = fun2(t)
three = fun3(t)
four = fun4(t)

plt.figure(figsize = (20,15))
plt.suptitle('ECE 351 Final - Question 2')
plt.subplot(2,2,1)
plt.ylim(-2,2)
plt.plot(t,one,color = 'black')
plt.legend(['$sin(5 \pi t)$'],loc="upper right")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.title('$x_1$')
plt.subplot(2,2,2)
plt.ylim(-5,5)
plt.plot(t,two,color = 'blue')
plt.legend(['$4cos(0.6 \pi t)$'],loc="upper left")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.title('$x_2$')
plt.subplot(2,2,3)
plt.ylim(-5,5)
plt.title('$x_3$')
plt.plot(three,color = 'magenta')
plt.legend(['$5e^{-0.2t}sin(3.2 \pi t)$'],loc="upper right")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.subplot(2,2,4)
plt.ylim(0,6)
plt.title('$x_4$')
plt.plot(t,four, color = 'green')
plt.legend(['$e^{-2t}+2e^{-4.6t}+3e^{-0.1t}$'],loc="upper right")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('x(t)')

"""
Task 3 
"""
# Y(3s^2+2s+26)=X(s^2+7s-11)

num = [1,7,-11]
den = [3,2,26]

zeros,poles,ga=sig.tf2zpk(num,den)
print()
print('Third Task')
print('Zeros:',zeros,'Poles',poles)

feed = num,den
m,n= sig.impulse(feed)

plt.figure(figsize = (20,10))
plt.title('ECE 351 Final - Question 3')
plt.grid()
plt.plot(m,n)
plt.xlim(0,10)

m,n = sig.step(feed)

plt.plot(m,n)
plt.legend(['Inpulse Response','Step Response'])

"""
Both responses are stable as they both die out to some constant
instead of taking off into infinity 
"""

"""
Task 4 
"""
uno = np.convolve(two,three)*0.001
due = np.convolve(two,four)*0.001
tre = np.convolve(four,one)*0.001
quatro = np.convolve(one,two)*0.001

#print (len(uno),len(due),len(tre),len(quatro))

t = np.linspace(0,15,11999)

plt.figure(figsize = (25,15))
plt.suptitle('ECE 351 Final - Question 4')
plt.subplot(2,2,1)
#plt.ylim(-4,4)
plt.plot(t,uno,color = 'black')
plt.legend(['$x_2*x_4$'],loc="upper right")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('f(t)')
plt.title('$f_1$')
plt.subplot(2,2,2)
#plt.ylim(-5,5)
plt.plot(t,due,color = 'blue')
plt.legend(['$x_2*x_4$'],loc="upper right")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('f(t)')
plt.title('$f_2$')
plt.subplot(2,2,3)
#plt.ylim(-5,5)
plt.title('$f_3$')
plt.plot(t,tre,color = 'purple')
plt.legend(['$x_4*x_1$'],loc="upper right")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('f(t)')
plt.subplot(2,2,4)
#plt.ylim(0,6)
plt.title('$f_4$')
plt.plot(t,quatro, color = 'purple')
plt.legend(['$x_1*x_2$'],loc="lower right")
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('f(t)')