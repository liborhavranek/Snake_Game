from turtle import Turtle
import random


class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(1)
		self.color("red")
		self.speed("fastest")
		self.refresh_food()

	def refresh_food(self):
		x_random = random.randint(-250, 250)
		y_random = random.randint(-250, 250)
		self.goto(x_random, y_random)

