def setup():
    size(500, 500)
    frameRate(3)
    noFill()
    # noSmooth()
    
    # ln = 100
    # global ln
    # noLoop()



def draw():
    background(255)
    ''' lsys '''
    # translate(width/2,height)
    # rotate(-PI)
    
    # turtle(lsys,10,PI/6)
    # turtle("FF++++F++++F",100,PI/6)
    
    
    ''' trees '''
    translate(width/2,height)
    branch(mouseX/2,(float(mouseY)/height)*(PI/2))
    # branchrnd(mouseX/2,0)
    
    # for i in cantorLineArr:
    #     for j in i:
    #         j.display()    
    # for i in kochLineArr:
    #     i.display()
    # fractalI(250,250,125)
    # cantor(10,10,480)
    # fractalcircle(250,250,500)

    
        

        
def fractalcircle(x,y,d):
    circle(x,y,d)
    if d>10:
        fractal(x+d/2,y,d/2)
        fractal(x-d/2,y,d/2)
        fractal(x,y+d/2,d/2)
        fractal(x,y-d/2,d/2)
        
def cantor(x,y,l):
    line(x,y,x+l,y)
    if l>5:
        cantor(x,y+10,l/3) 
        cantor(x+2*l/3,y+10,l/3)
        
def drawI(x,y,l):
    line(x-l/2,y-l/2,x-l/2,y+l/2)
    line(x+l/2,y-l/2,x+l/2,y+l/2)
    line(x-l/2,y,x+l/2,y)
    
def fractalI(x,y,l):
    drawI(x,y,l)
    if l>10:
        fractalI(x-l/2,y-l/2,l/2)
        fractalI(x-l/2,y+l/2,l/2)
        fractalI(x+l/2,y-l/2,l/2)
        fractalI(x+l/2,y+l/2,l/2)

    
class Line():
    def __init__(self, v1,v2):
        self.v1, self.v2, = v1,v2  
    def display(self):
        line(self.v1.x, self.v1.y, self.v2.x, self.v2.y) 
        
global kochLineArr        
kochLineArr = [Line(PVector(10,250), PVector(490,250))]


def generateKoch(lst):
    newlst = []
    for l in lst:
        a = l.v1
        e = l.v2
        b = PVector.lerp(a,e,1.0/3.0)
        d = PVector.lerp(a,e,2.0/3.0)
        bd = PVector.sub(d,b)
        bd.rotate(-PI/3)
        c = PVector.add(bd,b)
        newlst.append(Line(a,b))
        newlst.append(Line(b,c))
        newlst.append(Line(c,d))
        newlst.append(Line(d,e))
    return newlst

cantorLineArr = [[Line(PVector(10,10), PVector(490,10))]]

def generateCantor(lst):
    newlst = []
    for l in lst:
        a,d = PVector.copy(l.v1), PVector.copy(l.v2)
        print(a,d)
        a.y = a.y + 10
        d.y = d.y + 10
        b,c = PVector.lerp(a,d,1.0/3.0), PVector.lerp(a,d,2.0/3.0)
        newlst.append(Line(a,b))
        newlst.append(Line(c,d))
    return newlst



def branch(ln,a):
    strokeWeight(map(ln , 0,125, 0,10))
    line(0,0,0,-ln)
    translate(0,-ln)
    ln *= 0.66
    
    if ln>2:
        pushMatrix()
        rotate(a)
        branch(ln,a)
        popMatrix()
        
        pushMatrix()
        rotate(-a)
        branch(ln,a)
        popMatrix()
        
def branchrnd(ln,ang):
    strokeWeight(map(ln , 0,mouseX/2, 0,10))
    line(0,0,0,-ln)
    translate(0,-ln)
    ln *= 0.66
    
    if ln>2:
        for i in range(1,int(random(5))+1):
            pushMatrix()
            ang = random(-PI/2,PI/2)
            rotate(ang)
            branchrnd(ln,ang)
            popMatrix()
                
                
def turtle(string,ln,angle):
    for i in string:
        if i=="F":
            line(0,0,0,ln)
            translate(0,ln)
        elif i=="G":
             translate(0,ln)
        elif i=="+":
             rotate(angle)
        elif i=="-":
            rotate(-angle)
        elif i=="[":
            pushMatrix()          
        elif i=="]":
            popMatrix()

           
def lsysgen(string):
    next = ""
    for i in string:
        print(i)
        if i =="F":
            next = next + "FF+[+F-F-F]-[-F+F+F]"
        else:
            next=next+str(i)
        print(next)
    return next
  
# global lsys
# lsys = "F"
# lsys = lsysgen(lsys)
# lsys = lsysgen(lsys)
# lsys = lsysgen(lsys)
# lsys = lsysgen(lsys)

def mouseClicked():
    background(255)
    # lsys = lsysgen(lsys)
    # cantorLineArr.append(generateCantor(cantorLineArr[-1]))
    # global kochLineArr
    # kochLineArr = generateKoch(kochLineArr)
