clean:
	rm -rf extractedLetters
	rm model.hdf5
	rm labels.dat
setup:
	pip install -r requirements.txt
	sudo apt-get install libsm6 libxrender1 libfontconfig1
download:
	python captchaDownloader.py
extract:
	python Helpers/lettersExtractor.py
train:
	python modelTrainer.py
captcha:
	python app.py
server:
	gunicorn --bind 0.0.0.0:5000 server:app
