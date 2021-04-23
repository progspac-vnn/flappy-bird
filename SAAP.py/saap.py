#Simple Snake Game 

# Part-1 Set Up
# Part-2 Snake's Head
# Part-3 Food
# Part-4 Snake's Body
# Part-5 Border collisions
# Part-6 Body collisions
# Part-7 Pen(Scoring) 


import turtle
import random
import time
delay = 0.1

#Score
score = 0
high_score = 0

#set up the screen
win = turtle.Screen()
win.title("MAMBA")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0)

# Snake's Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Segment
segments = []

# pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  High Score:0",align="center",font=("Courier", 24,"normal"))


# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0, 100)

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
   if head.direction != "up":
       head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction ="right"
def go_left():
    if head.direction != "right":
        head.direction = "left"




def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety( y + 20)
    if head.direction =="down":
        y = head.ycor()
        head.sety( y - 20)
    if head.direction =="right":
        x = head.xcor()
        head.setx( x + 20)
    if head.direction =="left":
        x = head.xcor()
        head.setx( x - 20)


#Keyboard bindings

win.listen()
win.onkeypress(go_up,"Up")
win.onkeypress(go_down,"Down")
win.onkeypress(go_right,"Right")
win.onkeypress(go_left,"Left")

# Main game loop 
while True:
    win.update()
    
    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    
        
    # Check for collision with food
    if head.distance(food) <20:
        # Move food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
    
    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -=0.001

        # Increase the score 
        score += 1 
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier", 24,"normal"))



    # Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    

    move()
    
    # Check for Body collision 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Hide the segment
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments
            segments.clear()    
    
            # Reset the score
            score = 0
            # Reset the delay 
            delay = 0.1
            # Update the score display 
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier", 24,"normal"))

    time.sleep(delay)
win.mainloop()
