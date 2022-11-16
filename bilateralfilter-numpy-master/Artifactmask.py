import cv2
import numpy as np
imgA=cv2.imread('redA1.png')
imgF=cv2.imread('redF1.png')
#cv2.imshow('frame',imgA)
#cv2.imshow('frame2',imgF)
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# l_b = np.array([164, 174, 77])
# u_b = np.array([178, 255, 255])
# mask = cv2.inRange(hsv, l_b, u_b)
# res = cv2.bitwise_and(frame, frame, mask=mask)
# cv2.imshow("frame", frame)
# cv2.imshow("mask", mask)
# cv2.imshow('res', res)
img1=cv2.cvtColor(imgA,cv2.COLOR_BGR2YCrCb)
img2=cv2.cvtColor(imgF,cv2.COLOR_BGR2YCrCb)
YA,CrA,CbA=cv2.split(img1)
YF,CrF,CbF=cv2.split(img2)
R=CrF-CrA
_,Rn=cv2.threshold(R,153,255,cv2.THRESH_BINARY)
_,Ay=cv2.threshold(YA,0,153,cv2.THRESH_BINARY)
AandR=cv2.bitwise_and(Ay,Rn)
Res=cv2.bitwise_and(imgF,imgF,mask=AandR)
mean=np.mean(R)
std=np.std(R)
print(R)
print(mean)
print(std)
print(AandR)
cv2.imshow("frame",AandR)
print(Ay)
print(Rn)
cv2.imshow('frame3',Res)
cv2.waitKey(0)