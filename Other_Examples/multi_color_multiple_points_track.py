'''multi_color_multiple_points_track.py

In single_color_multiple_points_track.py, we tracked multiple points of same color. Now you can see with a very small modification, we can track multiple points with different colors. It is very simple.

I have just commented out draw_line part. If you want uncomment it. Then you will get a polygon connecting all these points.
For example, a triangle if only three points ( like i got in multi_color.png)

	
Written by Abid.K	--mail me at abidrahman2@gmail.com  '''

###############################################################################################################################

import cv
posx=0
posy=0
def getthresholdedimg(im):
	'''this function take RGB image.Then convert it into HSV for easy colour detection and threshold it with yellow part as white and all other regions as black.Then return that image'''
	imghsv=cv.CreateImage(cv.GetSize(im),8,3)
	cv.CvtColor(im,imghsv,cv.CV_BGR2HSV)				# Convert image from RGB to HSV
		
	# A little change here. Creates images for green,blue and yellow (or whatever color you like).
	imgyellow=cv.CreateImage(cv.GetSize(im),8,1)
	imgblue=cv.CreateImage(cv.GetSize(im),8,1)
	imggreen=cv.CreateImage(cv.GetSize(im),8,1)
	
	imgthreshold=cv.CreateImage(cv.GetSize(im),8,1)
	
	cv.InRangeS(imghsv,cv.Scalar(85,100,100),cv.Scalar(95,255,255),imggreen)
	cv.InRangeS(imghsv,cv.Scalar(20,100,100),cv.Scalar(30,255,255),imgyellow)	# Select a range of yellow color
	cv.InRangeS(imghsv,cv.Scalar(100,100,100),cv.Scalar(120,255,255),imgblue)	# Select a range of blue color
#	Add everything
	cv.Add(imgyellow,imgblue,imgthreshold)
	cv.Add(imgthreshold,imggreen,imgthreshold)
	return imgthreshold


capture=cv.CaptureFromCAM(0)
frame = cv.QueryFrame(capture)
frame_size = cv.GetSize(frame)
grey_image = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)
test=cv.CreateImage(cv.GetSize(frame),8,3)
img2=cv.CreateImage(cv.GetSize(frame),8,3)
cv.NamedWindow("Real",0)
cv.NamedWindow("Threshold",0)
#cv.NamedWindow("Final",0)
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


	while contour:
		# Draw bounding rectangles
		bound_rect = cv.BoundingRect(list(contour))
		contour = contour.h_next()
		
		# for more details about cv.BoundingRect,see documentation
		pt1 = (bound_rect[0], bound_rect[1])
		pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
		points.append(pt1)
		points.append(pt2)
		cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 2)

############### Line drawing part

#		lastx=posx
#		lasty=posy
#		posx=cv.Round((pt1[0]+pt2[0])/2)
#		posy=cv.Round((pt1[1]+pt2[1])/2)
#		if lastx!=0 and lasty!=0:
#			cv.Line(imdraw,(posx,posy),(lastx,lasty),(255,255,0),3,8,0)
#			cv.Circle(imdraw,(posx,posy),5,(0,255,255),-1)

	cv.Add(test,imdraw,test)

	cv.ShowImage("Real",color_image)
	cv.ShowImage("Threshold",img2)
	cv.ShowImage("Final",test)
	if cv.WaitKey(33)==1048603:
		cv.DestroyWindow("Real")
		cv.DestroyWindow("Threshold")
#		cv.DestroyWindow("Final")
		break
