from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f'Level: {self.level}', False, align='left', font=FONT)


    def level_up(self, times):
        self.clear()
        self.level += times
        self.write(f'Level: {self.level}', False, align='left', font=FONT)

class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        

class Lost(Write):
    def __init__(self):
        super().__init__()
        self.write(f'YOU LOST', False, align='center', font=("Courier", 35, "normal"))

class Win(Write):
    def __init__(self):
        super().__init__()
        self.write(f'Congrats! You WON!!', False, align='center', font=("Courier", 35, "normal"))


