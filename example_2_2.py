''' 
Referred to example 2.1 in the book "Learning OpenCV: Computer Vision with the OpenCV Library"

Example 2-2. A simple OpenCV program for playing a video file from disk.

Brought to you by Abid.K	--mail me at abidrahman2@gmail.com
'''
################################################################################################
import cv
cv.NamedWindow("Example2",cv.CV_WINDOW_AUTOSIZE)	
capture=cv.CreateFileCapture("video.avi")	#cv.CreateFileCapture(video_file_path)
while(1):
	frame=cv.QueryFrame(capture)
	cv.ShowImage("Example2",frame)
	c=cv.WaitKey(33)
	if c==1048603:				#cv.WaitKey(33) waits for 33 ms.If a keystroke comes in that time, it is stored in
		break				#variable c. If c=1048603,which corresponds to Esc key, window is destroyed.
cv.DestroyWindow("Example2")
#################################################################################################
# 33 ms is calculated on assumption that around 30 frames are shown in a second. If you want to play video faster, just reduce that time. To play it slower, increase the time. 
