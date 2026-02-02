# Baez Module 02 - Exercise 3: Graphics (Turtle)
# Author: Florentino Báez

import turtle

# EXERCISE 3: Graphics (4 different shapes)
# Draws: red circle (top left), blue square (top right),
# green triangle (bottom left), orange star (bottom right).

print("=" * 60)
print("EXERCISE 3: Graphics")
print("=" * 60)
print("Creating 4 different graphics...")

# Create turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Module 02 Lab - Graphics")

# Create turtle object
t = turtle.Turtle()
t.speed(3)

# Graphic 1: Red Circle (top left)
t.penup()
t.goto(-300, 200)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(50)
t.end_fill()

# Graphic 2: Blue Square (top right)
t.penup()
t.goto(200, 200)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

# Graphic 3: Green Triangle (bottom left)
t.penup()
t.goto(-250, -150)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# Graphic 4: Orange Star (bottom right)
t.penup()
t.goto(200, -100)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for _ in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

t.hideturtle()

print("Graphics created successfully!")
print("Close the graphics window to continue...")

screen.exitonclick()
