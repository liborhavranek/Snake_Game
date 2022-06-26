from turtle import Turtle

class Score_Board(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		with open("data.txt") as data:
			self.high_score = int(data.read())
		self.penup()
		self.goto(-50, 270)
		self.color("white")
		self.hideturtle()
		self.update_score_board()



	def update_score_board(self):
		self.clear()
		self.write(f"Score: {self.score} High score {self.high_score}", align='left', font=('Arial', 20, 'normal'))


	def reset(self):
		"""this way save high score and reset the score """
		if self.score > self.high_score:
			self.high_score = self.score
			with open("data.txt", mode="w") as data:
				data.write(f"{self.high_score}")

		self.score = 0
		self.update_score_board()
	# def game_over(self):
	# 	self.goto(-80, 0)
	# 	self.write(f"GAME OVER! SCORE: {self.score}", align='left', font=('Arial', 20, 'normal'))

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_score_board()
