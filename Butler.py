#GOPIGO API http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

#imports
from gopigo import *
import time

__author__ = 'Robert Hayek and Keith Neyman'

#Global Variable that says how far butler can get to a wall
STOP_DIST = 50

#print variables
ERROR = "ERROR"
VOLT = "HAZARDOUS VOLTAGE"
STOP = "STOPPING"
MOVE = "MOVING"
YES = "CONTINUING"

class Butler:


    ############
    ######## BASIC STATUS AND METHODS
    ############
    status = {'isMoving' : False, 'servo': 90, 'leftSpeed' : 175, 'rightSpeed' : 175, "distance" : 100}#gets the status of the robot

    def __init__(self):
        print "BUTLERPI IS NOW ON"
        self.status['distance'] = us_dist(15) #update distance  with the current distance through ultrasonic sensor in (mm)
    def stop(self):
        self.status["isMoving"] = False
        print STOP #debugging message (delete later after)
        for x in range(5):
            stop()
            time.sleep(.05)

    def fwd(self):
        self.status['isMoving'] = True
        print MOVE#debugging message (delete later)
        for x in range(5):
            fwd()
            time.sleep(.1)

    #Check if conditions are safe for ButlerPi to continue
    def keepGoing(self):
        if self.status['distance'] < STOP_DIST:
            print "OBSTACLE FOUND CHECKING WEATHER TO STOP"
            self.checkDistance()
            if self.status['distance'] < STOP_DIST:
                print ERROR
                return False
        elif volt() > 14 or volt() < 6: #check voltage and turn off robot is voltage is under 6V or above 14V
            print VOLT
            return False
        else:
            print YES
            return True
    #always watch for obstacles
    def keepWatch(self):
        while self.keepGoing():
            self.checkDistance()
    #check the distance Butler is away from something
    def checkDistance(self):
        self.status['distance'] = us_dist(15)
        print "CHECKING DISTANCE..." + "SOMETHING IS " + str(self.status['distance']) + "mm away"

    def equalizeSpeed(self):
        set_left_speed(500)
        set_right_speed(500)

    def butlerStatus(self):
        print volt()
        print fw_ver()
        print read_status()
        print read_enc_status()
        print read_timeout_status()

    ############
    ######## Dance Methods
    ############
    def spin(self):
        right_rot()
        time.sleep(6)
        self.stop()
        left_rot()
        time.sleep(6)
        self.stop()

    def strobe(self):#Strobe light using the LEDs
        while self.keepGoing():
            led_on(1)
            time.sleep(.10)
            led_off(1)
            led_on(0)
            time.sleep(.10)
            led_off(1)


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



############
######## MAIN APP STARTS HERE
############
butler = Butler()
while butler.keepGoing():
    butler.equalizeSpeed()
    butler.dance()
    butler.fwd()
    butler.strobe
    butler.keepWatch()
butler.stop()
print butler.status
butler.butlerStatus()