from gopigo import *
import time

__author__ = 'Robert Hayek and Keith Neyman'

class Pigo:

    ############
    ############ BASIC STATUS AND METHODS
    ############
    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'rightspeed' : 175}


    def __init__(self):
        print "ON"

    def stop(self):
        self.isMoving = False
        while stop() !=1
            time.sleep(.1)
            print "ERROR"
    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.slepp(.1)
            print "ERROR"


    ############
    ############ COMPLEX METHODS
    ############

    ############
    ############ MAIN APP STARTS HERE
    ############


butler = Pigo()
butler.fwd()
butler.sleep(2)
butler.stop()

