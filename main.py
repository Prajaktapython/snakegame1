import turtle
import random
import time 
screen=turtle.Screen()
screen.title('Snake game')
screen.setup(width = 700,height = 700)
screen.tracer(0)
turtle.bgcolor('purple')
turtle.speed(5)
turtle.pensize(5)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.penup()
turtle.hideturtle()
snake=turtle.Turtle()
snake.speed(0)
snake.color('green')
snake.shape('triangle')
snake.penup()
snake.goto(0,0)
snake.direction='stop'
food=turtle.Turtle()
food.speed(0)
food.color('orange')
food.shape('circle')
food.penup()
food.goto(50,50)
score=turtle.Turtle()
score.speed(0)
score.color('grey')
score.hideturtle()
score.penup()
score.goto(0,300)
score.write('score:',align='center',font=('Courier',24,'bold'))

def snake_go_up():
    if snake.direction != "down":
       snake.direction = "up"
       print('snake_up')
def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"
        print('snake_down')
def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right" 
        print('snake_right') 
def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"
        print('snake_left')          
   

def snake_move():
    if snake.direction =="up":
        print('up')
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        print('down')
        y =snake.ycor() 
        snake.sety(y - 20)   

    if snake.direction == "left":
        print('left')
        x = snake.xcor()    
        snake.setx(x - 20)

    if snake.direction == "right":
        print('right')
        x = snake.xcor()
        snake.setx(x + 20)   

screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")

points = 0
delay = 0.1 
old_fruit=[]

while True:
    screen.update()
    if snake.distance(food)<20:
        x = random.randint(-290,280)
        y = random.randint(-240,240)
        food.goto(x,y)
        score.clear()
        points+=1
        score.write('Score:{}'.format(points),align = "center",font=("courier",24,"bold"))
        

        delay-=0.001
        new_fruit=turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("circle")
        new_fruit.color("Orange")
        new_fruit.penup()

        old_fruit.append(new_fruit)
    for index in range(len(old_fruit)-1,0,-1):
        a = old_fruit[index-1].xcor()
        b = old_fruit[index-1].ycor()
        old_fruit[index].goto(a,b)
    if len(old_fruit)>0:
        a=snake.xcor()    
        b=snake.ycor()
        old_fruit[0].goto(a,b)
    snake_move()
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('blue') 
        score.goto(0,0) 
        score.write("game over\n your score is {}".format(points),align = "center",font=("courier",30,"bold"))
    for food in old_fruit:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('blue') 
            score.goto(0,0) 
            score.write("game over\n your score is {}".format(points),align = "center",font=("courier",30,"bold"))


   
    time.sleep(delay)
turtle.Terminator()