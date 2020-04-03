# import turtle
# # from turtle import Tkinter
# import tk as Tkinter


# fred = turtle.Pen()
# fred.shape("turtle")
# fred.forward(100)
# fred.circle(100)
# fred.color("blue")
# fred.circle(-100)
# fred.forward(100)
# Tkinter.mainloop()


import time
import turtle
import tk as Tkinter
from turtle import Turtle # specijalna funkcija Turtle (Kornjaca)
from random import randint # random integer (slucajni cijeli broj)

# kreiranje prozora
window = turtle.Screen()
window.title=("Trke Kornjaca")


turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0) # prikazi odmah
turtle.penup() # kretanje kornjace u drugim pozicijama, trenutno je kornjaca na poziciji x,y = [0,0]
turtle.setpos(-140, 200) # x lijevo, y gore
turtle.write("Trke Kornjaca", font=("Arial", 30, "bold"))
turtle.penup()

# zemlja oko staze, dekoracija
turtle.setpos(-400, -180)
turtle.color("chocolate")
turtle.begin_fill() # popuni oblik bojom
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

# finish linija
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range (10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range (10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

# class nova_kornjaca:
# 	def __init__(self,speed,color,shape,penup,goto):
# 		self.speed = speed
# 		self.color = color
# 		self.shape = shape
# 		self.penup = penup
# 		self.goto = goto
		

kornjaca1 = Turtle()
kornjaca1.speed(0)
kornjaca1.color("black")
kornjaca1.shape("circle")
kornjaca1.penup()
kornjaca1.goto(-250, 100)
kornjaca1.penup()
# kornjaca1 = nova_kornjaca(0,"black","turtle","","-250, 100")


# kornjaca 2
kornjaca2 = Turtle()
kornjaca2.speed(0)
kornjaca2.color("cyan")
kornjaca2.shape("turtle")
kornjaca2.penup()
kornjaca2.goto(-250, 50)
kornjaca2.penup()


# kornjaca 3
kornjaca3 = Turtle()
kornjaca3.speed(0)
kornjaca3.color("yellow")
kornjaca3.shape("turtle")
kornjaca3.penup()
kornjaca3.goto(-250, 0)
kornjaca3.penup()


# kornjaca 4
kornjaca4 = Turtle()
kornjaca4.speed(0)
kornjaca4.color("magenta")
kornjaca4.shape("turtle")
kornjaca4.penup()
kornjaca4.goto(-250, -50)
kornjaca4.penup()

# kornjaca 5
kornjaca5 = Turtle()
kornjaca5.speed(0)
kornjaca5.color("blue")
kornjaca5.shape("turtle")
kornjaca5.penup()
kornjaca5.goto(-250, -100)
kornjaca5.penup()

time.sleep(1)

# pokreni kornjace
for i in range(145):
    kornjaca1.forward(randint(1,5))
    kornjaca2.forward(randint(1,5))
    kornjaca3.forward(randint(1,5))
    kornjaca4.forward(randint(1,5))
    kornjaca5.forward(randint(1,5))

turtle.exitonclick()

Tkinter.mainloop()