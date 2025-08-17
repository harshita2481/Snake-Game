import turtle as t
class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score_record.txt") as sr:
            self.highscore=int(sr.read())
        self.color("purple")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.highscore}", align="center",font=("Courier",20,"normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()

    def save_highscore(self):
        with open("score_record.txt","w") as ssr:
            ssr.write(str(self.highscore))
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=("Courier",20,"normal"))

    def inc_score(self):
        self.score+=1
        self.update_scoreboard()