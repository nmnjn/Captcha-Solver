clean:
	rm -rf extractedLetters
	rm model.hdf5
	rm labels.dat
download:
	python captchaDownloader.py
extract:
	python Helpers/lettersExtractor.py
train:
	python modelTrainer.py
captcha:
	python app.py
server:
	pip install flask
	pip install gunicorn
	gunicorn --bind 0.0.0.0:5000 server:app
