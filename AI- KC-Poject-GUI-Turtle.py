def tortu():
    don.shape("turtle")
    don.pensize(70)
    don.pencolor("#2b8d1a")

    don.penup()
    don.pencolor("#0A210A")
    don.goto(-300, -160)
    don.pendown()
    don.forward(600)

    don.penup()
    don.pensize(70)
    don.pencolor("#3EE743")
    don.goto(-200, -200)
    don.pendown()

    don.penup()
    don.goto(-300, -190)
    don.pendown()
    don.forward(600)

    don.penup()
    don.pensize(10)
    don.goto(-200, -200)
    don.pendown()

    don.color("#d8c66b")
    don.begin_fill()
    for i in range(4):
        don.forward(150)
        don.left(90)
    don.end_fill()

    don.penup()
    don.pensize(5)
    don.pencolor("#cb571a")
    don.goto(-150, -200)
    don.pendown()

    don.color("#cb571a")
    don.begin_fill()
    for i in range(4):
        don.forward(60)
        don.left(90)
    don.end_fill()

    don.penup()
    don.goto(-200, -60)
    don.pendown()

    don.color("#f6ec15")
    don.begin_fill()
    don.circle(60)
    don.end_fill()

    don.color("#cb2d1a")
    don.begin_fill()
    for i in range(3):
        don.forward(150)
        don.left(120)
    don.color("#cb2d1a")
    don.end_fill()

    don.penup()
    don.pensize(35)
    don.pencolor("#865423")
    don.goto(90, -200)
    don.pendown()

    don.left(90)
    don.forward(200)

    don.penup()
    don.pensize(35)
    don.pencolor("#865423")
    don.goto(145, -30)
    don.pendown()

    don.color("#49b60e")
    don.begin_fill()
    don.circle(50)  # We call our Turtle to start the draw

from tkinter import *
import tkinter as tk
import turtle as don

window = tk.Tk()
window.geometry('600x600') #Defining size of the Window
window.title("Welcome to Tortuga y Casas app") #Title for the Window
canvas = tk.Canvas(master = window, width = 500, height = 500) # We create a Canvas of 600x600 attached to window
canvas.pack()

don = don.RawTurtle(canvas) #That's the magic to Get the Turtle inside the Canvas


tortu()

tk.Button(master = window, text = "That's All Folks", command = exit).pack(side = tk.BOTTOM) #Button attached to Window with Text with a Command
tk.Button(master = window, text = "Repeat Again", command = tortu()).pack(side = tk.BOTTOM) #Button attached to Window with a new call to turtle to repeat
window.mainloop()

