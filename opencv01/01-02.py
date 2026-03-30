import cv2
import sys

img = cv2.imread("lena.jpg")

if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

cv2.imshow("Lena.new",img)

#키 입력 기다리기
cv2.waitKey(0)
cv2.destroyAllWindows() #모든 opencv 창 끄기

