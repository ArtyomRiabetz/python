def setup():
    size(600,600)
    background(0,0,0)
    frameRate(5)

def draw():
    stroke(random(200,255))
    strokeWeight(random(1,5))
    point( random(5,600),random(5,600))
 
    
