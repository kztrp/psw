from matplotlib import pyplot as plt
import numpy as np
import random
from skimage import morphology

fig,ax = plt.subplots(4,2)
image = np.zeros((32, 64))
random_points = np.random.choice(list(range(31*63)), 256)
image.ravel()[random_points]=1
image.ravel()[random_points+1]=1
image.ravel()[random_points-64]=1
dis = morphology.disk(1)
dil = morphology.binary_dilation(image, dis)
ero = morphology.binary_erosion(image, dis)
opening = morphology.binary_dilation(morphology.binary_erosion(image, dis), dis)
closing = morphology.binary_erosion(morphology.binary_dilation(image, dis), dis)
#otwarcie - erozja -> dylatacja
#zamknicie - dylatacja -> erozja
con = np.array([closing, opening, image])
con = con.transpose((1,2,0))
print(con.shape)
ax[0,0].imshow(image)
ax[0,1].imshow(dis)
ax[1,0].imshow(dil)
ax[1,1].imshow(ero)
ax[2,0].imshow(opening)
ax[2,1].imshow(closing)
ax[2,1].imshow(closing)
ax[3,0].imshow(con)
plt.savefig('plt.png')