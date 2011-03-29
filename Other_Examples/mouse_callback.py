''' mouse_callback.py

A simple example about generating mouse callback function. It is targeted on an absolute beginner.This program just print the coordinates in the terminal when you double click at any point on the window.

Written by Abid.K	--mail me at abidrahman2@gmail.com

'''
########################################################################################

import cv
im=cv.CreateImage((400,400),cv.CV_8UC3,1)

#cv.Not(im,im)
#f=cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX,1.0,1.0,1.0,1,8)
cv.NamedWindow("Display",cv.CV_WINDOW_AUTOSIZE)

#	this is the method to define a mouse callback function. Several events are given in OpenCV documentation
def my_mouse_callback(event,x,y,flags,param):
	if event==cv.CV_EVENT_LBUTTONDBLCLK:		# here event is left mouse button double-clicked
		print x,y
		
		#text="{0},{1}".format(x,y)
		#cv.PutText(im,text,(x+5,y+5),f,cv.RGB(0,255,255))

cv.SetMouseCallback("Display",my_mouse_callback,im)	#binds the screen,function and image

while(1):
	cv.ShowImage("Display",im)
	if cv.WaitKey(15)%0x100==27:break		# waiting for clicking escape key
cv.DestroyWindow("Display")
########################################################################################

### Remove comment sign on lines 13,14,22,23 and run program. Much more interesting!!!!!!!
### If you are done with this code, next try example_4_1.py. It will give much more concepts... Thank you
### Also read track_yellow_draw_line.py and then try pick_and_track.py
