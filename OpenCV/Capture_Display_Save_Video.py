import cv2 as cv
import sys

cap = cv.VideoCapture(0)
# start capturing if camera opened else exit
if not cap.isOpened():
    sys.exit('Cannot open Camera')

# output video file specs
filename = './recorded.avi'
fourcc = cv.VideoWriter_fourcc(*'avc1')
fps = 30.0
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
fsize = (int(height), int(width))

out = cv.VideoWriter(filename, fourcc, fps, fsize)

while True:
    ret, frame = cap.read()
    # read frame by frame along with a return value (which is true if frame is read successfully)
    if not ret:
        print("Cannot read Frame.")
        break
    
    # convert frame to grayscale  
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # flip image horizontally
    img = cv.flip(gray_img, 0)
    
    # write current frame in output video
    out.write(img)
    
    # display video till exit
    cv.imshow('Grayscale Video', img)
    if cv.waitKey(1) == ord('q'):
        break

# release acquired memory
cap.release()
out.release()
cv.destroyAllWindows()
