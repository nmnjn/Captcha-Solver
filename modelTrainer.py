import cv2
import pickle
import os.path
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense
from Helpers.helpers import resize_to_fit

LETTERS = "extractedLetters"
MODEL = "model.hdf5"
LABELS = "labels.dat"

data = []
labels = []

images = paths.list_images(LETTERS)
for image_file in images:
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = resize_to_fit(image, 20, 20)

    #expand dimension for keras
    image = np.expand_dims(image, axis=2)

    label = image_file.split(os.path.sep)[-2]
    data.append(image)
    labels.append(label)

data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

(xTrain, xTest, yTrain, yTest) = train_test_split(data, labels, test_size=0.25, random_state=0)

#save the labels to use for prediction. (using one-hot encoding)
lb = LabelBinarizer().fit(yTrain)
yTrain = lb.transform(yTrain)
yTest = lb.transform(yTest)

file = open(LABELS, 'wb')
pickle.dump(lb, file)
file.close()

model = Sequential()

model.add(Conv2D(20, (5, 5), padding="same", input_shape=(20, 20, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Conv2D(50, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Flatten())
model.add(Dense(500, activation="relu"))

model.add(Dense(27, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(xTrain, yTrain, validation_data=(xTest, yTest), batch_size=27, epochs=10, verbose=1)

model.save(MODEL)
