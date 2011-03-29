'''	 track_yellow_draw_line.py

This program just track a yellow object in front of camera and draws a yellow line according to movement of the object.

Written by Abid.K	--mail me at abidrahman2@gmail.com	'''

################################################################################################

import cv
posx=0
posy=0

def getthresholdedimg(im):
	'''this function take RGB image.Then convert it into HSV for easy colour detection and threshold it with yellow part as white and all other regions as black.Then return that image'''
	imghsv=cv.CreateImage(cv.GetSize(im),8,3)
	cv.CvtColor(im,imghsv,cv.CV_BGR2HSV)				# Convert image from RGB to HSV
	imgthreshold=cv.CreateImage(cv.GetSize(im),8,1)
	cv.InRangeS(imghsv,cv.Scalar(20,100,100),cv.Scalar(30,255,255),imgthreshold)	# Select a range of yellow color
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
cv.NamedWindow("output")

while(1):
	frame=cv.QueryFrame(capture)
	cv.Flip(frame,frame,1)
	imdraw=cv.CreateImage(cv.GetSize(frame),8,3)	# we make all drawings on imdraw.
	imgyellowthresh=getthresholdedimg(frame)	# we get coordinates from imgyellowthresh
	cv.Erode(imgyellowthresh,imgyellowthresh,None,1)# eroding removes small noises
	(leftmost,rightmost,topmost,bottommost)=getpositions(imgyellowthresh)
	if (leftmost-rightmost!=0) or (topmost-bottommost!=0):
		lastx=posx
		lasty=posy
		posx=cv.Round((rightmost+leftmost)/2)
		posy=cv.Round((bottommost+topmost)/2)
		if lastx!=0 and lasty!=0:
			cv.Line(imdraw,(posx,posy),(lastx,lasty),(0,255,255))
			cv.Circle(imdraw,(posx,posy),5,(0,255,255),-1)

	cv.Add(test,imdraw,test)			# adding imdraw on test keeps all lines there on the test frame. If not, we don't get full drawing, instead we get only that fraction of line at the moment.
	cv.ShowImage("output",test)
	if cv.WaitKey(33)==1048603:			# exit if Esc key is pressed
		break
cv.DestroyWindow("output")				# releasing window
#######################################################################################################
## Please try mouse_callback.py and then read pick_and_track.py
