from tkinter import *
import time
import keyboard
from Frog import Frog
from Lane import Lane


def isGameFinished(frog, lanes):
    for lane in lanes:
        for c in lane.cars:
            if frog.collision(c):
                time.sleep(50 / 1000)
                return True, "lose"
    if frog.y+frog.height >= lanes[0].y:
        return False, ""
    else:
        return True, "win"


#initialize the screen
tk = Tk()
WIDTH = 800
HEIGHT = 400
w = Canvas(tk, width=WIDTH, height=HEIGHT)      #w os the object (window) where drawing lines, rectangles, etc.
w.pack()

#create array of cars -> cars
"""car1 = Car(50, 100, 40, 20, "left", 5)
car2 = Car(100, 50, 40, 20, "right", 5)
cars = [car1,car2]"""

#lanes
l1 = Lane(0, 100, WIDTH, 60, 40, 20, 2, 5, "left")
l2 = Lane(0, 160, WIDTH, 60, 40, 20, 2, 10, "right")
lanes=[l1, l2]

#create frog    -> frog
frog = Frog(400, 370, 30, 30)

start_time=time.time()
total_time=0
result = ""


while True:
    while True:     #infinite loop
        total_time = time.time()-start_time
        total_time = int((total_time*100)/100)
        gameFinished = isGameFinished(frog, lanes)

        if gameFinished[0]:
            result=gameFinished[1]
            w.create_rectangle(WIDTH/3,HEIGHT/3,(WIDTH/3)*2, (HEIGHT/3)*2, fill="white")
            if result == "win":
                w.create_text(400,200, text="Good job!\nYour score : " + str(100-total_time)+"\nPress space to restart")
            else:
                w.create_text(400,200, text="Failed!\nPress space to restart")
            w.update()
            break

        #move the cars
        for lane in lanes:
            lane.move()

        #move the frog

        if keyboard.is_pressed("up arrow"):
            if frog.y<=0:
                print("OUT, too high")
            else:
                frog.moveUp()   #you must define this function
        if keyboard.is_pressed("down arrow"):
            if (frog.y+frog.height)>=400:
                print("OUT, too low")
            else:
                frog.moveDown()
        if keyboard.is_pressed("left arrow"):
            if frog.x<=0:
                print("OUT, too far on the left edge")
            else:
                frog.moveLeft() #you must define this function
        if keyboard.is_pressed("right arrow"):
            if (frog.x+frog.width)>=800:
                print("OUT, too far on the right edge")
            else:
                frog.moveRight()    #you must define this function

        #draw elements
        w.delete("all")
        w.create_rectangle(0,0,WIDTH, HEIGHT, fill="white")     #clean screen

        for lane in lanes:
            lane.draw(w)
        frog.draw(w)

        w.create_text(30,30, text=str("Time : "+ str(total_time)))
        w.update()

        #wait 50ms
        time.sleep(50 / 1000)

    while True:
        if keyboard.is_pressed(" "):
            break
        time.sleep(50 / 1000)
    time.sleep(50 / 1000)
    continue
