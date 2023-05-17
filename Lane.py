from Car import Car


class Lane:
    def __init__(self, x, y, width, height, car_width, car_height, number_of_cars, speed, movement):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.cars = []
        self.car_width = car_width
        self.car_height = car_height
        self.speed = speed
        self.movement = movement
        for i in range(number_of_cars):
            if self.movement == "right":
                startX = -i*car_width*2
            else:
                startX = self.width+(i*car_width*2)
            car = Car(startX,y+self.height/2-self.car_height/2, self.car_width, self.car_height, self.speed, self, self.movement)
            self.cars.append(car)

    def move(self):
        for c in self.cars:
            c.move()

    def draw(self, w):
        w.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height, fill="gray")
        for c in self.cars:
            c.draw(w)
