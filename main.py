# 1/2/5
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

#1 These set of codes are used to set up the screen
window = turtle.Screen()
window.title("Retro Snake Game by @PrinceXXIV")
window.bgcolor("Gold")
window.setup(width=500, height=500)
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

#7 Pen - this is to setup the scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Score : 0  High Score : 0", align="center", font=("Courier", 24, "normal"))


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
  if snakehead.direction != "down" :  
      snakehead.direction = "up"

def go_down():
  if snakehead.direction != "up" :
      snakehead.direction = "down"

def go_right():
  if snakehead.direction != "left" :
      snakehead.direction = "right"

def go_left():
  if snakehead.direction != "right" :
      snakehead.direction = "left"

# Since the "def" 's are functions we need to bind these to the keyboard, so that the snake moves according to the keyboard arrows - connecting a key press to a particular function

window.listen()
window.onkeypress(go_up,"Up") #For Python 2.7 it is window.onkey not press
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")

#Main game Loop

#5 Check for collision with the border

if snakehead.xcor()>250 or snakehead.xcor()<-250 or snakehead.ycor()>250 or snakehead.ycor()<-250:
        time.sleep(1)
        snakehead.goto(0,0)
        snakehead.direction = "stop"

#5 Hide segments if collision occurs
for segment in segments:
     segment.goto(1000, 1000)

#5 Clear the segment list
segments.clear()

# Reset the score
score = 0

# Reset the delay
delay = 0.1

while True:
    window.update()

    #4 Check for collision with the food


    if snakehead.distance(food) < 20:
      #3 Move the food to a random spot on the screen
      x = random.randint(-250,250)
      y = random.randint(-250,250)
      food.goto(x, y)

    #4 add a segment
      new_segment = turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("circle")
      new_segment.color("brown")
      new_segment.penup()
      segments.append(new_segment)

    #Shorten delay
      delay -= 0.001

    #7 Increase in score
      score += 10

    if score > high_score :
        high_score = score
    
    pen.clear()
    pen.write("Score: {} | High Score: {}".format(score, high_score), align="center", font=("Courier", "24", "normal"))

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

    #6 Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(snakehead) < 20:
          time.sleep(1)
          snakehead.goto(0,0)
          snakehead.direction = "stop"

          #5 Hide segments if collision occurs
          for segment in segments:
              segment.goto(1000, 1000)

          #5 Clear the segment list
          segments.clear()

          #7 Reset the score
          score = 0

          #Reset the delay
          delay = 0.1

          #Update the score display
          pen.clear()
          pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", "24", "normal"))

    time.sleep(delay)

window.mainloop()