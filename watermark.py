import cv2 as cv
import numpy as np

logo = cv.imread("computer vision\logo.jpg")
h_logo,w_logo,_=logo.shape

img= cv.imread("computer vision\cat.jpg")
h_img,w_img,_=img.shape
center_y= int(h_img/2)
center_x= int(w_img/2)

top_y= center_y - int(h_logo/2)   #top left point
top_x= center_x - int(w_logo/2)

btm_y = top_y + h_logo    #bottom right point
btm_x = top_x + w_logo

roi=img[top_y:btm_y,top_x:btm_x]

result=cv.addWeighted(roi,1,logo,0.5,0)

img[top_y:btm_y,top_x:btm_x]=result


cv.imshow("img", img)
cv.waitKey(0)
# print(top_y,top_x)



