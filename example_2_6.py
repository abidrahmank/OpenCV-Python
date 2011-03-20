''' 
Referred to example 2.6 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 2-6. The Canny edge detector writes its output to a single channel (grayscale) image

Brought to you by Abid.K	--mail me at abidrahman2@gmail.com
'''
########################################################################################
import cv
image=cv.LoadImage("test.jpg")
cv.NamedWindow("input")
cv.NamedWindow("output")

def doCanny(image,lowThresh,highThresh,aperture):
# 	i have changed code a little bit from text book. With example in text book, you have to load 		grayscale image. But now you can load any image, no matter if RGB or GRAYSCALE
#	output image with single channel
	out=cv.CreateImage(cv.GetSize(image),cv.IPL_DEPTH_8U,1)
#	canny only handles grayscale images. So convert RGB to grayscale
	if image.nChannels != 1:
		cv.CvtColor(image,out,cv.CV_RGB2GRAY)
		cv.Canny(out,out,lowThresh,highThresh,aperture)
	else:
		cv.Canny(image,out,lowThresh,highThresh,aperture)
	return out

image=cv.LoadImage("test.jpg")
#	some arbitrary values are given as parameters
out=doCanny(image,100,200,3)
cv.ShowImage("input",image)
cv.ShowImage("output",out)
cv.WaitKey(0)
cv.DestroyWindow("input")
cv.DestroyWindow("output")
########################################################################################
