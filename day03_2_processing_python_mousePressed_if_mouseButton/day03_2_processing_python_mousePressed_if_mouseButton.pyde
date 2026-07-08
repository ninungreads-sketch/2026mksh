#day03_2_processing_python_mousePressed_if_mouseButton
#修改自 day03_1_processing_python_PFont_textSize_text
a=[99, 88, 77, 66, 55]

def mousePressed(): # mouse 按下去，對應的函式
    i=mouseX//100
    if mouseButton==LEFT:a[i]+=1 #按左鍵，a[i]加1
    else: a[mouseX//100]-=1 #按右鍵，a[i]減1
    
def setup(): #設定的函式
    size(500, 100) #視窗大小500*100
    
def draw(): #畫圖的函式
    for i in range(5):#迴圈跑五次
        fill(255, 255, 242) #淡黃色、米色
        rect(i*100, 0, 100, 100) #畫格子
        fill(255, 0, 0) #紅色的字
        textSize(60)
        text(a[i], i*100, 80) #畫出a[i]
