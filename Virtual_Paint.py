import cv2
import numpy as np


frameWidth=640
frameHeight=480

cap=cv2.VideoCapture(0)#gets video from webcam
cap.set(3,frameWidth)#sets width of frame 
cap.set(4,frameHeight)#sets height of frame

cap.set(10,130)#sets brightness

myColors=[[5,107,0,19,255,255],
          [133,56,0,159,156,255],
          [57,76,0,100,255,255]]

myColorValues=[[51,153,255],          ##BGR
               [255,0,255],
               [0,255,0]]

myPoints=[] #x,y,colorId


def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in myColors:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask= cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img): 
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#RETR_EXTERNAL:finds outer contours
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)#approximate number of corner points
            x , y , w , h =cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(Points,ColorValues,img):
    for point in Points:
        cv2.circle(img,(point[0],point[1]),40,ColorValues[point[2]],cv2.FILLED)


while True:
    success,img=cap.read()
    imgResult=img.copy()
    newPoints=findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues,imgResult)

    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break