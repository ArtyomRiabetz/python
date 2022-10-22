def setup():
    size(600,600)
    background(0,0,0)
    frameRate(5)

def draw():
    point(random(5,600),random(5,600))
    stroke(255,255,0)
    strokeWeight(random(1,5))
