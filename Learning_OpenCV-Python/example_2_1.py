''' 
Referred to example 2.1 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

A simple OpenCV program that loads an image from disk and displays it on the screen.
'''

import cv
img=cv.LoadImage("test.jpg")
# cv.LoadImage(image path,[flags)
# To load image in grayscale,add a flag cv.CV_LOAD_IMAGE_GRAYSCALE in the bracket above
cv.NamedWindow("Example1",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("Example1",img)
cv.WaitKey(0)			#the program indefinitely waits for a positive keystroke, or give time in milliseconds instead of 0
cv.DestroyWindow("Example1")
