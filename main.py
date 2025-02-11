import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, Lost, Win


screen = Screen()
screen.setup(width=600, height=600)
screen.title('The Turle Crossing')
screen.tracer(0)



player = Player()
scoreboard = Scoreboard()
cars = []
screen.listen()
screen.onkey(player.go, 'space')




game_is_on = True
while game_is_on:



    level_num = 1
    if level_num < 5:

        
        SPEED = 7 + level_num * 2

        
        for i in range(0, random.choice([0, 0, 0, 0, 0, 0, 1, 2])):
            car_i = CarManager(SPEED)
            cars.append(car_i)


        for j in cars:
            j.move()

            if player.ycor() + 22 > j.ycor() and player.ycor() - 22 < j.ycor():
                if player.xcor() + 33 > j.xcor() and player.xcor() - 10 < j.xcor():
                    lost_word = Lost()

                    if screen.textinput("You LOST", "Type 'y' to start again: ") == 'y':
                        screen.clear()
                        screen.tracer(0)
                        player = Player()
                        scoreboard = Scoreboard()
                        cars = []
                        screen.listen()
                        screen.onkey(player.go, 'space')

                    else:
                        game_is_on = False

                    
                    # print(f'bu rengidir: {j.color()}')
                    # print(f'masinin cord lari: {j.xcor(), j.ycor()}')
                    # print(f'playerin cord lari: {player.xcor(), player.ycor()}')

        if player.ycor() > 230:
            screen.clear()
            screen.tracer(0)
            player = Player()
            scoreboard = Scoreboard()
            scoreboard.level_up(level_num)
            cars = []
            screen.listen()
            screen.onkey(player.go, 'space')

            time.sleep(0.1)
            screen.update()
            level_num += 1
                    
    
        

   
                
        
        

    time.sleep(0.1)
    screen.update()




screen.exitonclick()
