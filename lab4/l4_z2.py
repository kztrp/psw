import numpy as np
from matplotlib import pyplot as plt
import skimage

img = np.mean(skimage.data.chelsea(), axis=-1).astype(np.uint8)

c_map = "Blues_r"
fig, ax = plt.subplots(4,1, figsize=(10,10))
ax[0].imshow(img, cmap=c_map)
img = img[::10, ::10]
source_values = np.reshape(img, -1)
aspect = img.shape[0]/img.shape[1]
x_source_space = np.linspace(0,1, img.shape[0])
y_source_space = np.linspace(0,aspect, img.shape[1])
A = np.meshgrid(x_source_space, y_source_space)


plt.savefig('foo2.png')
