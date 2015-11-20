__author__ = 'Robert Hayek and Keith Neyman'

file = open( "/dev/input/mice", "rb" );
speed=150

debug = 0	#Print raw values when debugging

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

	if flag==1: #If left or right mouse not pressed, move forward
		fwd()
		flag=0
	if l:		#If left mouse buton pressed, turn left
		left()
		flag=1
	if m:		#If middle mouse button pressed, stop
		stop()
	if r:		#If right mouse button presses, turn right
		right()
		flag=1
	if l and r:	#If both the left and right mouse buttons pressed, go back
		bwd()