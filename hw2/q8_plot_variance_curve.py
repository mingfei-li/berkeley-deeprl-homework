import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y_1 = np.log((4*x**2 + 8*x + 1) / (x * (1 - x)**4))
y_2 = np.log((x**2 + 3*x + 1) / (x * (1 - x)**4))

plt.figure(figsize=(12, 7))
plt.plot(x, y_1, label='Full reward')
plt.plot(x, y_2, label='Reward to go')
plt.xlabel('Theta')
plt.ylabel('Variance (logorithm scale)')
plt.legend()

plt.savefig('q8_varience_curves.png')