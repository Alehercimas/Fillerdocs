# Plotting a "sort" of sphere, basically testing some Python functions out

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def rotx(th):
    rotx = np.array([[1, 0, 0], [0, np.cos(th), -np.sin(th)], 
                     [0, np.sin(th), np.cos(th)]])
    return rotx

fig = plt.figure(figsize=(8,8))
ax = fig.gca(projection='3d')
z = np.zeros(51)
rotties = np.zeros(3)
Theta = np.linspace(0,np.pi*2, 51)
cosinus = np.array([])
sinus = np.array([])
for i in Theta:
    cosinus = np.append(cosinus,(np.cos(i)))
    sinus = np.append(sinus, (np.sin(i)))
arrh = np.hstack(((cosinus.reshape(51,1)), 
                  (sinus.reshape(51,1)), z.reshape(51,1)))
for j in Theta:
    for k in arrh:
        rotta = rotx(j) @ k.reshape(3,1)
        rotta = rotta[:,0]
        rotties = np.append(rotties, rotta).reshape(-1,3)
ax.plot(rotties[:,0], rotties[:,1], rotties[:,2])
plt.show()
