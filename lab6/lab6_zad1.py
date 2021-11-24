import matplotlib.pyplot as plt
import numpy as np
from skimage.draw import rectangle
from skimage.transform import rotate
from scipy.signal import convolve2d, medfilt

fig,ax = plt.subplots(3,2)
entry_img = np.zeros((256, 256))
rr, cc = rectangle((32,32), end=(92, 92))
entry_img[rr, cc] = 1
rr, cc = rectangle((92,92), end=(128, 128))
entry_img[rr, cc] = 1
rr, cc = rectangle((128,128), end=(144, 144))
entry_img[rr, cc] = 1
first_angle = np.random.uniform(low=-20, high=20)
rot_img = rotate(entry_img, first_angle)
s1 = np.array([[-1, 0, 1],[-2, 0, 2],[-1,0,1]])
s3 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
angles = np.linspace(-30, 30, 50)
abssums_s1 = np.zeros(50)
abssums_s3 = np.zeros(50)
for index, angle in enumerate(angles):
    out_img = rotate(rot_img, angle)
    ax[0,0].imshow(entry_img)
    ax[0,1].imshow(rot_img)
    ax[1,0].imshow(out_img)
    con_s1 = convolve2d(out_img, s1)
    con_s3 = convolve2d(out_img, s3)
    ax[1,1].imshow(con_s1, cmap='gray')
    ax[2,1].imshow(con_s3, cmap='gray')
    abssums_s1[index] = np.sum(np.abs(con_s1))
    abssums_s3[index] = np.sum(np.abs(con_s3))
    ax[2,0].plot(angles[:index], abssums_s1[:index])
    ax[2,0].plot(angles[:index], abssums_s3[:index])

    plt.savefig('plt.png')
min_s1 = abssums_s1.argmin()
bestangle_s1 = angles[min_s1]
min_s3 = abssums_s3.argmin()
bestangle_s3 = angles[min_s1]
bestangle = (bestangle_s1+bestangle_s3)/2
final_img = rotate(rot_img, bestangle)
stacked = np.stack([entry_img, final_img, rot_img], axis=-1)
plt.imsave('bar.png', stacked)
