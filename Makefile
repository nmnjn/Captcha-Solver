clean:
	rm -rf extractedLetters
	rm model.hdf5
	rm labels.dat
download:
	python captchaDownloader.py
extract-data:
	python Helpers/lettersExtractor.py
train-model:
	python modelTrainer.py
captcha-test:
	python app.py
server:
	gunicorn --bind 0.0.0.0:5000 server:app
