import turtle as tur
import colorsys as cs
tur.screensize(860,860)
tur.setup(675,675)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
for j in range(51): 
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/51,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
tur.done()
