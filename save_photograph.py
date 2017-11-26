#!/usr/bin/env python
import cv2, sys, config, json, binascii, os
from imgurpython import ImgurClient
from datetime import datetime

client = ImgurClient(config.client_id, config.client_secret, config.access_token, config.refresh_token)

def upload_image(path):
	"Upload a picture of a kitten. We don't ship one, so get creative!"

	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'name':  'Face captured {0}'.format(datetime.now()),
		'title': 'Face captured {0}'.format(datetime.now()),
		'description': 'Face captured {0}'.format(datetime.now())
	}

	print("Uploading image...")
	image = client.upload_from_path(path, config=config, anon=True)
	print("Done")
	print()

	return image

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
	print("Reading in image for test")
	retval, frame = vc.read()
else:

	# Exit the program
	print("Exiting due to competing context")
	sys.exit(1)
# Read in the next frame


def Capture_Image():
	img_name = "a" + binascii.b2a_hex(os.urandom(15)) + IMAGE_FILE
	print("Reading in image")
	retval, frame = vc.read()
	retval, frame = vc.read()
	retval, frame = vc.read()
	retval, frame = vc.read()
	retval, frame = vc.read()
	retval, frame = vc.read()
	retval, frame = vc.read()

	print("Writing image file")
	# Save the frame as an image file
	cv2.imwrite(img_name, frame)
	# Read the output file
	img = cv2.imread(img_name)

	print("Sending image")
	results = upload_image(img_name)

	# Show the frame to the user
	print("Displaying image")
	cv2.imshow("Therapist Visual Feedback", img)

	print("Saved image at " + results['link'])
	return results['link']