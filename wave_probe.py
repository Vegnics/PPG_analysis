import numpy as np
import h5py
from matplotlib import pyplot as plt
import cv2

"""
image = cv2.imread("splines.png",0)
x= np.array([k for k in range(image.shape[1])])
y=[]
for j in range(image.shape[1]):
    column = image[:,j]
    val = np.where(column == 0)
    if val[0].size > 0:
        val = np.mean(val[0])
        val = 696 - val
        y.append(val)
y=np.array(y)
np.save("ppg_int.npy",y)
"""
N = 10
ppg=np.load("ppg_int.npy")
ppg_total=ppg
for i in range(N):
    ppg_total=np.hstack((ppg_total,ppg))


plt.plot(ppg_total)
plt.show()



