# import cv2
# import numpy as np

# drawing = False

# # 흰색 배경 생성 (512x512)
# canvas = np.ones((512, 512, 3), dtype=np.uint8) * 255

# def mouse_callback(event, x, y, flags, param):
#     global drawing

#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         cv2.circle(canvas,(x,y),2,(0,0,255),-1)
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             cv2.circle(canvas,(x,y),2,(0,0,255),-1)
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False

# cv2.namedWindow("draw")
# cv2.setMouseCallback("draw",mouse_callback)

# while True:
#     if cv2.waitKey(1) & 0XFF == ord('q'):
#         break

# cv2.destroyAllWindows()

import cv2
import numpy as np

# 그리기 상태를 저장할 변수 (전역 변수)
drawing = False # 마우스가 눌려 있는 상태인지 확인

def mouse_callback(event, x, y, flags, param):
    global drawing

    # 1. 마우스를 누르면 그리기 시작
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 2, (0, 0, 0), -1) # 클릭 지점에 점 찍기

    # 2. 마우스를 누른 채 움직이면 연속해서 그리기
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # 원을 조밀하게 그려서 선처럼 보이게 함
            cv2.circle(img, (x, y), 2, (0, 0, 0), -1)

    # 3. 마우스를 떼면 그리기 종료
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# 빈 하얀색 캔버스 생성 (512x512, 3채널 컬러)
img = np.ones((512, 512, 3), dtype=np.uint8) * 255

cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', mouse_callback)

while True:
    cv2.imshow('Paint', img)
    if cv2.getWindowProperty('Paint', cv2.WND_PROP_VISIBLE) < 1:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        img[:] = 255 
    
    # 'q'를 누르면 종료
    elif key == ord('q'):
        break

cv2.destroyAllWindows()