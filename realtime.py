from tkinter.messagebox import RETRY
import cv2
import numpy as np
import math
#from statistics import mean
import time

def main():
    for i in range(1):
        print("\r{0}".format(i), end="")
        time.sleep(0.01)
    print("")







cap = cv2.VideoCapture(0)
while True:
    #カメラからの画像取得
    ret, frame = cap.read()
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    #カメラの画像の出力
    #cv2.imshow('frame' , frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("1nega.png", gray)
    #reversed_gray = cv2.bitwise_not(gray) これよりも下のCannyのほうが良さげ
    #cv2.imwrite("gray.png", reversed_gray)
    edges = cv2.Canny(gray,90,450,apertureSize = 3)
    #cv2.imwrite("2canny.png", edges)
    right=10 #degで指定
    left=-10 #degで指定
    a=np.deg2rad(right)
    b=np.deg2rad(left)



    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=150, minLineLength=300, maxLineGap=70)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        rad = math.atan2(y2 - y1, x2 - x1)
        deg = np.rad2deg(rad)
        

        if (a < rad) or (rad < b ):
            # 横縞以外の邪魔な線
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2,lineType=cv2.LINE_AA)
        else:
            # 横縞
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2,lineType=cv2.LINE_AA)
            
    #cv2.imwrite("result.jpg", frame)
    

    #print(deg)
    #if __name__ == "__main__":
    #    main()

    #繰り返し分から抜けるためのif文 ESCkey
    key =cv2.waitKey(10)
    if key == 27:
        break
    cv2.imshow('frame' , frame)
    mea = np.mean(deg) 
    #print(mea) 
    print(mea,end="\r")

#メモリを解放して終了するためのコマンド
cap.release()
cv2.destroyAllWindows()

#ret, frame = cap.read()
#cv2.imwrite("カメラ画像.jpg", frame)
#cv2.imshow('camera' , frame)
#print(ret)

"""

img = cv2.imread("IMG_4122.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("1nega.png", gray)
#reversed_gray = cv2.bitwise_not(gray) これよりも下のCannyのほうが良さげ
#cv2.imwrite("gray.png", reversed_gray)
edges = cv2.Canny(gray,90,450,apertureSize = 3)
cv2.imwrite("2canny.png", edges)

right=10 #degで指定
left=-10 #degで指定
a=np.deg2rad(right)
b=np.deg2rad(left)

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=150, minLineLength=300, maxLineGap=70)
for line in lines:
    x1, y1, x2, y2 = line[0]
    rad = math.atan2(y2 - y1, x2 - x1)
    deg = np.rad2deg(rad)

    if (a < rad) or (rad < b ):
        # 横縞以外の邪魔な線
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2,lineType=cv2.LINE_AA)
    else:
        # 横縞
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2,lineType=cv2.LINE_AA)

cv2.imwrite("result.jpg", img)


"""