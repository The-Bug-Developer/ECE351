################################################################
#                                                              #
# Zachary DeLuca                                               #
# ECE 351 Section 53                                           #
# Lab 11                                                       #
# Due: Apr 11                                                  #
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
from scipy . fftpack import fft , fftshift   
from matplotlib import patches                  #
################################################################

    
    
def zplane(b,a,filename = None):    
    ax = plt.subplot(1,1,1)
    uc = patches.Circle((0,0),radius=1,fill=False,color='black',ls='dashed')
    ax.add_patch(uc)
    
    if np.max(b)>1:
        kn = np.max(b)
        b = np.array(b)/float(kn)
    else:
        kn=1
    if np.max(a)>1:
        kd = np.max(a)
        a = np.array(a)/float(kd)
    else:
        kd = 1
    p = np.roots(a)
    z = np.roots(b)
    k= kn/float(kd)
    
    t1= plt.plot(z.real,z.imag,'o',ms=10,label='Zeros')
    plt.setp(t1,markersize=12.0,markeredgewidth=3.0)
    

    t2 = plt . plot ( p . real , p . imag , 'x ' , ms =10 , label = ' Poles ')
    plt . setp ( t2 , markersize =12.0 , markeredgewidth =3.0)
    
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.legend()
    
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
    return z,p,k

# H(z) = \frac{2-40z^-1}{1-10z^-1+16z^-2}
# h(k) = -4*8^k+6*2^k
    
poles = sig.residuez([2,-40],[1,-10,16])
print(poles)

zplane([2,-40],[1,-10,16])
thing1,thing2 = sig.freqz([2,-40],[1,-10,16],whole=True)


