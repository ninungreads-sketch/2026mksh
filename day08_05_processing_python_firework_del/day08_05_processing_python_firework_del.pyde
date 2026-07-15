# day08_05_processing_python_firework_del
# 想了解 del 的意思 day07_07_processing_python_firework_life_random

a = [10, 20, 30, 40] #空白的陣列，裡面是空的

def setup():
    size(600, 100)
    frameRate(1) #每秒畫 draw() 1 次
    
def draw():
    background(0) # 背景黑色
    # for i in range(len(a)):
    for i in range(len(a)-1, -1, -1):
        fill(255) # 白色的方塊
        rect(i*80, 0, 80, 80)
        fill(255, 0, 0) #紅色的字
        text(a[i], i*80+40, 40)
        a[i]-=1 #數值慢慢變少
        if a[i] < 0: del a[i] # 把變成0的方塊刪掉
    
def mousePressed(): # mouse 每按下一次就增加一格
    a.append( int(random(5, 30))) # 用append() 加上一格的數值
