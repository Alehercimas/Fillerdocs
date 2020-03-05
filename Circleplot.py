# Plotting a circle! simple as that!
# also testing complex numbers and so on

import numpy as np
import matplotlib.pyplot as plt

TrX = np.array([0.2,0.9,0.6,0.2])
TrY = np.array([0.2,0.2,0.6,0.2])
vv1 = np.complex(TrX[0], TrY[0])
vv2 = np.complex(TrX[1], TrY[1])
vv3 = np.complex(TrX[2], TrY[2])
vv4 = np.complex(TrX[3], TrY[3])
vv1c = np.conj(vv1)
vv2c = np.conj(vv2)
vv3c = np.conj(vv3)
vv4c = np.conj(vv4)
vv1c, vv2c, vv3c, vv4c = 1/vv1c, 1/vv2c, 1/vv3c, 1/vv4c
Trxin = np.array([vv1c.real, vv2c.real, vv3c.real, vv4c.real])
Tryin = np.array([vv1c.imag, vv2c.imag, vv3c.imag, vv4c.imag])
z = np.zeros(51)
Theta = np.linspace(0,np.pi*2, 51)
cosinus = np.array([])
sinus = np.array([])
for i in Theta:
    cosinus = np.append(cosinus,(np.cos(i)))
    sinus = np.append(sinus, (np.sin(i)))
plt.axis('equal')
plt.plot(cosinus, sinus)
plt.plot(TrX, TrY)
plt.plot(Trxin, Tryin)
