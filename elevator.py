#!/usr/bin/python
# Filename: elevator.py

import sys
import os
import time
import ichk
from Queue import PriorityQueue as Q

MAX_CAPACITY = 10
BUILDING_HEIGHT = 20
MIN_FLOOR = 1

def showBuilding(floor):
    os.system('clear')
    for x in range(BUILDING_HEIGHT,0,-1):
        if x==(floor):
            print '||----[0]----||', x
        else:
            print '||-----------||', x 


def isInt(x):
    try:
        x = int(x)
        return true
    except:
        return False


def getFloorChoice():
    try:
        floor = []
        while True:
            input = raw_input('Please enter your floor choice: ')
            int(input)
            if not ((ichk.isInt(input)) and (int(input)<=BUILDING_HEIGHT) and (int(input) >= MIN_FLOOR)):
                print("Invalid floor")
            else:
                floor.append(int(input))
    except ValueError:
        return floor
def go_down(floor, cur_floor):
    print("down")

def goToFloor(floor, cur_floor):
    if floor < cur_floor:
        for d in range(cur_floor, floor - 1, -1):
            showBuilding(d)
            time.sleep(.5)
    elif cur_floor < floor:
        print("up")
        for x in range(cur_floor, floor + 1, 1):
            showBuilding(x)
            time.sleep(.5)
    else:
        time.sleep(.5)
def exe_requests(requests, cur_floor):
     for i in range(len(requests)):
        goToFloor(requests[i], cur_floor)
        cur_floor = requests[i]

try:
    input = raw_input("Please enter number of floors: ")
    if ichk.isInt(input):
        BUILDING_HEIGHT = int(input)
    else:
        while not ichk.isInt(input):
            input = raw_input("Please enter a valid number of floors: ")
        BUILDING_HEIGHT = int(input)
    showBuilding(1)
    floor = 0
    cur_floor = 1
    while True:
        floors=getFloorChoice()
        exe_requests(floors, cur_floor)
except KeyboardInterrupt:
    print("\nExitting elevator simulator....\n")
    sys.exit()
# End of elevator.py
