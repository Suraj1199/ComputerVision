import cv2 as cv
import sys

img_src_path = '/Users/surajsingh/Downloads/landscape.jpeg'

img = cv.imread(img_src_path)

if img is None:
    sys.exit("Could not read file.")

cv.imshow("Display Window", img)
k = cv.waitKey(0)

img_save_path = './'
if k == ord('s'):
    cv.imwrite(img_save_path + 'landscape.jpeg', img)