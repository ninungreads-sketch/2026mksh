#day05_01_processing_python_cos_sin_dragon_ball
#國中教sin()cos()有什麼用? A:老師大學上3D圖學，很有用
size(400, 400) #視窗大小400*400，正中心(200，200)
ellipse(200, 200, 300, 300) #圓形正中心(200，200)，園的大小300*300

for i in range(7): #七個龍珠
    a=(PI*2/7)*i #對應的角度a是1/7個圓
    ellipse(200+150*cos(a), 200+150*sin(a), 80, 80) #畫出80*80的圓
    #圓心200半徑150 x座標對應cos(a)
    #圓心200半徑150 y座標對應cos(a)
                                
