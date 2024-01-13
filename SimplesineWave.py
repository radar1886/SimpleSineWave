import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,5*np.pi, 0.1)
y = np.sin(x);


plt.plot(x,y, color='green')
plt.show()