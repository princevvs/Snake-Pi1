# 1/2/5
import turtle
import time
import random

delay = 0.1

#1 These set of codes are used to set up the screen
window = turtle.Screen()
window.title("Retro Snake Game by @PrinceXXIV")
window.bgcolor("Gold")
window.setup(width=600, height=550)
window.tracer(0) #This turns off any screen update

#2 Snake head
snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("circle")
snakehead.color("red")
snakehead.penup()
snakehead.goto(0,0)
snakehead.direction = "stop"

#3 Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(0,100)

# 4
segments = []


#2 Functions
def move():
    if snakehead.direction == "up":
        y = snakehead.ycor()
        snakehead.sety(y + 20)

    if snakehead.direction == "down":
        y = snakehead.ycor()
        snakehead.sety(y - 20)

    if snakehead.direction == "right":
        x = snakehead.xcor()
        snakehead.setx(x + 20)

    if snakehead.direction == "left":
        x = snakehead.xcor()
        snakehead.setx(x - 20)

def go_up():
    snakehead.direction = "up"

def go_down():
    snakehead.direction = "down"

def go_right():
    snakehead.direction = "right"

def go_left():
    snakehead.direction = "left"

# Since the "def" 's are functions we need to bind these to the keyboard, so that the snake moves according to the keyboard arrows - connecting a key press to a particular function

window.listen()
window.onkeypress(go_up,"Up") #For Python 2.7 it is window.onkey not press
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")

#Main game Loop

#5 Check for collision with the border
if snakehead.xcor()>270 or snakehead.xcor()<-270 or snakehead.ycor()>270 or snakehead.ycor()<-270:
    time.sleep(1)
    snakehead.goto(0,0)
    snakehead.direction = "stop"
#5 Hide segments if collision occurs
for segment in segments:
    segment.goto(1000, 1000)

#5 Clear the segment list
segments.clear()

while True:
    window.update()

    #4 Check for collision with the food


    if snakehead.distance(food) < 20:
      #3 Move the food to a random spot on the screen
      x = random.randint(-290,290)
      y = random.randint(-290,290)
      food.goto(x, y)

    #4 add a segment
      new_segment = turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("circle")
      new_segment.color("brown")
      new_segment.penup()
      segments.append(new_segment)

    #4 Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #4 Move segment 0 to where the head is
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x,y)
    move()

    time.sleep(delay)

window.mainloop()