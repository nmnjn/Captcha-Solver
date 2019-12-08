from flask import Flask, jsonify, request
from captchaSolver import getCaptcha

app = Flask(__name__)

@app.route('/solve', methods=['GET'])
def solve():
	args = request.args
	if "url" in args:
		url = args["url"]
		print(url)
		resp = getCaptcha(url)
		return jsonify(resp)
	return "Please append a valid URL [?url=]"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='9999', threaded=True)
