# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#day08_01_spyder_opencv_webcam
#prompt : 我們想在 spyder 裡面使用opencv讓webcam視訊鏡頭的畫面，即時更新處，要做哪些步驟?有哪些可能卡住的地方?
#可以改成按 esc 鍵來退出opencv程式嗎?改掉原本哪幾行程式呢?

import cv2
print(cv2.__version__)

import cv2

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

    # 顯示畫面
    cv2.imshow("Webcam", frame)

    # 按 q 離開
    if cv2.waitKey(1) == 27:
        break
# 關閉
cap.release()
cv2.destroyAllWindows()
