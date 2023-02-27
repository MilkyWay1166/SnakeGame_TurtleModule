#Setup screen

import random
import turtle
import time

screen = turtle.Screen()
screen.setup(width=650,height=650)
screen.listen()
screen.tracer(0)
screen.title("Snake Game")


#Create class Scoreboard which automatically displays and updates players' score
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('blue')
        self.hideturtle()
        self.goto(0,300)
        self.write(f"YOUR SCORE: {self.score}", align='center',font=("Arial", 15, "normal"))
    
    #automatically increase players' score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"YOUR SCORE: {self.score}", align='center',font=("Arial", 15, "normal"))

    #display the final score when players lose
    def end_score(self):
        self.goto(0,0)
        self.write(f"END GAME!!!", align='center',font=("Arial", 15, "normal"))
                     


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color('yellow')
        x = random.randint(-13, 13)*20
        y = random.randint(-13, 13)*20
        self.goto(x, y)
    def refresh(self):
        x = random.randint(-13, 13)*20
        y = random.randint(-13, 13)*20
        self.goto(x, y)

START_POSITION = [(0,0),(-20,0),(-40,0)]

#create Snake class which initiate the snake and whose methods/functions execute its actions
class Snake:
    def __init__(self):
        self.snake = []
        for i in START_POSITION:
            segment = turtle.Turtle()
            segment.penup()
            segment.shape("square")
            segment.color("red")
            segment.goto(i)
            self.snake.append(segment)
        self.head = self.snake[0]

#the snake moves automatically and continuously 
    def move(self):
        
        position = self.snake[0].pos()
        self.snake[0].forward(20)
        for i in range(1,len(self.snake)):
            old_position = self.snake[i].pos()
            self.snake[i].goto(position)
            position = old_position

#change the snake's direction
    def move_up(self):
        if self.head.heading() in [0.0, 180.0]:
            self.head.setheading(90)
            

    def move_down(self):
        if self.head.heading() in [0.0, 180.0]:
            self.head.setheading(270)
            

    def move_left(self):
        if self.head.heading() in [90.0, 270.0]:
            self.head.setheading(180)
            

    def move_right(self):
        if self.head.heading() in [90.0, 270.0]:
            self.head.setheading(0)
            

    
#Eat food and lengthen the snake's size       
    def eat(self):
        longer = self.snake[-1].clone()
        self.snake.append(longer)
        

#Check if the snake is dead 
    def is_dead(self):

        #check if the snake hit the walls
        check_xcor = (self.head.xcor() > 279) or (self.head.xcor() < -279)
        check_ycor = (self.head.ycor() > 279) or (self.head.ycor() < -279)
        hit_wall = check_xcor or check_ycor

        #check if the snake eat itself
        check_self_eat = False
        for i in self.snake:
            if i == self.head:
                pass
            elif self.head.distance(i) < 15:
                check_self_eat = True
        
        #Snake will die if 1 of 2 situations above happens
        if hit_wall:
            return True
        elif check_self_eat:
            return True
        else:
            return False

#Setup snake, food, and scoreboard

snake_food = Food()
snake_game = Snake()
scoreboard = ScoreBoard()
border = turtle.Turtle()
border.penup()
border.goto(-280,280)
border.pendown()
border.pensize(10)
border.hideturtle()

#Create the border
for i in range(4):
    border.forward(280*2)
    border.right(90)
screen.update()


screen.onkey(key='Up',fun = snake_game.move_up)
screen.onkey(key='Down',fun = snake_game.move_down)
screen.onkey(key='Left',fun = snake_game.move_left)
screen.onkey(key='Right',fun = snake_game.move_right)


#GameLoop
while not snake_game.is_dead():
    time.sleep(0.3)
    screen.update()
    if snake_game.head.distance(snake_food) < 1:
        snake_food.refresh()
        snake_game.eat()
        scoreboard.increase_score()
                        
    snake_game.move()
    
scoreboard.end_score()

turtle.exitonclick()

    



