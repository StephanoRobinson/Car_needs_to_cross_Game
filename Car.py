class Car:  #you must define more functions in this class
    def __init__(self,x,y,width,height, speed,lane,movement="right"):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.movement=movement
        self.speed=speed
        self.lane=lane

    def move(self):
        tempY = self.y
        if self.movement =="left":
            self.x-=self.speed
        elif self.movement=="right":
            self.x+=self.speed

        if self.x>=800 and self.movement=="right":
            self.x=0
            self.y=tempY
        elif self.x<=0 and self.movement=="left":
            self.x=self.lane.width
            self.y=tempY

    def draw(self, w):  #just an example in how to draw a rectangle not filled
        if self.movement == "right":
            w.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height, fill="white")
            w.create_line(self.x+(0.75*self.width),self.y,self.x+(0.75*self.width),self.y+self.height)
        elif self.movement == "left":
            w.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height, fill="white")
            w.create_line(self.x+(0.25*self.width),self.y,self.x+(0.25*self.width),self.y+self.height)
