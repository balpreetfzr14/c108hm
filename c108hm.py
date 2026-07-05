
import turtle
#importing library
turtle.Screen().bgcolor("green")
turtle.Screen().setup(308,400)
polygon = turtle.Turtle() #defined variable
num_sides = 1000 #variable
side_length= 1
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)