import cv2 
import numpy as np
img=cv2.imread("sun.jpg")
cv2.imwrite("sun.png",img)
src = cv2.imread("sun.png", 0)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,1,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)
cv2.imwrite("test.png", dst)


