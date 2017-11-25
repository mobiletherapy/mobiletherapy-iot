#!/usr/bin/env python
import cv2, sys
print(0)

# Define constants
DEVICE_NUMBER = 0
print(1)

# Initialize webcam
vc = cv2.VideoCapture(DEVICE_NUMBER)
print(2)

# Check if the webcam works
if vc.isOpened():
	print(3)

	# Try to get the first frame
	retval, frame = vc.read()
	print(4)
else:

	# Exit the program
	print("Exiting")
	sys.exit(1)
# Read in the next frame

retval, frame = vc.read()
print(6)

# Show the frame to the user
cv2.imshow("DragonBoard 410c Workshop", frame)
print(7)

# Exit program after waiting indefinitely for a pressed key
cv2.waitKey(0)
print(8)