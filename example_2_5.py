''' 
Referred to example 2.1 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 2-5. Using cv.PyrDown() to create a new image that is half the width and height of the input
image

Brought to you by Abid.K	--mail me at abidrahman2@gmail.com
'''
########################################################################################
import cv
def doPyrDown(image,filter_type=cv.CV_GAUSSIAN_5x5):
#	assert if width and height of new image is not even
	assert (image.width%2==0 and image.height%2==0)
#	creating a new image of half the size of input to hold output
	out=cv.CreateImage((image.width/2,image.height/2),image.depth,image.nChannels)
#	Downsamples the image
	cv.PyrDown(image,out)
	return out

image=cv.LoadImage("girl.jpg")
out=doPyrDown(image,cv.CV_GAUSSIAN_5x5)
cv.NamedWindow("input")
cv.NamedWindow("output")
cv.ShowImage("input",image)
cv.ShowImage("output",out)
cv.WaitKey(0)
cv.DestroyWindow("input")
cv.DestroyWindow("output")
######################################################################################
