def setup():
    size(500, 500)
    background(255)
    stroke(0)
    strokeWeight(2)
    noSmooth()

pos = PVector(250,250)    
prev = PVector.copy(pos)

def draw():
    # background(255)
    pos.add((PVector.random2D()).mult(random(2,25)))
    line(pos.x,pos.y,prev.x,prev.y)
    prev.set(pos)
