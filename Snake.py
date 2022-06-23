from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	def __init__(self):
		self.snake = []
		self.create_snake()
		self.head = self.snake[0]

	def create_snake(self):
		for position in STARTING_POSITION:
			self.add_segment(position)


	def add_segment(self, position):
		new_part = Turtle()
		new_part.shape("square")
		new_part.color("white")
		new_part.penup()
		self.snake.append(new_part)
		new_part.goto(position)


	def extend_snake(self):
		self.add_segment(self.snake[-1].position())


	def moving_snake(self):
		for segment_number in range(len(self.snake) - 1, 0, -1):
			new_x = self.snake[segment_number - 1].xcor()
			new_y = self.snake[segment_number - 1].ycor()
			self.snake[segment_number].goto(new_x, new_y)
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		self.head.setheading(RIGHT)
