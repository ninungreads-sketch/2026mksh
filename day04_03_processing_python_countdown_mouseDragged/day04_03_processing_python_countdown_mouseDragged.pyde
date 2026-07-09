#day04_03_processing_python_countdown_mouseDragged
#修改自day04_02_processing_python_countdown_start_??
#希望 mouse 右鍵，會開始、暫停
def setup():
    size(400, 400)

t=10
start = False
def draw():
    global t
    background(0)
    textSize(300)
    textAlign(CENTER, CENTER)
    text(t, 200, 200)
    if start and frameCount%60==0 and t>0:t-=1
    
def mousePressed():
    global start
    if mouseButton ==RIGHT: start= not start #start =True
    
def mouseDragged(): #mouse往上下滑
    global t #會修改t的值
    t-=(mouseY-pmouseY)/4 #向量的差
    t=max(0, min(59, t))  #限制在0～59之間   
