import numpy as np
import simulation as sim

f = lambda x : sum(x**2) + np.random.normal(0, 5, 1)
g = lambda x : sum(x**2) + np.random.normal(0, 1, 1) + (1 / sum(x**2))

x = np.random.normal(0, 10, (10, 5))

phys = np.apply_along_axis(f, 1, x)
comp = np.apply_along_axis(g, 1, x)

print("Phys:", phys)
print("Comp:", comp)
