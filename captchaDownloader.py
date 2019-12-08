from bs4 import BeautifulSoup
import urllib.request
import numpy
import cv2
import os

URL = "https://sis.manipal.edu/{}"
OUTPUT_FOLDER = 'downloadedCaptchas'

count = 1
total = 1000

def downloadCaptchaImage(url):
	global count
	print("[INFO] downloading image {}/{}".format(str(count), str(total)))
	url_response = urllib.request.urlopen(url)
	img_array = numpy.array(bytearray(url_response.read()), dtype=numpy.uint8)
	image = cv2.imdecode(img_array, -1)

	if not os.path.exists(OUTPUT_FOLDER):
		os.makedirs(OUTPUT_FOLDER)

	path = os.path.join(OUTPUT_FOLDER, "{}.png".format(str(count).zfill(6)))
	count = count + 1
	cv2.imwrite(path, image)


def getCaptchaURL(source):
	soup = BeautifulSoup(source, 'html.parser')
	images = soup.find_all('img')
	imageUrl = URL.format(images[2]['src'])
	return imageUrl


def downloadCaptchas():
	x = range(total)
	for n in x:
		resp = urllib.request.urlopen(URL.format('studlogin.aspx'))
		captachaURL = getCaptchaURL(resp.read())
		downloadCaptchaImage(captachaURL)

downloadCaptchas()
