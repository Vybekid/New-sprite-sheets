import turtle
import time

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.title("IShowSpeed Dance")
screen.tracer(0) 

animation_frames = [
    "frame_1.gif", "frame_2.gif", "frame_3.gif", "frame_4.gif", 
    "frame_5.gif", "frame_6.gif", "frame_7.gif", "frame_8.gif", 
    "frame_9.gif", "frame_10.gif"
]

for frame in animation_frames:
    screen.addshape(frame)

character = turtle.Turtle()
character.penup()
character.goto(-screen.window_width() / 2 - 50, 0)

frame_index = 0

while True:
    character.shape(animation_frames[frame_index])
    
    frame_index = (frame_index + 1) % len(animation_frames)
    character.forward(10)    
    screen.update()
    
    if character.xcor() > screen.window_width() / 2 + 50:
        character.goto(-screen.window_width() / 2 - 50, 0)
        
    time.sleep(0.17)

    