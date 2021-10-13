import numpy as np
from matplotlib import pyplot as plt

depth = 2
drange = (-1, 1)
resolution = 256
n_iter = 256
N = np.power(2, depth)-1
prober = np.linspace(0, np.pi*8, resolution)
prober = np.sin(prober)
fig, ax = plt.subplots(2, 3, figsize=(12,8))
perfect_image = prober[:,np.newaxis] * prober[np.newaxis,:]
n_matrix = np.zeros(perfect_image.shape)
o_matrix = np.zeros(perfect_image.shape)

for i in range(n_iter):
    noise = np.random.normal(0, 1, perfect_image.shape)
    n_image = perfect_image + noise
    o_image = perfect_image.copy()
    n_image = (n_image+1)/2
    o_image = (o_image+1)/2
    n_image = np.clip(n_image, 0, 1)
    o_image = np.clip(o_image, 0, 1)
    n_dimg = np.rint(N * n_image)
    o_dimg = np.rint(N * o_image)

    n_matrix += n_dimg
    o_matrix += o_dimg

    ax[0,0].imshow(perfect_image, cmap='binary')
    ax[1,0].imshow(noise, cmap='binary')
    ax[0,1].imshow(o_dimg, cmap='binary')
    ax[1,1].imshow(n_dimg, cmap='binary')
    ax[0,2].imshow(o_matrix, cmap='binary')
    ax[1,2].imshow(n_matrix, cmap='binary')
plt.savefig("foo.png")
