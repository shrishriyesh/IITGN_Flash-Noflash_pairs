import cv2
from matplotlib import pyplot as plt
import numpy as np
#DETAILS
def main():
    A=cv2.imread('redA1.png',0)
    F=cv2.imread('redF1.png',0)
    AN=np.array(A,dtype='uint8')
    FN=np.array(F,dtype='uint8')
    Abil=cv2.bilateralFilter(A,5,3,0.2)
    Fbil=cv2.bilateralFilter(F,5,3,0.2)
    FbilN=np.array(Fbil,dtype='uint8')
    cv2.imwrite('Abil.jpg',Abil)
    details=FN/FbilN
    Fe1=(FN+0.02)
    Fe2=(FbilN+0.02)
    detailse=Fe1/Fe2
    max=detailse.max()
    new=detailse/max
    new=new*255
    new1=cv2.cvtColor(new,cv2.COLOR_GRAY2BGR)
    min=new.min()
    print(min)
    print(new)
    print(detailse)
    d1=cv2.convertScaleAbs(details)
    d2=cv2.normalize(d1,None,255,0,cv2.NORM_MINMAX,cv2.CV_8UC1)
    cv2.imwrite('test-1.png',details)
    #return details
    cv2.imwrite('imagenew.jpg',new)
    titles=['Ambient','Flash','Ambient bilateral','Flash bilateral','Details without e','Details with e']
    images=[A,F,Abil,Fbil,details,new]
    for i in range(6):
       plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
    plt.show()
    cv2.waitKey(1)
main()
