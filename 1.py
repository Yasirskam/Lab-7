
#%%
from numpy import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = linspace(1,10,40)
y=5*sin(10*x)*sin(3*x)/(x^x)
plt.plot(x, y, 'g--', label='5*sin(10*x)*sin(3*x)/(x**x)') 
plt.axis([1, 10 , -1, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік')
plt.legend()

plt.show()