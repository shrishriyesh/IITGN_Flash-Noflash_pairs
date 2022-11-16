import cv2
import numpy as np
import NF_pairs
import bilateralfilter as bf
from matplotlib import pyplot as plt
def nothing(x):
    pass
cv2.namedWindow("Tracking")
cv2.createTrackbar("Threshold","Tracking",0,255,nothing)
imgA=cv2.imread('redA1.png',0)
imgF=cv2.imread('redF1.png',0)
imgAN=cv2.imread('redA1.png')
imgFN=cv2.imread('redF1.png')
imgFL=cv2.cvtColor(imgFN,cv2.COLOR_BGR2LAB)
L,A,B=cv2.split(imgFL)
_,th2=cv2.threshold(L,242,255,cv2.THRESH_BINARY)
ero2=cv2.erode(th2,(3,3),iterations=2)
dil2=cv2.dilate(ero2,(3,3),iterations=2)
#cv2.imshow('light',dil2)
print(dil2)
AN=np.array(imgA,dtype='uint8')
FN=np.array(imgF,dtype='uint8')
diff=FN-AN;
joint=bf.bilateralfilter(imgAN,imgFN, 1, 25.5)
while True:
    val= cv2.getTrackbarPos("Threshold", "Tracking")
    _,res=cv2.threshold(diff,val,255,cv2.THRESH_BINARY_INV)
    #print(res)
    #cv2.imshow('thresh',res)
    ero=cv2.erode(res,(3,3),iterations=2)
    dil=cv2.dilate(ero,(3,3),iterations=2)
    mask=cv2.bitwise_or(dil2,dil)
    finalmask=cv2.blur(mask,(3,3))
    cv2.imshow('flshshadows.png',dil)
    cv2.imshow('final.png',finalmask)
    cv2.imshow('JBF.png',joint)
    cv2.imwrite('flshshadows.png', dil)
    cv2.imwrite('final.png', finalmask)
    cv2.imwrite('JBF.png', joint)
    cv2.waitKey(1)
