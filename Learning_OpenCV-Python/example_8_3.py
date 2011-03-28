''' 
Referred to example 8-3 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 8-3. Finding and drawing contours on an input image

Converted to Python by Abid.K	--mail me at abidrahman2@gmail.com
'''
########################################################################################

import cv,sys

#	this time input is given at commandline like this: python example_8_3.py <imagename>
filename=sys.argv[1]

#	load grayscale image
img=cv.LoadImage(filename,cv.CV_LOAD_IMAGE_GRAYSCALE)
#	load grayscale image for thresholding
img_th=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,1)
# 	create image for displaying 3-channel
img_adth=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,3)
# 	create a temperory 3-channel image
temp=cv.CreateImage((img.width,img.height),cv.IPL_DEPTH_8U,3)

#	creating windows
cv.NamedWindow("Image with Contour")
cv.NamedWindow("Input Image")
cv.NamedWindow("Contour")


#	thresholding 
cv.Threshold(img,img_th,127,255,cv.CV_THRESH_BINARY_INV)

#	finding contours
mem=cv.CreateMemStorage()
nc=cv.FindContours(img_th,mem,cv.CV_RETR_LIST,cv.CV_CHAIN_APPROX_SIMPLE,(0,0))	#try all four values of third flag
print len(nc)

#	Drawing contours, external contact red color, and internal contours green color
for c in nc:
	cv.DrawContours(img_adth,nc,cv.CV_RGB(255,0,0),cv.CV_RGB(0,255,0),2,2,8) # change max_value, sixth flag and check output

cv.CvtColor(img,temp,cv.CV_GRAY2BGR)
cv.Add(temp,img_adth,temp)

#	Displaying images
cv.ShowImage("Input Image",img)
cv.ShowImage("Contour",img_adth)
cv.ShowImage("Image with Contour",temp)

#	Being clean and tidy
if cv.WaitKey(0) % 0x100 == 27:
	cv.DestroyWindow("Input Image")
	cv.DestroyWindow("Contour")
	cv.DestroyWindow("Image with Contour")

####################################################################################################
