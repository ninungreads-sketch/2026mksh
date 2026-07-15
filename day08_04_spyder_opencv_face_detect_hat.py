# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:18:08 2026

@author: user
"""

#day08_04_spyder_opencv_face_detect_hat

import cv2
import numpy as np

print("OpenCV Version:", cv2.__version__)

# -----------------------------
# 載入人臉模型
# -----------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# -----------------------------
# 載入帽子(PNG透明背景)
# -----------------------------
hat = cv2.imread("hat.png", cv2.IMREAD_UNCHANGED)

if hat is None:
    print("找不到 hat.png")
    exit()

# -----------------------------
# 開啟攝影機
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

# 平滑化參數
prev_x = prev_y = prev_w = prev_h = 0
alpha = 0.7

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=6,
        minSize=(80, 80)
    )

    if len(faces) > 0:

        # 只取最大的臉
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

        # -------------------------
        # 平滑化
        # -------------------------
        if prev_w != 0:
            x = int(alpha * prev_x + (1-alpha) * x)
            y = int(alpha * prev_y + (1-alpha) * y)
            w = int(alpha * prev_w + (1-alpha) * w)
            h = int(alpha * prev_h + (1-alpha) * h)

        prev_x = x
        prev_y = y
        prev_w = w
        prev_h = h

        # -------------------------
        # 畫人臉框
        # -------------------------
        cv2.rectangle(frame,
                      (x, y),
                      (x+w, y+h),
                      (0,255,0),
                      2)

        # -------------------------
        # 調整帽子大小
        # -------------------------
        hat_width = int(w * 1.4)

        ratio = hat.shape[0] / hat.shape[1]
        hat_height = int(hat_width * ratio)

        hat_resize = cv2.resize(
            hat,
            (hat_width, hat_height)
        )

        # -------------------------
        # 帽子位置
        # -------------------------
        hat_x = x - int((hat_width - w)/2)
        hat_y = y - hat_height + 25

        # -------------------------
        # 邊界檢查
        # -------------------------
        if hat_x >= 0 and hat_y >= 0 and \
           hat_x + hat_width <= frame.shape[1] and \
           hat_y + hat_height <= frame.shape[0]:

            # RGB
            hat_rgb = hat_resize[:, :, :3]

            # Alpha
            alpha_mask = hat_resize[:, :, 3] / 255.0

            # ROI
            roi = frame[
                hat_y:hat_y+hat_height,
                hat_x:hat_x+hat_width
            ]

            # Alpha Blend
            for c in range(3):
                roi[:, :, c] = (
                    alpha_mask * hat_rgb[:, :, c] +
                    (1-alpha_mask) * roi[:, :, c]
                )

            frame[
                hat_y:hat_y+hat_height,
                hat_x:hat_x+hat_width
            ] = roi

    cv2.imshow("Face + Hat", frame)

    # ESC 離開
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()