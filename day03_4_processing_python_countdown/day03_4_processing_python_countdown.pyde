# day03_4_processing_python_countdown
#倒數計時，先把時間印出來
def setup(): #設定的函式
    size(500, 200)#視窗大小
    
def draw(): #畫圖的函式
    background(0) #背景黑色
    textSize(150) #字體很大(150號字)
    #text("00:00", 80, 150) #測式大小、位置用的
    mm=minute() #分鐘
    ss=second() #秒鐘
    text(nf(mm,2)+":"+nf(ss,2),80, 150)
