__author__ = 'Robert Hayek and Keith Neyman'

from gopigo import *
import time

#Global Variable that says how far butler can get to a wall
STOP_DIST = 50

#print variables
error = "ERROR"
volt = "HAZARDOUS VOLTAGE"
on = "BUTLERPI IS NOW ON"
stop = "STOPPING"
move = "MOVING"

class Butler:

    ############
    ######## BASIC STATUS AND METHODS
    ############
    status = {'isMoving' : False, 'servo' : 90, 'leftSpeed' : 175, 'rightSpeed' : 175, "distance" : 100}

    def __init__(self):
        print on
        self.Butler = "Butler" #define self
        self.status['distance'] = us_dist(15) #update distance  with the current distance through ultrasonic sensor in (mm)
    def stop(self):
        self.status["isMoving"] = False
        print stop #debugging message (delete later after)
        for x in range(3):
            stop()

    def fwd(self):
        self.isMoving = True
        print move #debugging message (delete later)
        for x in range(3):
            fwd()
    #Check if conditions are safe for ButlerPi to continue
    def keepGoing(selfself):
        if self.status['distance'] < STOP_DIST:
            return False
        elif volt() > 14 or volt() < 6:
            print volt
            return False
        else:
            return True

    def checkDistance(self):
        self.status['distance'] = us_dist(15)
        print "CHECKING DISTANCE" + "SOMETHING IS " + str(self.status['distance']) + "mm away"

    ############
    ######## COMPLEX METHODS
    ############
    def dance(self):
        print "STARTING DANCE METHOD" #Dance Method
        self.spin()
        self.shuffle()
        self.shakeServo()
        self.rightTurn()
        self.leftTurn()
        self.led()


############
######## MAIN APP STARTS HERE
############
butler = Butler()
while butler.keepGoing():
    butler.checkDistance()
    butler.fwd()
    butler.sleep(2)
    butler.stop()

butler.stop()

