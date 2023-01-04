from turtle import Turtle

ALIGNMENT = "center"
FONT_SCORE = ("Verdana", 18, "normal")
FONT_GAME_OVER = ("Verdana", 28, "normal")


class Scoreboard(Turtle):

    def __init__(self, nick1, nick2):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.name1 = nick1
        self.name2 = nick2
        self.write(f"{self.name1}: {self.l_score}      {self.name2}: {self.l_score}", align=ALIGNMENT, font=FONT_SCORE)

    def refresh(self):
        self.clear()
        self.write(f"{self.name1}: {self.l_score}      {self.name2}: {self.r_score}", align=ALIGNMENT, font=FONT_SCORE)

    def l_point(self):
        self.l_score += 1
        self.refresh()

    def r_point(self):
        self.r_score += 1
        self.refresh()

    def p1_score(self):
        return self.l_score

    def p2_score(self):
        return self.r_score

    def finish(self, color, who):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT_GAME_OVER)
        self.penup()
        self.goto(0, -40)
        self.color(color)
        self.pendown()
        self.write(f"{who} wins!", align=ALIGNMENT, font=FONT_GAME_OVER)



