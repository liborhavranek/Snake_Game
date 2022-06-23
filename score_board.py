from turtle import Turtle

class Score_Board(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.penup()
		self.goto(-50, 270)
		self.color("white")
		self.hideturtle()
		self.update_score_board()



	def update_score_board(self):
		self.write(f"Score: {self.score}", align='left', font=('Arial', 20, 'normal'))

	def game_over(self):
		self.goto(-80, 0)
		self.write(f"GAME OVER! SCORE: {self.score}", align='left', font=('Arial', 20, 'normal'))

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_score_board()
