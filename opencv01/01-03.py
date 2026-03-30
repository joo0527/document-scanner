import cv2
import sys

img = cv2.imread("lena.jpg")

if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

#특정지점 색상 파악
blue = img[100,100,0]
green = img[100,100,1]
red = img[100,100,2]

print("100행 100열의 색상:", blue, green, red)

#특정 지점의 색상 변경
img[10:100,10:100] = [0,0,0]

cv2.imshow("Lena.new",img)

#키 입력 기다리기
cv2.waitKey(0)
cv2.destroyAllWindows() #모든 opencv 창 끄기

