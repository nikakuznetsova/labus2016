__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
x=np.arange (-3, 3.01, 0.01)
plt.plot(x, x**2-x-6)
plt.grid(True)
plt.show()