# Exercise 7: Drawing Shapes with Turtle
# Use the turtle module to draw basic shapes (circle, triangle, square)
# with different colors and positions on the screen.

import turtle

# Create a turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set drawing speed

# Draw a red circle
pen.color("red")
pen.begin_fill()
pen.circle(50)  # radius 50
pen.end_fill()

# Move to a new position for the triangle
pen.penup()
pen.goto(-150, -100)
pen.pendown()

# Draw a blue triangle
pen.color("blue")
pen.begin_fill()
for _ in range(3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()

# Move to another position for the square
pen.penup()
pen.goto(100, -100)
pen.pendown()

# Draw a green square
pen.color("green")
pen.begin_fill()
for _ in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# Finish and display the drawing
print("Drawing complete! Close the turtle window to continue.")
turtle.done()
