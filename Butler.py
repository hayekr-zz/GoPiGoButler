from gopigo import *
import time

__author__ = 'Robert Hayek and Keith Neyman'

class Butler:

    ############
    ############ BASIC STATUS AND METHODS
    ############

    status = {'isMoving' : False, 'servo' : 90, 'leftSpeed' : 175, 'rightSpeed' : 175}

    def __init__(self):
        print "ROBOT IS NOW ON"

    def stop(self):
        self.status["isMoving"] = False
        print "STOPPING" #debugging message (delete later)
        for x in range(3):
            stop()

    def fwd(self):
        self.isMoving = True
        print "MOVING" #debugging message (delete later)
        for x in range(3):
            fwd()


    ############
    ############ COMPLEX METHODS
    ############

    ############
    ############ MAIN APP STARTS HERE
    ############


butler = Butler()
butler.fwd()
butler.sleep(2)
butler.stop()

