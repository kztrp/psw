import numpy as np
import matplotlib.pyplot as plt

resolutions = [8, 16, 32, 64, 128, 256]
depth = range(1, 5)
fig, ax = plt.subplots(len(resolutions), 6, figsize=(20,15))

for i in range(len(resolutions)):
    lin = np.linspace(0, 8*np.pi, resolutions[i])
    sinus = np.sin(lin)
    noise = np.random.normal(0, 0.1, resolutions[i])
    sinus += noise
    image = sinus[:,np.newaxis] * sinus[np.newaxis,:]
    image = (image+1)/ 2
    image = np.clip(image, 0, 1)
    ax[i, 0].plot(sinus)
    ax[i, 0].set_title('sinus')
    ax[i, 1].imshow(image, cmap='binary')

    for j in depth:
        dmin, dmax = (0, np.power(2, j)-1)
        digital_image = np.rint(image* dmax)
        ax[i, j+1].imshow(digital_image, cmap='binary')

plt.savefig('foo2.png')
