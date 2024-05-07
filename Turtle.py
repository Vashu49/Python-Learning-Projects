#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle

# Function to draw a single square
def draw_square():
    for _ in range(4):
        turtle.forward(20)
        turtle.left(90)

# Function to draw the floor
def draw_floor():
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    for _ in range(20):
        for _ in range(20):
            draw_square()
            turtle.forward(20)
        turtle.penup()
        turtle.goto(-200, turtle.ycor() + 20)
        turtle.pendown()

# Function to move turtle forward and draw a line
def move_forward():
    turtle.forward(20)

# Function to turn turtle left
def turn_left():
    turtle.left(90)

# Function to turn turtle right
def turn_right():
    turtle.right(90)

# Function to lift pen
def lift_pen():
    turtle.penup()

# Function to drop pen
def drop_pen():
    turtle.pendown()

# Read commands from a file
def read_commands_from_file(filename):
    with open(filename, 'r') as file:
        commands = file.readlines()
    return [command.strip() for command in commands]

if __name__ == "__main__":
    # Initialize turtle
    turtle.speed(0)
    turtle.hideturtle()

    # Draw the floor
    draw_floor()

    # Optionally, read commands from a file
    # commands = read_commands_from_file("commands.txt")

    # List of commands
    commands = ["forward", "left", "right", "lift", "drop"]

    # Perform commands
    for command in commands:
        if command == "forward":
            move_forward()
        elif command == "left":
            turn_left()
        elif command == "right":
            turn_right()
        elif command == "lift":
            lift_pen()
        elif command == "drop":
            drop_pen()

    turtle.done()


# In[ ]:




