import cv2
import numpy as np

# 흰색 배경 생성 (512x512)
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)

# 그리기
cv2.line(canvas, (50, 50), (450, 450), (0, 0, 255), 5)
cv2.line(canvas, (450, 50), (50, 450), (0, 0, 255), 5)          
cv2.rectangle(canvas,(50,50), (450,450), (0,255,0),-1)
cv2.circle(canvas,(450,50),50,(50,450),3)
cv2.putText(canvas, "Hello!", (20,40),cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),1)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()