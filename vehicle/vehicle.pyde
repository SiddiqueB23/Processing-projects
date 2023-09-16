def setup():
    size(500, 500)
    background(255)    
    # noLoop()
    
def draw():
    background(255)
    t = PVector(mouseX,mouseY)
    fill(0)
    circle(t.x,t.y,20)
    
    # line(200,200,400,300)
    # projP = vectProjPoint(PVector(200,200),PVector(400,300),t)
    # circle(projP.x,projP.y,20)
    
    # v.seek(PVector(500,500))
    # v1.seek(t)
    # v1.flee(v2)
    # v1.update()
    # v1.display()
    # v2.pursue(v1)
    # v2.arrive(t)
    # v2.seek(t)
    # v2.update()
    # v2.display()
    # v3.wander()
    # v3.update()
    # v3.display()
    
    p.display()
    projP = vectProjPoint(p.p1,p.p2,t)
    circle(projP.x,projP.y,5)
    
    v4.followPath(p)
    v4.update()
    v4.display()
    
    print(frameCount)
    
def mouseClicked():
    background(255)
    v1.pos = PVector(random(250),random(250))
    v4.vel=PVector.random2D()*4
    
    
def vectProjPoint(l1,l2,p): # vector projection of a on b
    a = p-l1
    b = l2-l1
    b.normalize()
    b.setMag(a.dot(b))
    b.add(l1)
    return(b)

    
class Path():
    def __init__(self,p1=PVector(0,250),p2=PVector(500,250)):
        self.p1, self.p2 = p1,p2
        self.radius = 30
        
    def display(self):        
        stroke(200)
        strokeWeight(self.radius*2)
        line(self.p1.x,self.p1.y,self.p2.x,self.p2.y)
        strokeWeight(1)
        stroke(0)
        line(self.p1.x,self.p1.y,self.p2.x,self.p2.y)

    
class Vehicle():
    def __init__(self, pos=PVector(0,0), vel=PVector(0,0),acc=PVector(0,0),ang=0,s=10,maxSpeed=5,maxForce=0.5):
        self.pos, self.vel, self.acc, self.ang, self.s = PVector.copy(pos),PVector.copy(vel),PVector.copy(acc),ang,s
        self.maxSpeed,self.maxForce = maxSpeed, maxForce
        self.steerForce = PVector(0,0)
        self.wanderTheta = PI/2
        self.path = []
    
    # def applyForce(self,force):
    #     self.acc.add(force)
    #     print(self.acc.x,self.acc.y)
        
    def seek(self,target):
        self.target = target
        self.steerForce = PVector.sub(self.target,self.pos)        
        self.steerForce.normalize()
        self.steerForce.setMag(self.maxSpeed)
        self.steerForce.sub(self.vel)
        if self.steerForce.mag()>self.maxForce:
            self.steerForce.setMag(self.maxForce)
        self.acc.add(self.steerForce)
        
    def flee(self,target):
        self.target = target
        self.steerForce = PVector.sub(self.target,self.pos)        
        self.steerForce.normalize()
        self.steerForce.setMag(self.maxSpeed)
        self.steerForce.sub(self.vel)
        if self.steerForce.mag()>self.maxForce:
            self.steerForce.setMag(self.maxForce)
        self.steerForce.x *= -1
        self.steerForce.y *= -1
        self.acc.add(self.steerForce)
        
    def pursue(self,veh):
        self.target = veh.pos + veh.vel*veh.maxSpeed
        self.steerForce = PVector.sub(self.target,self.pos)        
        self.steerForce.normalize()
        self.steerForce.setMag(self.maxSpeed)
        self.steerForce.sub(self.vel)
        if self.steerForce.mag()>self.maxForce:
            self.steerForce.setMag(self.maxForce)
        self.acc.add(self.steerForce)
        
    def evade(self,veh):
        self.target = veh.pos + veh.vel*veh.maxSpeed
        self.steerForce = PVector.sub(self.target,self.pos)        
        self.steerForce.normalize()
        self.steerForce.setMag(self.maxSpeed)
        self.steerForce.sub(self.vel)
        if self.steerForce.mag()>self.maxForce:
            self.steerForce.setMag(self.maxForce)
        self.steerForce.x *= -1
        self.steerForce.y *= -1
        self.acc.add(self.steerForce)
        
    def arrive(self,target):
        self.target = target
        self.steerForce = PVector.sub(self.target,self.pos)
        distance = self.steerForce.mag()        
        self.steerForce.normalize()        
        slowRadius = 50
        if distance<slowRadius:
            self.steerForce.setMag(map(distance,0,slowRadius,0,self.maxSpeed))
        else :
            self.steerForce.setMag(self.maxSpeed)
        self.steerForce.sub(self.vel)
        if self.steerForce.mag()>self.maxForce:
            self.steerForce.setMag(self.maxForce)
        self.acc.add(self.steerForce)

    def wander(self):
        dir = self.vel.copy()
        dir.normalize()
        dir.setMag(100)
        dir.add(self.pos)
        stepSize = 1
        self.wanderTheta += (random(1)-0.5)*stepSize
        wanderR = 50
        wanderPoint = PVector.fromAngle(self.wanderTheta)
        wanderPoint *= wanderR
        wanderPoint += dir
        noFill()
        stroke(100)
        circle(dir.x,dir.y,2*wanderR)
        circle(wanderPoint.x,wanderPoint.y,10)
        self.steerForce = PVector.sub(wanderPoint,self.pos)
        if self.steerForce.mag()>self.maxForce:
            self.steerForce.setMag(self.maxForce)
        self.acc.add(self.steerForce)
        
    def followPath(self,path):
        future = PVector.copy(self.vel).setMag(50) + self.pos
        circle(future.x,future.y,5)
        proj = vectProjPoint(path.p1,path.p2,future)
        circle(proj.x,proj.y,5)
        dst = dist(proj.x,proj.y,future.x,future.y)
        if dst > path.radius:
            self.seek(proj)
                    
    def update(self):
        self.vel.add(self.acc)
        if self.vel.mag()>self.maxSpeed:
            self.vel.setMag(self.maxSpeed)
        # print(self.vel.x,self.vel.y)
        self.pos.add(self.vel)
        self.pos.x %= width
        self.pos.y %= height
        self.ang = self.vel.heading()
        self.acc.set(0,0)
        
    def display(self):
        pushMatrix()
        translate(self.pos.x,self.pos.y)
        rotate(self.ang)
        fill(180)
        stroke(0)
        triangle(self.s,0,-self.s,self.s/2,-self.s,-self.s/2)
        popMatrix()

p = Path()        
v1 = Vehicle(pos=PVector(random(250),random(250)), vel=PVector.random2D()*3,s = 5)
v2 = Vehicle(pos=PVector(250,250),maxSpeed=3,maxForce=0.3)
v3 = Vehicle(pos=PVector(250,250),vel=PVector.random2D()*3,maxSpeed=3,maxForce=0.3)
v4 = Vehicle(pos=PVector(0,125),vel=PVector(4,0))
    
