import turtle
from turtle import Turtle, Screen

screen = Screen()
me = Turtle("turtle")
me.speed(-10)
me.pensize(3)
screen.title("Welcome to the turtle zoo!")

def penUp():
    me.penup()

def penDown():
    me.pendown()

def dragging(x,y):
    me.ondrag(None)
    me.setheading(me.towards(x, y))
    me.goto(x, y)
    me.ondrag(dragging)

def clickright(x,y):
    me.clear()

turtle.onkey(penUp, "z")
turtle.onkey(penDown, "x")

def main():
    turtle.listen()
    me.ondrag(dragging)
    turtle.onscreenclick(clickright, 3)
    screen.mainloop()

main()

