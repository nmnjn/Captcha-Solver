FROM tensorflow/tensorflow:latest-py3

COPY requirements.txt /

RUN apt update && apt install -y libsm6 libxext6 libxrender-dev

RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

RUN python Helpers/lettersExtractor.py

RUN python modelTrainer.py

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 server:app
