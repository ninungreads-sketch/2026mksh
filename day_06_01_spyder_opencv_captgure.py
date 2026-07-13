#day_06_01_spyder_opencv_captgure.py
#利用 chatgpt 修改
#修改自day04_07_processing_java_vedio_library_Capture_start read
import cv2

# 開啟預設攝影機
cam = cv2.VideoCapture(0) #0:第一台攝影機，1:第二台攝影機

# 設定解析度
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:  #迴圈會一直跑，直到有 break 才跳開結束
    ret, frame = cam.read()

    if not ret: #若沒有成功就離開
        break

    # 顯示影像
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1)==27:  #按 Esc 離開
        break

cam.release() #把 camera 正確關閉
cv2.destroyAllWindows() #把剛剛開啟的 openCV 視窗全部關掉