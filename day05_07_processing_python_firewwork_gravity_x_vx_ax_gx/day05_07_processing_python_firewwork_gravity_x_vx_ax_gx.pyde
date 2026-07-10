#day05_07_processing_python_firewwork_gravity_x_vx_ax_gx
#物理大師牛頓 F=ma 位置、速度、加速度
def setup():
    size(500, 500)
    
x, y=0, 250   #位置
vx, vy=10, -10  #速度
gx, gy=0, 0.98  #加速度 (9.8 老師縮小成0.98)
def draw():   
    global x, y, vx, vy   #要修改外面的global全域變數
    #background(0)
    stroke(255, 255, 0)
    ellipse(x, y, 10, 10)
    x+=vx #位置會隨速度改變
    y+=vy
    vx+=gx #速度會隨加速度改變
    vy+=gy
