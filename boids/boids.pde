float max_vel_mag_sq = 60;
float max_vel_mag = sqrt(max_vel_mag_sq);
float max_force = 0.3;
int dispHeight = 1000;
int dispWidth = 1900;
PVector acc = new PVector(0,0);
PVector sepAcc = new PVector(0,0);
PVector cohAcc = new PVector(0,0);
PVector aliAcc = new PVector(0,0);
PVector diff = new PVector(0,0);
float  sepScalar = 5;
float  cohScalar = 4;
float  aliScalar = 8;
float visionDiam = 60;
float protDiam = 30;
float d;
int neighbours = 0,closeNeighbours = 0;
int BoidN = 500;
Boid[] B = new Boid[BoidN];

class Boid{
  PVector pos;
  PVector vel;
  PVector acc;
  int col = int(random(50,155));
  Boid(){
    pos = new PVector(random(dispWidth),random(dispHeight));
    vel = PVector.random2D();
    vel.setMag(random(max_vel_mag));
    acc = new PVector(0,0);
  }
  void update(){
    sepAcc.set(0,0);cohAcc.set(0,0);aliAcc.set(0,0);neighbours = 0;closeNeighbours = 0; 
    for(int i=0;i<BoidN;i++){
      d = dist(pos.x,pos.y,B[i].pos.x,B[i].pos.y);
      if(d<visionDiam){
        if(d<protDiam){
          closeNeighbours++;
          diff.set(0,0);
          diff.add(pos);
          diff.sub(B[i].pos);
          //diff.div(d+1);
          diff.mult(protDiam-d);
          sepAcc.add(diff);
        }
        aliAcc.add(B[i].vel);
        cohAcc.add(B[i].pos);
        neighbours++;
      }
    }
    closeNeighbours--;
    neighbours--;
    if(closeNeighbours>0)sepAcc.div(closeNeighbours);
    sepAcc.mult(sepScalar);
    acc.add(sepAcc);
    aliAcc.sub(vel);
    cohAcc.sub(pos);
    if(neighbours>0){
      aliAcc.div(neighbours);
      cohAcc.div(neighbours);
    }
    cohAcc.sub(pos);
    cohAcc.setMag(max_vel_mag);
    aliAcc.sub(vel);
    aliAcc.mult(aliScalar);
    cohAcc.mult(cohScalar);
    acc.add(aliAcc);
    acc.add(cohAcc);
    acc.limit(max_force);
    
    vel = vel.add(acc);
    vel.limit(max_vel_mag);
    
    pos = pos.add(vel);
    if(pos.x<0){pos.x = 0;vel.x*=-1;pos.add(vel);}
    if(pos.x>dispWidth){pos.x = dispWidth;vel.x*=-1;pos.add(vel);}
    if(pos.y<0){pos.y = 0;vel.y*=-1;pos.add(vel);}
    if(pos.y>dispHeight){pos.y = dispHeight;vel.y*=-1;pos.add(vel);}
  }
  void display(){
    fill(col);
    circle(pos.x,pos.y,10);
  }
}



void setup(){
  size(1900,1000);
  for(int i=0;i<BoidN;i++){
    B[i] = new Boid();
  }
}

void draw(){
  background(0);
  for(int i=0;i<BoidN;i++){
    B[i].update();
    B[i].display();
  }
  println(frameRate);
  frameRate(60);
}
