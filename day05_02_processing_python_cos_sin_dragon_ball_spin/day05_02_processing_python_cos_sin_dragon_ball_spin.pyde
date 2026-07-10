#day05_02_processing_python_cos_sin_dragon_ball_spin
#想讓七龍珠轉動
def setup(): #設定的函式
    size(400, 400)
    
def draw(): #畫圖的函式
    background(0) #背景是黑色的
    for i in range(7): #七龍珠跑七次迴圈
        #a=(PI*2/7)*i+mouseX/1000.0 #滑鼠轉動是要增加角度
        a=(PI*2/7)*i+radians(frameCount)/5
        ellipse(200+150*cos(a), 200+150*sin(a), 80, 80) #畫出80*80的圓
