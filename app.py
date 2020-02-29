from flask import Flask, jsonify, request
from captchaSolver import getCaptcha
import flask_profiler

app = Flask(__name__)

app.config["flask_profiler"] = {
        "enabled": True,
        "storage": {
            "engine": "sqlite"
         },
        "basicAuth":{
            "enabled": True,
            "username": "admin",
            "password": "password"
        }
     }



@app.route('/solve', methods=['GET'])
def solve():
	args = request.args
	if "url" in args:
		url = args["url"]
		print(url)
		resp = getCaptcha(url)
		return jsonify(resp)
	return "Please append a valid URL [?url=]"


flask_profiler.init_app(app)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000', threaded=True)
