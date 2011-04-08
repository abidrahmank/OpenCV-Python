''' 
Referred to example 4-1 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 4-1. Toy program for using a mouse to draw boxes on the screen

Converted to Python by Abid.K	--mail me at abidrahman2@gmail.com
'''
########################################################################################

import cv
#	cvRect	box=[box.x,box.y,box.width,box.height]
box=[0,0,0,0]

#	creating mouse callback function
def my_mouse_callback(event,x,y,flags,param):
	global drawing_box
	if event==cv.CV_EVENT_LBUTTONDOWN:
		drawing_box=True
		[box[0],box[1],box[2],box[3]]=[x,y,0,0]
		print box[0]

	if event==cv.CV_EVENT_LBUTTONUP:
		drawing_box=False
		if box[2]<0:
			box[0]+=box[2]
			box[2]*=-1
		if box[3]<0:
			box[1]+=box[3]
			box[3]*=-1
			
	if event==cv.CV_EVENT_MOUSEMOVE:
		if (drawing_box==True):
			box[2]=x-box[0]
			box[3]=y-box[1]	
		
# 	function to draw the rectangle, added flag -1 to fill rectangle. If you don't want to fill, just delete it.		
def draw_box(img,box):
	cv.Rectangle(img,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),(255,0,0),-1)

#	main program	
drawing_box=False
image=cv.CreateImage((200,200),cv.IPL_DEPTH_8U,3)
#	make a clone of image
temp=cv.CloneImage(image)

cv.NamedWindow("Box Example")
cv.SetMouseCallback("Box Example",my_mouse_callback,image)
while(1):
	cv.Copy(image,temp)
	if drawing_box==True:
		draw_box(temp,box)
	cv.ShowImage("Box Example",temp)
	if cv.WaitKey(20)%0x100==27:break
	
cv.DestroyWindow("Box Example")
###################################################################################################
## Also refer to examples in the folder Other_examples/############################################
###################################################################################################
