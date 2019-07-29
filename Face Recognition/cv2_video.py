# Read a video stream from a camera (Frame by Frame)
import cv2

cap=cv2.VideoCapture(0)

while True:
	# Capture frame-by-frame
	ret,frame = cap.read()# ret = 1 if the video is captured; frame is the image
# This code initiates an infinite loop (to be broken later by a break statement),
# where we have ret and frame being defined as the cap.read(). Basically,
# ret is a boolean regarding whether or not there was a return at all,
# at the frame is each frame that is returned. If there is no frame, 
# you wont get an error, you will get None.
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    

	if ret ==False:
		continue
 # Display the resulting image
	cv2.imshow("Video Frame",frame)
	cv2.imshow("Gray Frame",gray_frame)


	#Wait for user input- q,then u will stop
	# press q to quit
	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


# This releases the webcam, then closes all of the imshow() windows.


# 0xFF is a hexadecimal constant which is 11111111 in binary. 
# By using bitwise AND (&) with this constant,it leaves only the last 8 bits
# of the original (in this case, whatever cv2.waitKey(0) is).