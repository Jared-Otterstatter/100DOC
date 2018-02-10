import turtle as t
def main():
    screen=t.Turtle()
    c1 = Coin(100,200,5,5)
    print(c1)
    c1.applyForce(Vector(2,2))
    c1.update()
    c1.draw(t)
    print(c1)


class Coin:
    """Coin Class"""
    def __init__(self,length, width,x,y):
        self.length = length
        self.width  = width
        self.mass = 1
        self.pos = Vector(x,y)
        self.vel = Vector(0,0)
        self.acc = Vector(0,0)
    def __str__(self):
        outString = "Length: " + str(self.length) + " Width: " + str(self.width) +"\n"
        outString += "Pos: "+ str(self.pos) + " Vel:" + str(self.vel) + "Acc:" +str(self.acc)
        return outString

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getMass(self):
        return self.mass

    def draw(self,t):
        t.pu()
        t.goto(self.pos.getX(),self.pos.getY())
        t.pd()
        t.goto(self.pos.getY()+self.getWidth(),self.pos.getX())
        t.goto(self.pos.getY()+self.getWidth(),self.pos.getX())
        t.goto(self.pos.getY()+self.getWidth(),self.pos.getX()+self.getWidth())
        t.goto(self.pos.getY(),self.pos.getX()+self.getWidth())
        t.goto(self.pos.getY(),self.pos.getX())
        t.pu()

    def update(self):
        self.vel+=self.acc
        self.pos+=self.vel
        self.acc=Vector(0,0)
        return True

    def applyForce(self,vec):
        self.acc+=vec

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ","+ str(self.y)+")"
    
    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)

    def scale(self, scaler):
        self.x *=scaler
        self.y *=scaler

    def getX(self):
        return self.x

    def getY(self):
        return self.y





if __name__ == "__main__": main()
