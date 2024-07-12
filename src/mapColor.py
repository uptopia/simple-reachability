#===========================#
# Map Value to Jet ColorMap
#===========================#
# Ref:https://stackoverflow.com/questions/7706339/grayscale-to-red-green-blue-matlab-jet-color-scale
import cv2
import numpy as np
import matplotlib.pyplot as plt

height, width = 100, 1000
b, g, r = 0x3E, 0x88, 0xE5  # orange
img = np.zeros((height, width, 3), np.uint8)
img[:, :, 0] = b
img[:, :, 1] = g
img[:, :, 2] = r

h, w, c = img.shape
print('height: ', h)#100
print('width:  ', w)#1000
print('channel:', c)#3


vmin = 0 
vmax = w
for i in range(h):
    for j in range(w):
        # color changes in row
        v=j
        dv = vmax - vmin
        r,g,b=1,1,1
        if (v < (vmin + 0.25 * dv)):
            r = 0
            g = 4 * (v - vmin) / dv
        elif (v < (vmin + 0.5 * dv)):
            r = 0
            b = 1 + 4 * (vmin + 0.25 * dv - v) / dv
        elif (v < (vmin + 0.75 * dv)):
            r = 4 * (v - vmin - 0.5 * dv) / dv
            b = 0
        else:
            g = 1 + 4 * (vmin + 0.75 * dv - v) / dv
            b = 0
            
        img[i,j]=[r*255,g*255,b*255]

## Use Opencv
# cv2.imshow("colorMap", img)
# cv2.setWindowTitle
# cv2.waitKey(0)
        
## Use Matplotlib
plt.imshow(img)
plt.xlim([vmin, vmax])
plt.gca().set_yticklabels([])
plt.title('ColorMap')
plt.show()