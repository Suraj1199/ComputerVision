import numpy as np
import cv2 as cv
import sys

img = np.zeros((512, 512, 3), np.uint8)

# Draw line
lpt1 = (40, 40)
lpt2 = (240, 120)
color = (255, 0, 0)
cv.line(img, lpt1, lpt2, color, 5) 

# Draw rectangle
top_left = (100, 120)
bottom_right = (200, 220)
color = (0, 255, 0)
cv.rectangle(img, top_left, bottom_right, color, 2) 

# Draw Circle
center = (340, 340)
radius = 20
color = (0, 0, 255)
cv.circle(img, center, radius, color, -1) # thickness -1 for solid fill 

# draw polygons
n = 5
pts = np.array([20, 40, 30, 20, 40, 20, 50, 40, 35, 60]).reshape(n, 1, 2)
is_closed= True
color = (0, 0, 128)
cv.polylines(img, [pts], is_closed, color, 3)

# Add Text
text = 'OpenCV'
pos = (220, 30)
font = cv.FONT_HERSHEY_SIMPLEX
scale = 1
color = (255, 255, 255)
linetype = cv.LINE_AA
cv.putText(img, text, pos, font, scale, color, 1, linetype)

cv.imshow('image', img)
cv.waitKey(0)

cv.destroyAllWindows()
