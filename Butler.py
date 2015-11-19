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

servo(90)

class Pigo:


    ############
    ######## BASIC STATUS AND METHODS
    ############
    status = {'isMoving' : False, 'servo': 90, 'leftSpeed' : 175, 'rightSpeed' : 175, "distance" : 100}#gets the status of the robot
    def __init__(self):
        threading.Thread.__init__(self)
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
        while butler.keepGoing():
            for x in range(5):
                right_rot()
                time.sleep(6)
                self.stop()
                left_rot()
                time.sleep(6)
                self.stop()

    def strobe(self):# Strobe light using the LEDs
        while butler.keepGoing():
            for x in range(5):
            led_on(1)
            time.sleep(.10)
            led_off(1)
            # led_on(0)
            time.sleep(.10)
            led_off(1)

    def shuffle(self):
        while butler.keepGoing():
            for x in range(5):
                right_rot()
                time.sleep(.10)
                left_rot()
                time.sleep(.10)

    def rightTurn(self):
        while butler.keepGoing():
            for x in range(3):
                fwd()
                right_rot(50)
                fwd()

    def leftTurn(self):
        while butler.keepGoing():
            for x in range(3):
                fwd()
                time.sleep(.10)
                left_rot(50)
                fwd()
                time.sleep(.10)

    def specialMethod(self):
        while butler.keepGoing():
            for x in range(5):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            increase_speed()
            bwd()
            enc_tgt(1,1,72)
            fwd()
            servo(45)
            servo(20)
            servo(20)
            servo(20)
            servo(40)
            stop()



    #############
    ######## COMPLEX METHODS
    #############
    def servoSweep(self):
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)

    def dance(self):
        print "STARTING DANCE METHOD" #Dance Method
        print "Spin!"
        self.spin()
        print "Shuffle!"
        self.shuffle()
        print "Sweep!"
        self.servoSweep()
        print "Turn to the right"
        self.rightTurn()
        print "Turn to the left!"
        self.leftTurn()
        print "SPECIAL MOVE!"
        self.specialMethod()

############
######## MAIN APP STARTS HERE
############
butler = Pigo()
while butler.keepGoing():
    butler.keepGoing()
    butler.equalizeSpeed()
    butler.dance()
    butler.strobe()
    butler.keepWatch()
butler.stop()
print butler.status
butler.butlerStatus()