//day02_1_processing_java_PImage_loadImage_image
size(600, 300);
PImage img; //宣告圖片的變數
//上望找圖片，存檔 penghu.jpg 放桌面或下載，在「拉到程式裡」
//img=loadImage("...檔名等一下放這"); //讀入圖片
img=loadImage("penghu.jpg"); //讀入圖片
image(img, 0, 0, 600, 300); //畫出圖片，在(0,0) 大小600*300
