# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:03:14 2026

@author: user
"""
# day08_03_spyder_opencv_face_detect_smooth
#prompt: face detect 出來的人臉有點抖動，請問要如何修改成沒有抖動的版本?

import cv2

print("OpenCV Version:", cv2.__version__)

# 載入人臉分類器
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 開啟攝影機
cap = cv2.VideoCapture(0)

# 檢查攝影機
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

# -------------------------
# 前一幀的人臉座標(平滑化用)
# -------------------------
prev_x = 0
prev_y = 0
prev_w = 0
prev_h = 0

while True:

    # 讀取畫面
    ret, frame = cap.read()

    if not ret:
        print("讀取失敗")
        break

    # 灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 人臉偵測
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=6,
        minSize=(80, 80)
    )

    # 若有偵測到人臉
    if len(faces) > 0:

        # 只取最大的那張臉
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

        # 第一張畫面
        if prev_w == 0:
            smooth_x = x
            smooth_y = y
            smooth_w = w
            smooth_h = h
        else:
            # ========= 平滑化 =========
            alpha = 0.7      # 越大越穩，0.6~0.8皆可

            smooth_x = int(alpha * prev_x + (1 - alpha) * x)
            smooth_y = int(alpha * prev_y + (1 - alpha) * y)
            smooth_w = int(alpha * prev_w + (1 - alpha) * w)
            smooth_h = int(alpha * prev_h + (1 - alpha) * h)

        # 更新上一幀資料
        prev_x = smooth_x
        prev_y = smooth_y
        prev_w = smooth_w
        prev_h = smooth_h

        # 畫方框
        cv2.rectangle(
            frame,
            (smooth_x, smooth_y),
            (smooth_x + smooth_w, smooth_y + smooth_h),
            (0, 255, 0),
            2
        )

        # 顯示文字
        cv2.putText(
            frame,
            "Face",
            (smooth_x, smooth_y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # 顯示畫面
    cv2.imshow("Face Detection", frame)

    # ESC 離開
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 關閉攝影機
cap.release()
cv2.destroyAllWindows()