#in this program i am trying to detect a rectangle and return its coordinate so that
#drone gets a coordinate to go on

import cv2
import numpy as np
def nothing(x):
    pass

cam = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H","Trackbars",0,180,nothing)
cv2.createTrackbar("L-S","Trackbars",66,255,nothing)
cv2.createTrackbar("L-V","Trackbars",134,255,nothing)
cv2.createTrackbar("U-H","Trackbars",180,180,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",243,255,nothing)

while(True):
    _,frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S","Trackbars")
    l_v = cv2.getTrackbarPos("L-V","Trackbars")
    u_h = cv2.getTrackbarPos("U-H","Trackbars")
    u_s = cv2.getTrackbarPos("U-S","Trackbars")
    u_v = cv2.getTrackbarPos("U-V","Trackbars")

    lower_red = np.array([l_h,l_s,l_v])
    upper_red = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    kernal = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernal)
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>400:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            M = cv2.moments(box)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #xc = int((x1+x2)/2)
            #yc = int((y1+y2)/2)
            #print(xc,yc)
            cv2.circle(frame,(cx,cy),5,(0,255,0),-1)
            #cv2.putText(frame,"pt1",(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
            #cv2.putText(frame,"pt2",(x2,y2),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
            img = cv2.drawContours(frame,[box],0,(0,0,0),3)
    cv2.imshow("minArearect",frame)
    if cv2.waitKey(1)==27:
        break
cam.release()
cv2.destroyAllWindows()
        
