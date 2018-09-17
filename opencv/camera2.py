import cv2

cam = cv2.VideoCapture(0)
print("resolution: ", cam.get(3), cam.get(4))
cam.set(3, 320)
cam.set(4, 240)

while True:
    ret,im = cam.read()
    if ret:
        cv2.imshow('video test',im)
        
        key = cv2.waitKey(10)
        if key == 120: # ascii code for letter 'x'
            break
        if key == ord(' '):
            cv2.imwrite('capture.jpg',im)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('cap_gray.jpg', gray)
            
cam.release()
cv2.destroyAllWindows()
