''' 
Referred to example 5-4 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 5-4. Threshold versus adaptive threshold

Converted to Python by Abid.K	--mail me at abidrahman2@gmail.com
'''
########################################################################################

import cv,sys

#	this time input is given at commandline like this: python example_5_4.py <imagename>
filename=str(sys.argv[1])

#	load grayscale image
img=cv.LoadImage(filename,cv.CV_LOAD_IMAGE_GRAYSCALE)
img_th=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,1)
img_adth=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,1)
cv.NamedWindow("Input Image")
cv.NamedWindow("Threshold")
cv.NamedWindow("Adaptive Threshold")

#	thresholding and adaptive threshold
cv.Threshold(img,img_th,100,255,cv.CV_THRESH_BINARY_INV)
cv.AdaptiveThreshold(img,img_adth,255,cv.CV_ADAPTIVE_THRESH_MEAN_C,cv.CV_THRESH_BINARY_INV,3,5)

cv.ShowImage("Input Image",img)
cv.ShowImage("Threshold",img_th)
cv.ShowImage("Adaptive Threshold",img_adth)
if cv.WaitKey(0)% 0x100==27:	#	waiting for esc key
	cv.DestroyWindow("Input Image")
	cv.DestroyWindow("Threshold")
	cv.DestroyWindow("Adaptive Threshold")

