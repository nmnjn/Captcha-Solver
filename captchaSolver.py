from keras.models import load_model
from Helpers.helpers import resize_to_fit
import urllib.request
import numpy as np
import imutils
import cv2
import pickle

MODEL = "model.hdf5"
LABELS = "labels.dat"

model = load_model(MODEL)

file = open(LABELS, 'rb')
labels = pickle.load(file)
file.close()

def getCaptcha(url):
	try:
		#downloading image
		urlResponse = urllib.request.urlopen(url)
		imgArray = np.array(bytearray(urlResponse.read()), dtype=np.uint8)
		image = cv2.imdecode(imgArray, -1)

		#image manipulation
		grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		image = cv2.copyMakeBorder(grey, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
		thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

		#detecting blobs of pixels
		characters = []
		blobs = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
		for blob in blobs:
			(x, y, w, h) = cv2.boundingRect(blob)
			characters.append((x, y, w, h))

		#check for accurate detection
		if len(characters) != 4:
			return {'success': False, 'captcha': None, 'msg': 'Failed to detect 4 characters'}

		#predictions of characters from left to right
		predictions = []
		characters = sorted(characters, key=lambda x: x[0])

		for character in characters:
			x, y, w, h = character
			characterImage = image[y - 2:y + h + 2, x - 2:x + w + 2]
			characterImage = resize_to_fit(characterImage, 20, 20)

			# expanding dimensions for keras
			characterImage = np.expand_dims(characterImage, axis=2)
			characterImage = np.expand_dims(characterImage, axis=0)

			prediction = model.predict(characterImage)
			ch = labels.inverse_transform(prediction)[0]
			predictions.append(ch)

		captcha = "".join(predictions)
		print("CAPTCHA text is: {}".format(captcha))
		return {'success': True, 'captcha': captcha}
	except:
		return {'success': False, 'msg': 'The URL is invalid or expired'}
