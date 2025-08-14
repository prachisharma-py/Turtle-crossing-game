import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Road")
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect the collision with the car.
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()

    # Detect successful crossing.
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
