# Import the robot control commands from the library
import math
import random
from simulator import robot
import time

L = "L"
R = "R"
F = "F"
B = "B"

def forward(distance):
    robot.motors(1,1,distance)
def backward(distance):
    robot.motors(-1,-1,distance)
def left(angle):
    robot.motors(1,-1,(angle*(1/59.21)))
def right(angle):
    robot.motors(-1,1,(angle*(1/59.21)))
def spin(direction,amount):
    if direction == "L":
        return left(360*amount)
    if direction == "R":
        return right(360*amount)
def seizure(length):
    for i in range (round(length*2.38095238095)):
        for i in range(random.randint(1,10)):
            forward(random.uniform(0.05,0.01))
            backward(random.uniform(0.05,0.01))
        for i in range(random.randint(1,10)):
            left(random.uniform(0.5,2))
            right(random.uniform(0.5,2))

def first_move():
    print(leftdistance)
    print(rightdistance)
    choice1 = float(input("How far should the robot move? "))
    forward(choice1)
    print(leftdistance)
    print(rightdistance)
    choice2 = str(input("What direction should the robot turn? (L or R) "))
    if choice2 == "L":
        print("turning left")
        choice2 = "L"
        left(90)
    elif choice2 == "R":
        print("turning right")
        choice2 = "R"
        right(90)
    print(leftdistance)
    print(rightdistance)
    choice3 = str(input("Should the robot move forward or backward? (F or B) "))
    choice4 = float(input("How far should the robot move? "))
    if choice3 == "B":
        print("moving backward")
        choice3 = "B"
        backward(choice4)
    elif choice3 == "F":
        print("moving forward")
        choice3 = "F"
        forward(choice4)
    print(leftdistance)
    print(rightdistance)
    choice5 = float(input("How many seconds should the robot have a seizure for? "))
    seizure(choice5)
def second_move():
    if choice3 == "B":
        print("moving forward")
        forward(choice4)
    elif choice3 == "F":
        print("moving backward")
        backward(choice4)
    if choice2 == "L":
        print("turning right")
        right(90)
    elif choice2 == "R":
        print("turning left")
        left(90)
    backward(choice1)


leftdistance, rightdistance = robot.sonars()

while leftdistance and rightdistance >= 250:
        print("good to go")
first_move()