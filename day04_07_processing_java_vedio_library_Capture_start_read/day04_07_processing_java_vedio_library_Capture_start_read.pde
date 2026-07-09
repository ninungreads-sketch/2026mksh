//day04_07_processing_java_vedio_library_Capture_start read
import processing.video.*;
Capture cam;

void setup(){
  size(640, 480);
  cam=new Capture(this, 640, 480);
  cam.start();
}
void draw(){
  if(cam.available())cam.read();
  image(cam, 0, 0);
}
  
