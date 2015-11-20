#GOPIGO API http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

__author__ = 'Robert Hayek and Keith Neyman'

file = open( "/dev/input/mice", "rb" );
########
####Variables
########
speed = 150
debug = 0

def getMouseEvent():
	buf = file.read(3)
	button = ord( buf[0] )
	bLeft = button & 0x1
	bMiddle = ( button & 0x4 ) > 0
	bRight = ( button & 0x2 ) > 0
	x,y = struct.unpack( "bb", buf[1:] )
	if debug:
		print ("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft,bMiddle,bRight, x, y) )
	return [bLeft,bMiddle,bRight,x,y]

flag=0
print "Press Enter to start"
a=raw_input()	#Wait for an input to start
set_speed(speed)
stop()
while( 1 ):
	[l,m,r,x,y]=getMouseEvent()	#Get the inputs from the mouse
	if debug:
		print l,m,r,x,y
	print x,"\t",y

	#If there is a significant mouse movement Up (positive y-axis)
	if y >20:
		fwd()	#Move forward

	#If there is a significant mouse movement Down (negative y-axis)
	elif y<-20:
		bwd()	#Move Back

	#If there is a significant mouse movement Left (positive x-axis)
	elif x<-20:
		left()	#Move left

	#If there is a significant mouse movement Right (negative x-axis)
	elif x>20:
		right()	#Move Right

	#Stop the GoPiGo if left mouse button pressed
	if l:
		stop()
	time.sleep(.01)