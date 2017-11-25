#!/usr/bin/env python
import cv2, sys

# Define constants
DEVICE_NUMBER = 2
print("Setting configuration values")

# Initialize webcam
vc = cv2.VideoCapture(DEVICE_NUMBER)
print("Creating image capture context")

# Check if the webcam works
if vc.isOpened():

	# Try to get the first frame
	retval, frame = vc.read()
	print("Reading in image")
else:

	# Exit the program
	print("Exiting due to competing context")
	sys.exit(1)
# Read in the next frame

retval, frame = vc.read()
print("Reading additional frame")

# Show the frame to the user
cv2.imshow("Therapist Visual Feedback", frame)
print("Displaying image")

# Exit program after waiting indefinitely for a pressed key
cv2.waitKey(0)
print("Exiting")
sys.exit(0)