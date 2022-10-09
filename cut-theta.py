import cv2
import numpy as np
import math


    
img_origin = cv2.imread("IMG_4122.JPG")
#xyxy to yyxx 
img = img_origin[649:1725,1281:4032]


def txtmake():
    with open('deg.txt', 'a') as f:
        content = str(deg)
        f.write(content + '\n')
    with open('line.txt', 'a') as f:
        content2 = str(line)
        f.write(content2 + '\n')
        #print("txtOpen")


with open('deg.txt', 'w') as f:
    print("text clean")
with open('line.txt', 'w') as f:
    print("text clean")
with open('sort_deg.txt', 'w') as f:
    print("text clean")

#白黒のネガにする
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("1nega.png", gray)

edges = cv2.Canny(gray,90,450,apertureSize = 3)
#cv2.imwrite("2canny.png", edges)

right=10
left=-10
a=np.deg2rad(right)
b=np.deg2rad(left)
print(a,b)   

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=150, minLineLength=300, maxLineGap=70)
for line in lines:
    x1, y1, x2, y2 = line[0]
    rad = math.atan2(y2 - y1, x2 - x1)
    deg = np.rad2deg(rad)
    if(deg<0):
        deg=-deg

    if (a < rad) or (rad < b ):
        # 横縞以外の邪魔な線
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2,lineType=cv2.LINE_AA)
    else:
        # 横縞
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2,lineType=cv2.LINE_AA)
        txtmake()


cv2.imwrite("result.jpg", img)

with open('deg.txt', 'r') as f:
    deg = f.readlines()
    #print(deg)
    deg.sort()
    with open('sort_deg.txt', 'a') as f:
        #content = str(deg)
        #f.write(content)
        for line in deg:
            #print(line.rstrip('\n'))
            f.write(line)