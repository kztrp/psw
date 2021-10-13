import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,9,9)
y = x[:, np.newaxis] * x[np.newaxis, :]
print(x)
print(y)
