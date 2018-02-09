import turtle
def main():
    c1 = Coin(1,2)
    print(c1)
    return


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
        return "Length: " + str(self.length) + " Width: "+ str(self.width)

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getMass(self):
        return self.mass

    def drawCoin(self,t):
        t.pu()
        t.goto(self.pos.getX())

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + self.x + ","+self.y+")"
    
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
