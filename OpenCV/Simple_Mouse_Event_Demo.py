import numpy as np
import cv2 as cv
import sys

# create black image
img = np.zeros((512, 512, 3), np.uint8)

# Create mouse call back function
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 50, (0, 0, 255), -1)

# create window and bind function
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while True:
    cv.imshow('image', img)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
