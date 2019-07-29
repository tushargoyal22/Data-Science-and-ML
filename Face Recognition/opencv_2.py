import cv2

img = cv2.imread('iitmandi.jpg')
gray = cv2.imread('iitmandi.jpg',cv2.IMREAD_GRAYSCALE)


cv2.imshow('IIT MANDI',img)
cv2.imshow('IIT MANDI_gray',gray)


''' waitKey(0) will display the window infinitely until any keypress 
(it is suitable for image display). waitKey(25) will display a frame for 25 ms,
 after which display will be automatically closed. 
 (If you put it in a loop to read videos, 
 it will display the video frame-by-frame)'''

cv2.waitKey(0)
1

# As per the cv2.waitkey docs:

# It returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.
cv2.destroyAllWindows()