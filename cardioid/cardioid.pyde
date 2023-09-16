def setup():
    size(800,800)
    background(255)
    noLoop()
    
def draw():
    translate(400,200)
    stroke(255,0,0)
    strokeWeight(3)
    # point(0,0)=
    noSmooth()
    rotate(PI)
    
    # translate(0,400)
    lim = 1000.0
    for i in range(int(lim)):
        theta = TWO_PI*(i/lim)
        print(TWO_PI*(i/lim))
        r = 100*(2-2*sin(theta) + (sin(theta)*(sqrt(abs(cos(theta))))/(sin(theta)+1.4)))
        # point(200*(1-cos(theta)),0)
        point(r,0)
        # point(200*sin(2*i*(TWO_PI/lim)),0)
        # translate(-100,-100)
        rotate(TWO_PI/lim)
        
