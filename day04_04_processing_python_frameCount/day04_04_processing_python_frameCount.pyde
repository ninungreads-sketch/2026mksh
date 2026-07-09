#day04_04_processing_python_frameCount
#希望瞭解day04_03的 frameCount 是什麼意思
def setup():
    size(400, 400)
    #frameRate(5)#等一下會刪掉
#如果想知道現在是第幾次執行void draw()要用t來數
t = 1    #第一行宣告t變數
def draw():
    global t #第二行要認識外面的t
    
    background(0)
    textSize(100)
    textAlign(CENTER, CENTER)
    text(frameCount, 200, 100)
    
    text(t, 200, 200) #第三行試著畫出t的值
    t += 1   #第四行每次結束時t會+1
    
    text(frameCount//60, 200, 300) #每秒60次所以//6會變秒
