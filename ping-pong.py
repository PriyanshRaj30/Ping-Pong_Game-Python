import turtle

win = turtle.Screen()
win.title("Classic : Ping Pong")
win.bgcolor("black")
win.setup(width=800,height=700)
win.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)


while True:
	win.update()
