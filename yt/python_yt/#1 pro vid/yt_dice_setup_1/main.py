import turtle

win = turtle.Screen()
win.setup(width=500, height= 500)
win.bgcolor('black')
win.title('Dice')
win.tracer(0)

dot = turtle.Turtle()
dot.shape('circle')
dot.color('red')
dot.goto(0,0)

while True:
    win.update()


win.mainloop()