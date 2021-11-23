import skimage
from matplotlib import pyplot as plt
import numpy as np

image = skimage.data.chelsea()
n=100
noise = np.random.normal(0, 512, size=image.shape + (n,))
# print(noise[0].shape)
fig, ax = plt.subplots(3,1)
noised_image = image[:,:,:,np.newaxis] + noise
noised_image = np.clip(noised_image, 0 ,255)
noised_image -= np.min(noised_image)
noised_image /= np.max(noised_image)
N = np.power(2,8)-1
# for i in range(n):

dmin, dmax = [0, N]
n_digm = np.rint(noised_image * dmax)

unnoised = np.zeros(image.shape)
for i in range(n_digm.shape[3]):
    unnoised = unnoised + n_digm[:,:,:,i]

unnoised /= np.max(unnoised)
    # n_matrix = n_matrix + n_digm
ax[0].imshow(image)
ax[1].imshow(noised_image[:,:,:,0])
ax[2].imshow(unnoised)

plt.savefig('foo.png')
