import random as r
#import turtle
#print(r.randint(0,100))
#from random import randint #only randint for random
# lst = [0, 1, 2, 3, 4, 5, 6, 7]
# print(r.choice(lst)) #выбор содержимого
# r.shuffle(lst) #shuffle=перемешать содержимое
# print(lst)
import turtle as t
screen=t.Screen()
t = t.Turtle()
# t.forward(500)
t.pensize(2)
t.speed(0)
t.shape("turtle")
t.color("blue")
x = 100
y = 200
t.fd(x)
t.rt(90)
t.fd(y)
t.rt(90)
t.fd(x)
t.rt(90)
t.fd(y)
t.rt(90)
t.penup()
t.fd(20)
t.rt(90)
t.fd(20)
t.pendown()
t.fd(30)
t.rt(-90)
t.fd(60)
t.rt(-90)
t.fd(30)
t.rt(-90)
t.fd(60)
t.circle(30)
t.write("Movavi", font=("Arial black", 50,"normal"), align="center")
screen.exitonclick()
