# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:40:14 2026

@author: user
"""

#day08_02_spyder_opencv_face_detect
#prompt:希望程式能偵測到人臉，用線條、圖形等把臉框起來，請問此程式要再做甚麼修改?
import cv2

print(cv2.__version__)

# 載入人臉偵測模型
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 開啟攝影機
cap = cv2.VideoCapture(0)

# 檢查是否成功開啟
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

while True:

    # 讀取一張畫面
    ret, frame = cap.read()

    if not ret:
        print("讀取失敗")
        break

    # ===== 新增：轉成灰階 =====
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ===== 新增：偵測人臉 =====
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )

    # ===== 新增：畫方框 =====
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,
                      (x, y),
                      (x+w, y+h),
                      (0,255,0),
                      2)

    # 顯示畫面
    cv2.imshow("Webcam", frame)

    # ESC 離開
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 關閉
cap.release()
cv2.destroyAllWindows()