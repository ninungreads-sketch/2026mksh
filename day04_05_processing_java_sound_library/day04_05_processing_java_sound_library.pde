//day04_05_processing_java_sound_library
import processing.sound.*; //使用Sound外掛

void setup(){ //設定的函式
  size(400, 400); //視窗大小
//記得把sound_files目錄中的music.mp3拉到程式中
  SoundFile music=new SoundFile(this, "music.mp3");
  music.play(); //播放
}
void draw(){
  background(#CCCCFF);
}
