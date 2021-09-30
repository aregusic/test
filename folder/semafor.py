import time
import os
import turtle

screen = turtle.Turtle()
screen.fillcolor('red')
screen.begin_fill()
screen.circle(100)
screen.end_fill()

red_status = False
yellow_status = False 
green_status = False

red_light_time = 3
yellow_light_time = 2
green_light_time = 2.5

os.system('cls')

def print_semafor(red_status, yellow_status, green_status):
    print(f'''
    red - {red_status}
    yellow - {yellow_status}
    green - {green_status}
    ''')

while True:
    red_status = True
    yellow_status = False
    green_status = False
    print_semafor(red_status, yellow_status, green_status)
    time.sleep(red_light_time)
    os.system('cls')

    red_status = True
    yellow_status = True
    green_status = False
    print_semafor(red_status, yellow_status, green_status)
    time.sleep(yellow_light_time)
    os.system('cls')

    red_status = False
    yellow_status = False
    green_status = True
    print_semafor(red_status, yellow_status, green_status)
    time.sleep(green_light_time)
    os.system('cls')
