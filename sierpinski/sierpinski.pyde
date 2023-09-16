def setup():
    size(1000, 1000)
    # frameRate(1)
    # noFill()
    # noLoop()

def draw():
    background(255)
    print(frameCount)
    translate(width/2,height/2)
    stroke(0)
    # fill(0)
    # t = genPoly(100,5,frameCount*0.00)
    # circle(0,0,10)
    # shape(t,0,0)
    # sierp(frameCount//5+3,250,PI/2,PVector(0,300))
    # drawPoly(5,100,frameCount*0.00,PVector(0,0))
    sierp(3,250,PI/2,PVector(0,300))

# def genPoly(s,n,a):
#     sh = createShape()
#     sh.beginShape()
#     r = s/(2*sin(PI/n))
#     dv = PVector.fromAngle(a+180)*r
#     v = PVector.fromAngle(a)*r
#     for i in range(0,n):
#         res = dv+v
#         sh.vertex(res.x,res.y)
#         v.rotate(2*PI/n)
#     sh.endShape(CLOSE)
#     return sh

def vecLine(v1,v2):
    line(v1.x,v1.y,v2.x,v2.y)

def drawPoly(n,s,a,o):
    r = s/(2*sin(PI/n))
    mid = PVector.fromAngle(a)*(-r)
    o+=mid
    v1 = PVector.fromAngle(a)*r
    v2 = PVector.fromAngle(a+2*PI/n)*r
    for i in range(0,n):
        line((o+v1).x,(o+v1).y,(o+v2).x,(o+v2).y)
        v1.rotate(2*PI/n)
        v2.rotate(2*PI/n)
        

def sierp(n,r,a,o):
    
    # r = s/(2*sin(PI/n))
    s = r*(2*sin(PI/n))
    drawPoly(n,s,a,o)
    # print("#")
    v = PVector.fromAngle(a+PI/n)*r*cos(PI/n)
    # o += PVector.fromAngle(a)*(r)
    # circle(o.x,o.y,5)
    snew = s*sin(PI/n)*sin(PI/n)/(1+cos(PI/n))
    rnew = snew/(2*sin(PI/n))
    if snew>1:
        for i in range(0,n):
            res = o+v
            # circle(res.x,res.y,5)
            sierp(n,rnew,v.heading()+PI,res)
            v.rotate(2*PI/n)
