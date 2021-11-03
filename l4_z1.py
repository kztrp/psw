import numpy as np
from matplotlib import pyplot as plt


points = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])

ones = np.ones((points.shape[0],1))
A = np.concatenate((points, ones), axis=1)
theta=1
transformations = {
'jednokladnosc': np.array([[1,0,0],[0,1,0],[0,0,1]]),
'translacja_x_y': np.array([[1,0,.5],[0,1, .5],[0,0,1]]),
'odbicie_x': np.array([[-1,0,0],[ 0,1,0],[ 0,0,1]]),
'odbicie_y': np.array([[1, 0,0],[0,-1,0],[0, 0,1]]),
'skalowanie_x': np.array([[2,0,0],[0,1,0],[0,0,1]]),
'skalowanie_y': np.array([[1,0,0],[0,2,0],[0,0,1]]),
'obrot_theta': np.array([[np.cos(theta), -np.sin(theta),0],[np.sin(theta),np.cos(theta),0],
[0,0,1]]),
'pochylenie_x': np.array([[1, .5,0],[0,1,0],[0,0,1]]),
'pochylenie_y': np.array([[1, 0,0],[.5,1  ,0],[0,0  ,1]]),
}
fig, ax = plt.subplots(3,3, figsize=(10,10))
keys = np.array([*transformations]).reshape(3,3)
for i in range(keys.shape[0]):
    for j in range(keys.shape[1]):
        ax[i,j].plot(A[:,0],A[:,1], color='red')
        ax[i,j].scatter(A[:,0],A[:,1], color='red')
        key = keys[i][j]
        value = transformations.get(key)
        Z = A @ value.T
        ax[i,j].plot(Z[:,0],Z[:,1], color='blue')
        ax[i,j].scatter(Z[:,0],Z[:,1], color='blue')
        ax[i,j].set_xlim(-2,3)
        ax[i,j].set_ylim(-2,3)
        ax[i,j].grid(ls=':')


plt.savefig('foo.png')
