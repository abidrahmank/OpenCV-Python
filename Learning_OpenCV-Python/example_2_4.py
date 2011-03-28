'''
Referred to example 2.4 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 2-4. Loading and then smoothing an image before it is displayed on the screen

Brought to you by Abid.K	--mail me at abidrahman2@gmail.com
'''
########################################################################################
import cv
image=cv.LoadImage("test.jpg")
#	create windows to show input and output images
cv.NamedWindow("Example4-in")
cv.NamedWindow("Example4-out")
cv.ShowImage("Example4-in",image)
#	create an image to hold smoothed output
out=cv.CreateImage(cv.GetSize(image),cv.IPL_DEPTH_8U,3)
#	smoothing--> cv.Smooth(input,output,smooth_type,parameter1,parameter2)
cv.Smooth(image,out,cv.CV_GAUSSIAN,3,3)
cv.ShowImage("Example4-out",out)
cv.WaitKey(0)
# 	be clean
cv.DestroyWindow("Example4-in")
cv.DestroyWindow("Example4-out")
#########################################################################################
