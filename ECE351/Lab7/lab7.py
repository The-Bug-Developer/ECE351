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

ZeroG,PolesG,gg = sig.tf2zpk([1,9], sig.convolve([1,-6,-16],[1,4]))
print("Poles and Zeroes of G(s)")
print("Zeroes = ",ZeroG)
print("Poles = ",PolesG)

ZerosA, PolesA, ga = sig.tf2zpk([1,4], [1,4,3])

print("Poles and Zeroes of A(s)")
print("Zeroes = ",ZerosA)
print("Poles = ",PolesA)


RootsB = np.roots([1,26,168])
print("B(s) Roots")
print("Roots = ",RootsB)


den = sig.convolve([1,4,3],[1,-6,-16])
print("denomanator = ",den)

openLoop = [1,9],sig.convolve([1,4,3],[1,-6,-16])
t, s = sig.step(openLoop)


plt.figure(figsize=(20,10))
plt.subplot(2,1,1) 
plt.plot(t, s)
plt.title('Open Loop')  


numG = [1,9]
denG = sig.convolve([1,-6,-16],[1,4])

numA = [1,4]
denA = [1,4,3]

numB = [1,26,168]
denB = [1]


num = sig.convolve(numG, numA)
den = sig.convolve(denA, denG) + sig.convolve(sig.convolve(denA, numB), numG)

print("Numerator = ",num)
print("den = ",den)

closedLoop = num, den
t, s = sig.step(closedLoop)

plt.figure(figsize = (20,10))
plt.subplot(2,1,1) 
plt.plot(t, s)
plt.title('Closed Loop')  