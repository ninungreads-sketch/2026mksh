//day04_06_processing_java_sound_library_duration_bar
import processing.sound.*; //使用Sound外掛
float T;
void setup(){ //設定的函式
  size(400, 50); //視窗大小
//記得把sound_files目錄中的music.mp3拉到程式中
  SoundFile music=new SoundFile(this, "music.mp3");
  music.play(); //播放
  T=music.duration();
}
void draw(){
  background(255,255,242);
  fill(255, 0, 0);
  rect(0, 0, 400*(frameCount/60.00)/T, 50);
}
