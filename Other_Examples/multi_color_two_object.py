''' multi_color_two_object.py

Go through multi_color_multiple_points_track.py well before reading this script.

This program tracks only two objects of two different colors (yellow and blue here) to draw to different lines independant of each other. In multi_color_multiple_points_track.py, we get a line connecting those blobs. Here each blob draws its own independent lines. I have uploaded an image "multi_track.png" to show you what i got.

Disadvantage:- It applies only for different colors, not for same color.
		This seems not to be a good method when there is large number of objects.


Brought to you by Abid.K 			mail me at abidrahmank@gmail.com
'''
###############################################################################################################################

import cv
global imghsv

def getthresholdedimg(im):
	
	'''this function take RGB image.Then convert it into HSV for easy colour detection and threshold it with yellow and blue part as white and all other regions as black.Then return that image'''
	global imghsv
	imghsv=cv.CreateImage(cv.GetSize(im),8,3)
	cv.CvtColor(im,imghsv,cv.CV_BGR2HSV)				# Convert image from RGB to HSV
		
	# A little change here. Creates images for blue and yellow (or whatever color you like).
	imgyellow=cv.CreateImage(cv.GetSize(im),8,1)
	imgblue=cv.CreateImage(cv.GetSize(im),8,1)
	
	imgthreshold=cv.CreateImage(cv.GetSize(im),8,1)
	
	cv.InRangeS(imghsv,cv.Scalar(20,100,100),cv.Scalar(30,255,255),imgyellow)	# Select a range of yellow color
	cv.InRangeS(imghsv,cv.Scalar(100,100,100),cv.Scalar(120,255,255),imgblue)	# Select a range of blue color
	cv.Add(imgyellow,imgblue,imgthreshold)
	return imgthreshold

capture=cv.CaptureFromCAM(0)
frame = cv.QueryFrame(capture)
frame_size = cv.GetSize(frame)
test=cv.CreateImage(cv.GetSize(frame),8,3)
img2=cv.CreateImage(cv.GetSize(frame),8,3)
cv.NamedWindow("Real",0)
cv.NamedWindow("Threshold",0)
cv.NamedWindow("final",0)

#	Create two lists to store co-ordinates of blobs
blue=[]
yellow=[]

while(1):
	color_image = cv.QueryFrame(capture)
	imdraw=cv.CreateImage(cv.GetSize(frame),8,3)
	cv.SetZero(imdraw)
	cv.Flip(color_image,color_image,1)
	cv.Smooth(color_image, color_image, cv.CV_GAUSSIAN, 3, 0)
	imgyellowthresh=getthresholdedimg(color_image)
	cv.Erode(imgyellowthresh,imgyellowthresh,None,3)
	cv.Dilate(imgyellowthresh,imgyellowthresh,None,10)
	img2=cv.CloneImage(imgyellowthresh)
	storage = cv.CreateMemStorage(0)
	contour = cv.FindContours(imgyellowthresh, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
	points = []	

#	This is the new part here. ie Use of cv.BoundingRect()
	while contour:
		# Draw bounding rectangles
		bound_rect = cv.BoundingRect(list(contour))
		contour = contour.h_next()
		print contour
		# for more details about cv.BoundingRect,see documentation
		pt1 = (bound_rect[0], bound_rect[1])
		pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
		points.append(pt1)
		points.append(pt2)
		cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 1)
	
	#	Calculating centroids
	
		centroidx=cv.Round((pt1[0]+pt2[0])/2)
		centroidy=cv.Round((pt1[1]+pt2[1])/2)
	
	#	Identifying if blue or yellow blobs and adding centroids to corresponding lists	
		if (20<cv.Get2D(imghsv,centroidy,centroidx)[0]<30):
			yellow.append((centroidx,centroidy))
		elif (100<cv.Get2D(imghsv,centroidy,centroidx)[0]<120):
			blue.append((centroidx,centroidy))

# 		Now drawing part. Exceptional handling is used to avoid IndexError.	After drawing is over, centroid from previous part is #		removed from list by pop. So in next frame,centroids in this frame become initial points of line to draw.		
	try:
		cv.Circle(imdraw,yellow[1],5,(0,255,255))
		cv.Line(imdraw,yellow[0],yellow[1],(0,255,255),3,8,0)
		yellow.pop(0)
	except IndexError:
		print "Just wait for yellow"
		
	try:
		cv.Circle(imdraw,blue[1],5,(255,0,0))
		cv.Line(imdraw,blue[0],blue[1],(255,0,0),3,8,0)
		blue.pop(0)			
	except IndexError:
		print "just wait for blue"	
	cv.Add(test,imdraw,test)

	cv.ShowImage("Real",color_image)
	cv.ShowImage("Threshold",img2)
	cv.ShowImage("final",test)
	if cv.WaitKey(33)==1048603:
		cv.DestroyWindow("Real")
		cv.DestroyWindow("Threshold")
		cv.DestroyWindow("final")
		break
###########################################################################################################################
