class Frog: #you must define more functions in this class
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def moveUp(self):
        self.y-=5

    def moveDown(self):
        self.y+=5

    def moveLeft(self):
        self.x-=5

    def moveRight(self):
        self.x+=5

    def collisionPoint(self, x, y):
        if self.x <= x <= self.x+self.width and self.y <= y <= self.y+self.height:
            return True
        else:
            return False

    def collision(self, c):
        if self.collisionPoint(c.x, c.y) or self.collisionPoint(c.x, c.y+c.height) or self.collisionPoint(c.x+c.width, c.y) or self.collisionPoint(c.x+c.width, c.y+c.height):
            return True
        return False

    def draw(self,w):   #just an example in how to draw a rectangle filled in green
        w.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height,fill="green")
