//day01_processing_java_painter_line_mouseX_mouseY_pmouseX_pmouseY
//簡單的小畫家(Painter)
void setup(){ //設定的函式
  size(500,500);//視窗500*500
}
void draw(){ //畫圖的函式
  //如果 mouse按下去
  if (mousePressed)
    line(mouseX, mouseY, pmouseX,pmouseY );
    //畫線 從 mouse 座標到pmouse座標
}
