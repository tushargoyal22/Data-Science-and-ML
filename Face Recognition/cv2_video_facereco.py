# Read a video stream from a camera (Frame by Frame)
import cv2

cap=cv2.VideoCapture(0)
face_cascade =cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
while True:
	# Capture frame-by-frame
	ret,frame = cap.read()
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


 	# Display the resulting image
 	#let's detect multiscale (some images may be closer to camera than others) images
 	if ret ==False:
 		continue
 	
	faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

	#print the number of faces found
	print('Faces found: ', len(faces)


# Next, let's loop over the list of faces (rectangles) it returned and drew those rectangles using yet another built-in OpenCV rectangle function on our original colored image to see if it found the right faces:

	for (x, y, w, h) in faces:

    	cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

	cv2.imshow("Video Frame",frame)

	#Wait for user input- q,then u will stop
	# press q to quit
	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()