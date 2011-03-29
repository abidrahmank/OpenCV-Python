'''	pick_and_track.py

	In track_yellow_draw_line.py, we need to specify the color to track and give corresponding HSV values (It is boring for me). I don't have a yellow blob always. I decided to pick a color myself on the spot from camera. For this, i joined earlier two programmes, mouse_callback.py and track_yellow_draw_line.py. Now i can pick whatever color to track.	
	
Written by Abid. K		-- mail me at abidrahman2@gmail.com	

'''
########################################################################################################

import cv
posx=0
posy=0
global h,s,v,i,im,evente
h,s,v,i,r,g,b,j,evente=0,0,0,0,0,0,0,0,0

#	Mouse callback function	(from earlier mouse_callback.py with little modification)
def my_mouse_callback(event,x,y,flags,param):
	global evente,h,s,v,i,r,g,b,j
	evente=event
	if event==cv.CV_EVENT_LBUTTONDBLCLK:		# Here event is left mouse button double-clicked
		hsv=cv.CreateImage(cv.GetSize(frame),8,3)
		cv.CvtColor(frame,hsv,cv.CV_BGR2HSV)
		(h,s,v,i)=cv.Get2D(hsv,y,x)
		(r,g,b,j)=cv.Get2D(frame,y,x)
		print "x,y =",x,y
		print "hsv= ",cv.Get2D(hsv,y,x)		# Gives you HSV at clicked point
		print "im= ",cv.Get2D(frame,y,x) 	# Gives you RGB at clicked point

#	Thresholding function	(from earlier mouse_callback.py)	
def getthresholdedimg(im):
	'''This function take RGB image.Then convert it into HSV for easy colour detection and threshold it with the given part as white and all other regions as black.Then return that image'''
	imghsv=cv.CreateImage(cv.GetSize(im),8,3)
	cv.CvtColor(im,imghsv,cv.CV_BGR2HSV)
	imgthreshold=cv.CreateImage(cv.GetSize(im),8,1)
	cv.InRangeS(imghsv,cv.Scalar(h,100,10),cv.Scalar(h+10,255,255),imgthreshold)
	return imgthreshold
	
def getpositions(im):
	''' this function returns leftmost,rightmost,topmost and bottommost values of the white blob in the thresholded image'''
	leftmost=0
	rightmost=0
	topmost=0
	bottommost=0
	temp=0
	for i in range(im.width):
		col=cv.GetCol(im,i)
		if cv.Sum(col)[0]!=0.0:
			rightmost=i
			if temp==0:
				leftmost=i
				temp=1		
	for i in range(im.height):
		row=cv.GetRow(im,i)
		if cv.Sum(row)[0]!=0.0:
			bottommost=i
			if temp==1:
				topmost=i
				temp=2	
	return (leftmost,rightmost,topmost,bottommost)
	
capture=cv.CaptureFromCAM(0)
frame=cv.QueryFrame(capture)
test=cv.CreateImage(cv.GetSize(frame),8,3)

# 	Now the selection of the desired color from video.( new)
cv.NamedWindow("pick")
cv.SetMouseCallback("pick",my_mouse_callback)
while(1):
	frame=cv.QueryFrame(capture)
	cv.ShowImage("pick",frame)
	cv.WaitKey(33)
	if evente==7:					# When double-clicked(i.e. event=7), this window closes and opens next window
		break
cv.DestroyWindow("pick")

#	Drawing Part (from earlier program)
cv.NamedWindow("threshold")	
cv.NamedWindow("output")
while(1):
	frame=cv.QueryFrame(capture)
	cv.Flip(frame,frame,1)				# Horizontal flipping for synchronization, comment it to see difference.
	imdraw=cv.CreateImage(cv.GetSize(frame),8,3)	# We make all drawings on imdraw.
	thresh_img=getthresholdedimg(frame)		# We get coordinates from thresh_img
	cv.Erode(thresh_img,thresh_img,None,1)		# Eroding removes small noises
	(leftmost,rightmost,topmost,bottommost)=getpositions(thresh_img)
	if (leftmost-rightmost!=0) or (topmost-bottommost!=0):
		lastx=posx
		lasty=posy
		posx=cv.Round((rightmost+leftmost)/2)
		posy=cv.Round((bottommost+topmost)/2)
		if lastx!=0 and lasty!=0:
			cv.Line(imdraw,(posx,posy),(lastx,lasty),(b,g,r))
			cv.Circle(imdraw,(posx,posy),5,(b,g,r),-1)

	cv.Add(test,imdraw,test)			# Adding imdraw on test keeps all lines there on the test frame. If not, we don't get full drawing, instead we get only that fraction of line at the moment.
	
	cv.ShowImage("threshold",thresh_img)
	cv.ShowImage("output",test)
	if cv.WaitKey(33)==1048603:			# Exit if Esc key is pressed
		break
cv.DestroyWindow("output")				# Releasing window
cv.DestroyWindow("threshold")

######################################################################################################

# Here selection is not real time. If you want to change the color while tracking, you have re-run the program.
# So for a real time tracking, just copy line 70 and paste it as line 82. Then completely comment out line 68-74.Copy line 74 and # paste it at very end of the program. Now run!!!! You select any color whenever you like.!!!!!!!!
