#day05_05_processing_python_firewwork
#花火節的煙火
def setup(): #設定的函式
    size(500, 500) #視窗500*500 中心(250, 250)
def draw(): #畫圖的函式
    background(255, 255, 242) #背景淡黃色
    for i in range(20):
        R = 20 + mouseX  #花火的爆炸半徑是20+mouseX
        a = (PI*2 / 20 )*i #圓/7*i會有不同角度
        line(250, 250, 250+R*cos(a), 250+R*sin(a))
        #黑色的線從中心(250, 250)往半徑大圓外面射出去
