import cv2
import numpy as np
import math
img = cv2.imread("IMG_4122.JPG")
#xyxy to yyxx 
img1 = img[649:1725,1281:4032]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("1nega.png", gray)
#reversed_gray = cv2.bitwise_not(gray) これよりも下のCannyのほうが良さげ
#cv2.imwrite("gray.png", reversed_gray)
edges = cv2.Canny(gray,90,450,apertureSize = 3)
cv2.imwrite("2canny.png", edges)

right=10
left=-10
a=np.deg2rad(right)
b=np.deg2rad(left)
#print(a,b)   

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=150, minLineLength=300, maxLineGap=70)
for line in lines:
    x1, y1, x2, y2 = line[0]
    rad = math.atan2(y2 - y1, x2 - x1)
    deg = np.rad2deg(rad)
    with open('test.txt', 'a') as f:
        content = str(deg)
        f.write(content + '\n')
    with open('test2.txt', 'a') as f:
        content2 = str(line)
        f.write(content2 + '\n')
    if (a < rad) or (rad < b ):
        # 横縞
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2,lineType=cv2.LINE_AA)
    else:
        # 横縞以外の邪魔な線
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2,lineType=cv2.LINE_AA)
cv2.imwrite("result.jpg", img)

