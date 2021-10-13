import numpy as np
import matplotlib.pyplot as plt

x = np.zeros((16,16))

x[5:10, 3:12] = 1
resolution = 256
resolutions = [8, 16, 32, 64, 128, 256]
lin = np.linspace(0, 8*np.pi, resolution)
sinus = np.sin(lin)
fig, ax = plt.subplots(2, 3, figsize=(10,5))
# ax[0,0].imshow(x, cmap='binary', vmin=0, vmax=16)
# plt.tight_layout()
ax[0, 0].plot(lin)
ax[0, 0].set_title('sampling space')
ax[0, 1].plot(sinus)
ax[0, 1].set_title('sinus')
ax[0, 2].plot(lin, sinus)
ax[0, 1].set_title('reflectance')
image = sinus[:,np.newaxis] * sinus[np.newaxis,:]
image = (image+1)/ 2
image = np.clip(image, 0, 1)
ax[1, 0].imshow(image, cmap='binary')
ax[1, 0].set_title("{}, {}".format(round(np.min(image),3), round(np.max(image),3)))
depth = 5
dmin, dmax = (0, np.power(2, depth)-1)
digital_image = np.rint(image* dmax)
ax[1, 1].imshow(digital_image, cmap='binary')

plt.savefig('foo.png')
