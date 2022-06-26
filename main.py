import time
from turtle import Screen
from Snake import Snake
from food import Food
from score_board import Score_Board

# screen setting ---------------------------------------------
my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("SnakeGame")
my_screen.tracer(0)
# --------------------------------------------------------------

my_snake = Snake()
food = Food()
score_board = Score_Board()

my_snake.create_snake()

my_screen.listen()
my_screen.onkey(my_snake.up, "w")
my_screen.onkey(my_snake.down, "s")
my_screen.onkey(my_snake.right, "d")
my_screen.onkey(my_snake.left, "a")

game_is_on = True

while game_is_on:
	my_screen.update()
	time.sleep(0.1)
	my_snake.moving_snake()

	# Detect collision with food
	if my_snake.head.distance(food) < 15:
		my_snake.extend_snake()
		food.refresh_food()
		score_board.increase_score()

	# Detect collision with wall

	if my_snake.head.xcor() < -290 or my_snake.head.xcor() > 290 or my_snake.head.ycor() < -290 or my_snake.head.ycor() > 290:
		score_board.reset()
		my_snake.reset()

	# Detect collision with tail
	for segment in my_snake.snake[1:]:
		if my_snake.head.distance(segment) < 10:
			score_board.reset()
			my_snake.reset()



my_screen.exitonclick()
