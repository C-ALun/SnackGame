from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    # TODO- 5 Create a scoreboard
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def increare_score(self):
        self.score += 1
        self.update_scoreboard()