# Captcha-Solver
A python application to solve the [SIS Portal](https://sis.manipal.edu) CAPTCHA using a custom trained model with TensorFlow and Keras.
___

#### Tools
- Python 3
- OpenCV
- Keras
- TensorFlow

#### Installation

###### Download the Source Code
```
git clone https://github.com/naman17/Captcha-Solver.git
(or download the zip)
```

###### Install the Requirements
```
cd Captcha-Solver
pip install -r requirements.txt
```

###### (Optional) Download a set of CAPTCHAs from the SIS Portal:
```
make download
```

#### Running the Script
###### Step 1 - Extracting Dataset:
```
make extract-data
```
###### Step 2 -  Training the Model:
```
make train-model
```

###### (Optional) To test the Script with a URL:
```
make captcha-test
```

###### (Optional) To start a server:
```
make server
```

The server will start on `localhost:5000`.
To test the server send a `get` request on `/solve?url=<append-url-here>`

<br>

_As a proof of concept you can test the script on `http://139.59.7.182:8001/solve?url=` by appending the CAPTCHA Image URL from the [SIS Portal](https://sis.manipal.edu/studlogin.aspx)._


![](/img/first.png)
![](/img/second.png)

---

###### (Optional) To clear all the datasets and model generated :
```
make clean
```
<br>

### Running with Docker
```
docker build -t sis-captcha-solver .
```

```
docker run --rm -it -p 5000:5000 sis-captcha-solver
```

The server will start on localhost:5000. 
To test the server send a get request on `/solve?url=<append-url-here>`

---
