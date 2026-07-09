#day04_00 # 初始設定剩餘時間為 10 秒 (可以是任意設定的值)
remain = 10 
is_run = False  # 是否開始倒數的開關：True(開始), False(暫停)
last_m = 0      # 紀錄上一次扣秒的時間點
def setup():
    size(500, 300) # 稍微加高視窗，留位置放按鈕
    textAlign(CENTER, CENTER) # 讓文字全部置中對齊
def draw():
    global remain, last_m
    background(0) # 背景黑色
    # --- 1. 倒數計時邏輯 ---
    if is_run and remain > 0:  # 如果現在的時間比上一次紀錄的時間多了 1000 毫秒(1秒)
        if millis() - last_m >= 1000:
            remain -= 1       # 剩餘秒數減 1
            last_m = millis() # 重新紀錄時間點
    mm = remain // 60 # 計算分鐘     mm = remain // 60 # 計算分鐘 
    ss = remain % 60  # 計算秒數
    textSize(120)
    fill(255) # 白色字
    # nf(數字, 2) 可以把個位數補零，變成 05:09 的好看格式
    text(nf(mm, 2) + ":" + nf(ss, 2), width/2, 100)  # --- 3. 畫出「開始/暫停」按鈕 與 提示 ---
    textSize(20)
    if not is_run:
        fill(100, 255, 100) # 暫停中顯示綠色
        rect(180, 220, 140, 40, 5)
        fill(0)
        text("START", width/2, 240)        
        # 提示左右滑動調整時間
        fill(150)
        text("← 左右滑動畫面可調整時間 →", width/2, 180)
    else:
        fill(255, 100, 100) # 執行中顯示紅色
        rect(180, 220, 140, 40, 5)
        fill(0)
        text("PAUSE", width/2, 240)
def mousePressed():
    global is_run, last_m  # 檢查是否點擊到下方的按鈕範圍 (x: 180~320, y: 220~260)
    if 180 <= mouseX <= 320 and 220 <= mouseY <= 260:
        is_run = not is_run # 切換開始/暫停
        last_m = millis()   # 按下的那一刻重新校準計時器
def mouseDragged():
    global remain  # 只有在「暫停狀態」下，才允許滑動修改時間
    if not is_run:
        if mouseX - pmouseX > 0:# mouseX - pmouseX 代表滑鼠「這瞬間移動的左右距離」# 往右滑增加秒數，往左滑減少秒數
            remain += 1
        elif mouseX - pmouseX < 0:
            remain = max(0, remain - 1) # 用 max 確保時間不會減到變成負數！
