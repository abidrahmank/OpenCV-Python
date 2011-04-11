'''single_color_multiple_points_track.py

	Before reading this code make sure you are thorough with track_yellow_draw_line.py and example_8_3.py. It is a combination of both plus use of new function and new ideas. This code shows how you can use contours to track multiple object. A new function cv.BoundingRect also used here to draw bounding rectangles of contours.

	In track_yellow_draw_line.py, we tracked a single yellow object. And we didn't use contours there. Here we track multiple yellow objects. ie the name, single_color_multiple_points_track.py. That is the main function.
	
	Plus, as earlier, i have kept drawing function also there, to see a nice output. And i have uploaded a picture scmpt.png to show you what output i got.
	
	Always remember, i am following an hierarchy from simple to complex, and i always put path above. Follow it. 
	
Written by Abid.K	--mail me at abidrahman2@gmail.com  '''

###############################################################################################################################

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


capture=cv.CaptureFromCAM(0)
frame = cv.QueryFrame(capture)
frame_size = cv.GetSize(frame)
grey_image = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)
test=cv.CreateImage(cv.GetSize(frame),8,3)
cv.NamedWindow("Real")
cv.NamedWindow("Threshold")
while(1):
	color_image = cv.QueryFrame(capture)
	imdraw=cv.CreateImage(cv.GetSize(frame),8,3)
	cv.Flip(color_image,color_image,1)
	cv.Smooth(color_image, color_image, cv.CV_GAUSSIAN, 3, 0)
	imgyellowthresh=getthresholdedimg(color_image)
	cv.Erode(imgyellowthresh,imgyellowthresh,None,3)
	cv.Dilate(imgyellowthresh,imgyellowthresh,None,10)

	storage = cv.CreateMemStorage(0)
	contour = cv.FindContours(imgyellowthresh, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
	points = []	

#	This is the new part here. ie Use of cv.BoundingRect()
	while contour:
		# Draw bounding rectangles
		bound_rect = cv.BoundingRect(list(contour))
		contour = contour.h_next()
		
		# for more details about cv.BoundingRect,see documentation
		pt1 = (bound_rect[0], bound_rect[1])
		pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
		points.append(pt1)
		points.append(pt2)
		cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 1)
		lastx=posx
		lasty=posy
		posx=cv.Round((pt1[0]+pt2[0])/2)
		posy=cv.Round((pt1[1]+pt2[1])/2)
		if lastx!=0 and lasty!=0:
			cv.Line(imdraw,(posx,posy),(lastx,lasty),(0,255,255))
			cv.Circle(imdraw,(posx,posy),5,(0,255,255),-1)
	cv.Add(test,imdraw,test)

	cv.ShowImage("Real",color_image)
	cv.ShowImage("Threshold",test)
	if cv.WaitKey(33)==1048603:
		cv.DestroyWindow("Real")
		cv.DestroyWindow("Threshold")
		break
