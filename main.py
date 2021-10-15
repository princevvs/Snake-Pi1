import turtle
import time

delay = 0.1

#These set of codes are used to set up the screen
window = turtle.Screen()
window.title("Retro Snake Game by @PrinceXXIV")
window.bgcolor("Gold")
window.setup(width=600, height=550)
window.tracer(0) #This turns off any screen update

#Snake head
snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("circle")
snakehead.color("red")
snakehead.penup()
snakehead.goto(0,0)
snakehead.direction = "stop"

#Functions
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
while True:
    window.update()

    move()

    time.sleep(delay)


window.mainloop()