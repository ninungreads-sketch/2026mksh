#day_06_04_processing_python_firework_mousePressed_many
#修改自day_06_03_processing_python_firework_gravity_20
#想做出有互動的煙火，而且mouse可以連續點很多次
def setup():
    size(500, 500)
    
x, y = [], [] #一開始的座標
vx, vy = [], [] #一開始也沒速度
gx, gy = 0, 0.0098 #加速度
N = 0 #現在有幾個煙火?

def draw():
    background(0)
    ellipse(mouseX, mouseY, 10, 10) 
    for i in range(N):
        ellipse(x[i], y[i], 10, 10)
        x[i]+=vx[i]
        y[i]+=vy[i]
        vx[i]+=gx
        vy[i]+=gy
    
def mousePressed(): #mouse 按下去要射出花火
    global x, y, vx, vy, N #要去修改外面的變數
    x+=[mouseX]*20
    y+=[mouseY]*20
    vx+=[2*cos(PI*2/20*i) for i in range(20)]
    vy+=[2*sin(PI*2/20*i) for i in range(20)]
    N += 20
