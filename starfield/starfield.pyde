def setup():
    size(w, h)
    background(0)
    # noLoop()

global w,h,f,r,maxX,maxY
w,h,f,r = 1000,1000,1000,1000
global maxX
global maxY
maxX = w*(r+f)/(2*f)
maxY = h*(r+f)/(2*f)    
def draw():
    # if frameCount%5==0:
    background(0,0,0,255)
    translate(250,250)    
    for i in starArr:
        i.update()
        i.show()
    
class Star():
    def __init__(self):
        self.x = random(-maxX/2,maxX/2)
        self.y = random(-maxY/2,maxY/2)
        self.z = random(r)
        self.s = random(2,20)
        self.prevx,self.prevy = f*self.x/(self.x + self.z), f*self.y/(self.y + self.z)
        
    def update(self):
        self.z -= 20
        if self.z <10:
            self.x = random(-maxX/2,maxX/2)
            self.y = random(-maxY/2,maxY/2)
            self.z=r
            self.prevx,self.prevy = f*self.x/(self.x + self.z), f*self.y/(self.y + self.z)
        
    def show(self):
        fill(255)
        noStroke()
        stroke(255)
        sx = f*self.x/(self.x + self.z)
        sy = f*self.y/(self.y + self.z)
        ss = f*self.s/(self.s + self.z)
        circle(sx,sy,ss)
        line(sx,sy,self.prevx,self.prevy)
        self.prevx = sx;
        self.prevy = sy;
        
starArr = [Star() for x in range(100)]
