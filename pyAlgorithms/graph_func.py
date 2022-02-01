import numpy as np
import matplotlib.pyplot as plt 

def function(x):
	return x**2

x = np.arange(-10, 10, 0.01)
y = [function(n) for n in x]

plt.plot(x, y)
plt.show()