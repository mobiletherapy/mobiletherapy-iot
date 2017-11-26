#!/usr/bin/env python
import cv2, sys

# Define constants
print("Setting configuration values")
DEVICE_NUMBER = 2
IMAGE_FILE = "output.jpg"

# Initialize webcam
print("Creating image capture context")
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcam works
if vc.isOpened():

	# Try to get the first frame
	print("Reading in image")
	retval, frame = vc.read()
else:

	# Exit the program
	print("Exiting due to competing context")
	sys.exit(1)
# Read in the next frame

print("Reading additional frame")
retval, frame = vc.read()

print("Writing image file")
# Save the frame as an image file
cv2.imwrite(IMAGE_FILE, frame)
# Read the output file
img = cv2.imread(IMAGE_FILE)

# Show the frame to the user
print("Displaying image")
cv2.imshow("Therapist Visual Feedback", img)

# Exit program after waiting indefinitely for a pressed key
cv2.waitKey(0)
print("Exiting")
sys.exit(0)