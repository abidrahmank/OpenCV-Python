''' example_7_1.py 

Referred to example 7.1 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 7-1. Histogram computation and display

usage: python example_7_1.py <image>

Converted by Abid.K	--mail me at abidrahman2@gmail.com
'''
################################################################################################

import cv,sys

if len(sys.argv)==2 and (cv.LoadImage(sys.argv[1])!=0):
	src=cv.LoadImage(sys.argv[1])
	hsv=cv.CreateImage(cv.GetSize(src),8,3)

	cv.CvtColor(src,hsv,cv.CV_BGR2HSV)
	h_plane=cv.CreateImage(cv.GetSize(src),8,1)
	s_plane=cv.CreateImage(cv.GetSize(src),8,1)
	v_plane=cv.CreateImage(cv.GetSize(src),8,1)

	planes=[h_plane,s_plane]

	cv.CvtPixToPlane(hsv,h_plane,s_plane,v_plane,None)

	h_bins=30
	s_bins=32

#	Build the histogram and compute its contents.

	hist=cv.CreateHist([h_bins,s_bins],cv.CV_HIST_ARRAY,[(0,180),(0,255)],1)
	cv.CalcHist(planes,hist,0,None)
	cv.NormalizeHist(hist,1.0)

#	Create an image to use to visualize our histogram.

	scale=10
	hist_img=cv.CreateImage((h_bins*scale,s_bins*scale),8,3)
	cv.Zero(hist_img)

	max_value=0
	(minvalue,maxvalue,minidx,maxidx)=cv.GetMinMaxHistValue(hist)

	for h in range(h_bins):
		for s in range(s_bins):
			bin_val=cv.QueryHistValue_2D(hist,h,s)
			intensity=cv.Round(bin_val*255/maxvalue)
			cv.Rectangle(hist_img,(h*scale,s*scale),((h+1)*scale-1,(s+1)*scale-1),(intensity,intensity,intensity),cv.CV_FILLED)
			print intensity	

	cv.ShowImage("src",src)
	cv.ShowImage("hsv",hist_img)
	cv.WaitKey(0)

else:
	print "usage : python example_7_1.py <image>"

