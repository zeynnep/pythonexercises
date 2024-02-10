import turtle 
import colorsys

t= turtle.Turtle()
s = turtle.Screen()
s.bgcolor('purple')
t.speed(0)
n = 50
h = 0

for i in range(800):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h=h+1/n
    t.color(c)
    t.forward(i*2)
    t.left(145)

turtle.done()