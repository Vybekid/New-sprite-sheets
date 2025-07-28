from turtle import *

# Settings for the turtle
speed(9)
hideturtle()
width(4)

# Move to starting position for the red rectangle
penup()
goto(160, -100)
pendown()

# Draw the outer red rounded rectangle
begin_fill()
color('#FF0000')
fillcolor("#FF0000")
left(90)

# Loop to draw the two long sides and two rounded corners
for i in range(2):
    forward(100)
    circle(50, 90)
    forward(200)
    circle(50, 90)
end_fill()

# Move to position for the white play triangle
goto(-20, 0)

# Draw the white play triangle
begin_fill()
fillcolor('#fff')
color('#fff')
left(180)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()

# Keep the window open until it's closed manually
done()